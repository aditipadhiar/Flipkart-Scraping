import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_flipkart_search(query):
    base_url = f"https://www.flipkart.com/search?q={query}"
    try:
        all_product_info = []
        page_number = 1
        max_retries = 3  # Maximum number of retries
        retries = 0
        while True:
            url = base_url + f'&page={page_number}'
            response = requests.get(url)
            
            # Retry if server error occurs
            if response.status_code == 500 and retries < max_retries:
                retries += 1
                print(f"Retrying request for page {page_number}...")
                time.sleep(2)  # Wait for a few seconds before retrying
                continue
            
            response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)
            soup = BeautifulSoup(response.content, 'html.parser')
            product_info = []
            for product in soup.find_all('div', class_='_1AtVbE'):
                name_tag = product.find('div', class_='_4rR01T')
                price_tag = product.find('div', class_='_30jeq3')
                rating_tag = product.find('div', class_='_3LWZlK')
                image_tag = product.find('img', class_='_396cs4')
                
                # Check if all required tags are found
                if name_tag and price_tag and image_tag:
                    name = name_tag.text.strip()  # Remove leading/trailing whitespace
                    price = price_tag.text.strip()
                    image_url = image_tag['src']  # Extract image URL
                    
                    # Check if rating tag exists
                    if rating_tag:
                        rating = rating_tag.text.strip()
                    else:
                        rating = ""  # Set rating to an empty string if not available
                    
                    product_info.append({'Image': image_url, 'Name': name, 'Price': price, 'Rating': rating})
            
            # Append product info to the list
            all_product_info.extend(product_info)
            
            # Check if there are more pages to scrape
            next_button = soup.find('a', class_='_1LKTO3')
            if not next_button or 'disabled' in next_button.get('class', []):
                break  # No more pages to scrape
            
            # Move to the next page
            page_number += 1
        
        return all_product_info
    except Exception as e:
        print("Error occurred:", e)
        return None

# Take user input for the product search query
query = input("Enter the product you want to search for on Flipkart: ")

# Scrape Flipkart for the given query
product_info = scrape_flipkart_search(query)

if product_info:
    # Store the results in a DataFrame
    df = pd.DataFrame(product_info)
    print("Product details stored in DataFrame:")
    print(df.to_string())
    
    # Save the DataFrame to a CSV file
    csv_filename = f"product_details_{query}.csv"
    df.to_csv(csv_filename, index=False)
    print(f"Product details saved to {csv_filename}")
else:
    print("No product details retrieved from Flipkart.")
