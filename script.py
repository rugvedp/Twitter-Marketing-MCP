from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import os
import json
import requests
import tweepy
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
import uuid

mcp = FastMCP("Twitter Marketing MCP", dependencies=["tweepy", "google-genai"])

load_dotenv()

@mcp.tool()
def tweet(text: str, image_path: str = None) -> str:
    """ Text should be less than 280 characters and takes image filename as input """
    try:
        # Load credentials
        api_key = os.getenv('X_api_key')
        api_secret = os.getenv('X_api_key_sec')
        access_token = os.getenv('X_access_token')
        access_token_secret = os.getenv('X_access_token_sec')
        bearer_token = os.getenv('X_bearer_token')

        auth_v1 = tweepy.OAuth1UserHandler(api_key, api_secret)
        auth_v1.set_access_token(access_token, access_token_secret)
        client_v1 = tweepy.API(auth_v1, wait_on_rate_limit=True)

        client_v2 = tweepy.Client(
            bearer_token=bearer_token,
            consumer_key=api_key,
            consumer_secret=api_secret,
            access_token=access_token,
            access_token_secret=access_token_secret,
            wait_on_rate_limit=True
        )

        media_ids = None
        # Check if the image path is provided and exists

        if image_path:
            full_path = os.path.join("generated_images", image_path)
            if os.path.exists(full_path):
                print(full_path)
                media = client_v1.media_upload(filename=full_path)
                media_ids = [media.media_id]

        response = client_v2.create_tweet(text=text, media_ids=media_ids)
        return f"✅ Tweet posted: {response.data['id']}"


    except tweepy.TweepyException as e:
        return f"❌ Twitter error: {e}"

    except Exception as e:
        return f"❌ Unexpected error: {e}"
    


@mcp.tool()
def generate_image(prompt: str) -> str:
    """ returns the image filename in png format"""
    try:
        # Create a new folder for saving images if it doesn't exist
        image_folder = "generated_images"
        if not os.path.exists(image_folder):
            os.makedirs(image_folder)

        # Initialize the Gemini client
        client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp-image-generation",
            contents=prompt,
            config=types.GenerateContentConfig(response_modalities=['TEXT', 'IMAGE'])
        )

        # Check if an image was returned and save it
        for part in response.candidates[0].content.parts:
            if part.inline_data:
                image = Image.open(BytesIO(part.inline_data.data))
                # Generate a unique image filename
                image_filename = f"{uuid.uuid4().hex}.png"
                image_path = os.path.join(image_folder, image_filename)
                image.save(image_path)

                return image_filename

        return "❌ No image generated."

    except Exception as e:
        return f"❌ Error generating image: {e}"

@mcp.tool()
def web_scrape(query: str, country_code: str) -> str:
    """
    Web scrape using the Serper API to perform localized Google-like search.

    Args:
        query (str): Search query.
        country_code (str): Country code (e.g., 'us', 'in').

    Returns:
        str: Raw JSON response with search results.
    """
    try:
        url = "https://google.serper.dev/search"
        payload = json.dumps({"q": query, "gl": country_code})
        headers = {
            'X-API-KEY': os.getenv('serper_api'),
            'Content-Type': 'application/json'
        }

        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status()  # Raises error for bad status codes
        return response.text

    except requests.exceptions.RequestException as e:
        return f"❌ Web scraping error: {e}"

    except Exception as e:
        return f"❌ Unexpected error: {e}"
