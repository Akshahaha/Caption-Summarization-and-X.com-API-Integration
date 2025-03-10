Instagram Caption Summarization and X (Twitter) API Integration

This project scrapes Instagram post captions, summarizes them using Google's Gemini API, and posts the summarized caption as a tweet on X (formerly Twitter).

Features

Scrapes Instagram post details (caption and image URL)

Summarizes captions using Google's Gemini API

Posts summarized text to X (Twitter) using Tweepy

Provides API endpoints via Flask for integration

Requirements

Install the following dependencies using pip:

pip install requests beautifulsoup4 tweepy google-generativeai flask python-dotenv

Environment Variables

Create a .env file in the project directory with the following keys:

GOOGLE_API_KEY=<YOUR_GOOGLE_API_KEY>
X_BEARER_TOKEN=<YOUR_X_BEARER_TOKEN>
X_CONSUMER_KEY=<YOUR_X_CONSUMER_KEY>
X_CONSUMER_SECRET=<YOUR_X_CONSUMER_SECRET>
X_ACCESS_TOKEN=<YOUR_X_ACCESS_TOKEN>
X_ACCESS_TOKEN_SECRET=<YOUR_X_ACCESS_TOKEN_SECRET>

Usage

1. Run the Flask Server

python main.py

2. API Endpoints

Summarize and Post Tweet

POST /post-tweet

Body:

{
    "caption": "Your Instagram caption text here"
}

Scrape Instagram Post and Post to X

GET /scrape-and-tweet

3. Sample Response

{
    "message": "Tweet posted successfully!"
}

Project Structure

.
├── main.py
├── .env
├── requirements.txt
└── README.md

Important Notes

Ensure your .env file is not included in your public repository.

Google's Gemini API and X credentials must be securely stored.
