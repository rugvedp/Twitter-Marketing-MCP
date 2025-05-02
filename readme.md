# Twitter Marketing MCP

This repository contains the **Twitter Marketing MCP**, a tool designed to streamline social media marketing tasks using Python. It includes features for tweeting, image generation, and web scraping.

## Video Demonstration

Watch the video demonstration of the **Twitter Marketing MCP** in action:  
[![Demo](https://imagekit.io/tools/asset-public-link?detail=%7B%22name%22%3A%22screenshot_1746178835929.png%22%2C%22type%22%3A%22image%2Fpng%22%2C%22signedurl_expire%22%3A%222028-05-01T09%3A40%3A33.818Z%22%2C%22signedUrl%22%3A%22https%3A%2F%2Fmedia-hosting.imagekit.io%2F33b7f5ba913347cd%2Fscreenshot_1746178835929.png%3FExpires%3D1840786834%26Key-Pair-Id%3DK2ZIVPTIP2VGHC%26Signature%3D06js~0NLS0YWydyud9a-Gf9QumEnCyA9QyWDl6aYpqGkRHtIHzIq0kDzbIz2Ls3bQ9oRUa-YMeyuwruwZ3NbbYxwtBJtMKg4RLEz-VJjspBi~W9u1MTeOyFevPhdKpf~0cBs2TNZ-kARliO06MSkjyyl6gweO~szeiJLkmMp2Gyw17Wt--AcF6sukIrd1fxKBelsKpesX02FQWnxtqAIRD2P-THIZ9xqEUmxDAuTvRJHnmTUnQwN4znzca1OUam6-qI65YGlS3ueaGq8GI9l9lH2JShlxPSmcf6-0gfyc-YusZoiBO3wUvoaXE7zggN3qNz5lkq2YGd5Qevdqgd-bQ__%22%7D)](working.mp4)


## Features

### 1. **Tweet Posting**
Post tweets with or without images directly to Twitter.  

### 2. **Image Generation**
Generate images based on text prompts using Google's Gemini API.  

### 3. **Web Scraping**
Perform localized Google-like searches using the Serper API.  

## Installation

1. Clone the repository:
     ```bash
     git clone https://github.com/rugvedp/Twitter-Marketing-MCP.git
     cd Twitter-Marketing-MCP
     ```

2. Install dependencies:
     ```bash
     pip install requirements.txt
     mcp install script.py
     ```

3. Create a `.env` file with the following keys:
     ```env
     X_api_key=<your_twitter_api_key>
     X_api_key_sec=<your_twitter_api_secret>
     X_access_token=<your_twitter_access_token>
     X_access_token_sec=<your_twitter_access_token_secret>
     X_bearer_token=<your_twitter_bearer_token>
     GEMINI_API_KEY=<your_gemini_api_key>
     serper_api=<your_serper_api_key>
     ```

## Usage 

Open your claude desktop you will see the Twitter Marketing MCP` is ready to use.

If not then Copy paste the `config.json` into your claude_desktop_config.json

## Folder Structure
```
.
├── generated_images/   # Folder for storing generated images
├── script.py           # MCP core logic
├── .env                # Environment variables
├── requirements.txt    # Python dependencies
└── readme.md           # Project documentation
```

## License
This project is licensed under the MIT License.  
