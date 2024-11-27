import requests
import sys
import argparse

def validate_url(url):
    """Check if a URL is reachable."""
    try:
        response = requests.head(url, timeout=5)
        return response.status_code < 400
    except requests.RequestException as e:
        print(f"Error validating URL: {e}")
        return False

def shorten_url(url):
    """Shorten a URL using TinyURL."""
    api_url = f"http://tiny.cc/api?c=rest_api&s=tiny.cc&version=2.0.3&login=your_tinycc_email&apikey=your_tinycc_api_key&output=xml&short={url}"
    try:
        response = requests.get(api_url, timeout=5)
        if response.status_code == 200:
            # Assuming XML response; for simplicity, this example doesn't parse XML.
            # In a real scenario, use an XML parser to extract the shortened URL.
            # For this demo, we'll just return a success message with the original URL.
            return f"Shortening successful. Original URL: {url}"
        else:
            return f"Failed to shorten URL. Status Code: {response.status_code}"
    except requests.RequestException as e:
        return f"Error shortening URL: {e}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Validate and shorten a URL.')
    parser.add_argument('url', type=str, help='The URL to validate and shorten.')
    args = parser.parse_args()
    
    if validate_url(args.url):
        print(f"Valid URL: {args.url}")
        result = shorten_url(args.url)
        if "successful" in result:
            # For demo purposes, the actual shortened URL isn't extracted from the TinyURL response.
            # Replace with actual extraction logic.
            print(f"Shortened URL: http://tiny.cc/XXXXXX")
        else:
            print(f"Invalid URL or failed to shorten: {args.url}")
            print(f"Error Message: {result}")
    else:
        print(f"Invalid URL or failed to shorten: {args.url}")
