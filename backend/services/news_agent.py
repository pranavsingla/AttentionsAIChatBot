import requests
import time

def get_news(city, date, max_retries=3, backoff_factor=1):
    url = f"https://api.gdeltproject.org/api/v2/doc/doc?query={city}&mode=artlist&maxrecords=10&format=json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    for retry in range(max_retries):
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            try:
                data = response.json()
                # print("Data fetched:", data)  # Check the structure of the JSON
                if 'articles' in data:
                    return [article['title'] for article in data['articles']]
                else:
                    # print("No articles key in data:", data)  # Debugging
                    return ["News data not available"]
            except requests.exceptions.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
                return ["Invalid JSON response"]
        
        elif response.status_code == 429:
            # Too many requests, wait and retry
            time.sleep(backoff_factor * (2 ** retry))
        else:
            print(f"Request failed with status code {response.status_code}")
            print("Response content:", response.content)  # Print the full response content for debugging
            return ["Failed to fetch news data"]
    
    return ["Too many requests. Please try again later."]



# import requests
# import time

# def get_news(city, date, max_retries=3, backoff_factor=1):
#     url = f"https://api.gdeltproject.org/api/v2/doc/doc?query={city}&mode=artlist&maxrecords=10&format=json"
    
#     for retry in range(max_retries):
#         response = requests.get(url)
#         print("\n\n\n",response, "\n\n\n")
        
#         if response.status_code == 200:
#             try:
#                 data = response.json()
#                 # Extracting titles from the articles
#                 if 'articles' in data:
#                     return [article['title'] for article in data['articles']]
#                 else:
#                     return ["News data not available"]
#             except (requests.exceptions.JSONDecodeError, KeyError) as e:
#                 return ["News data not available"]
#         elif response.status_code == 429:
#             # Wait before retrying
#             time.sleep(backoff_factor * (2 ** retry))
#         else:
#             return ["Failed to fetch news data"]
    
#     return ["Too many requests. Please try again later."]




# import requests

# def get_news(city, date):
#     api_key = "your_api_key"
#     url = f"https://newsapi.org/v2/everything?q={city}&from={date}&sortBy=publishedAt&apiKey={api_key}"
#     response = requests.get(url)
#     data = response.json()
#     return [article['title'] for article in data['articles']]
