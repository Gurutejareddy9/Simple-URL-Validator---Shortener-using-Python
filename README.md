# Simple URL Validator & Shortener using Python

## Overview
This Python script validates if a given URL is reachable and then shortens it using the TinyURL API. It's a simple demonstration of URL manipulation and API interaction.

## Installation

To run this script, ensure you have Python installed on your system. Additionally, you'll need to install the `requests` library if you haven't already:
```
pip install requests
```

## Example Output
 If the URL is valid and the shortening process succeeds:

 > Valid URL: https://www.example.com    
 > Shortened URL: http://tiny.cc/XXXXXX

 If the URL is invalid or shortening fails:

 > Invalid URL or failed to shorten: https://www.example.com     
 > Error Message: [Displayed if any]

## Important Notes:

1. TinyURL API: This script uses TinyURL's API for demonstration. You should replace your_tinycc_email and your_tinycc_api_key with your actual TinyURL credentials if you plan to use this script beyond testing.
2. Note: As of my last update, TinyURL's API might require adjustments in the script for proper usage, including handling the response to extract the shortened URL correctly.
3. XML Parsing: The script simplifies the response handling from TinyURL. For production use, implement proper XML parsing to extract the shortened URL.
Error Handling: Enhanced error handling can be implemented for more robustness, especially around network errors and API response parsing.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
