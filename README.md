# Flipkart-Scraping
Python script to scrape product data from Flipkart and save it as CSV. Easily search, scrape, and analyze product details.

## Overview
This Python script scrapes product information from the Flipkart website based on user input. It extracts details such as image URL, product name, product price and product rating from the search results page and stores them in a CSV file.

## How It Works
User Input: The script prompts the user to enter the product they want to search for on Flipkart.

Scraping Flipkart: It then sends a request to Flipkart's search page for the specified product and extracts relevant information from the HTML response.

Extracting Product Information: The script looks for specific HTML elements and classes (_1AtVbE, _4rR01T, _30jeq3, _3LWZlK, _396cs4) to extract product details such as name, price, rating, and image URL.

Storing in CSV: The extracted information is stored in a Pandas DataFrame and then saved to a CSV file with a filename based on the user input.

## Limitations
Dependent on HTML Structure: The script relies on specific HTML classes and structures present in Flipkart's search results page. If Flipkart changes the structure of their website or if the product being searched for has a different HTML structure, the script may not work properly.

Limited Error Handling: The script provides basic error handling for HTTP requests and HTML parsing errors. However, it may not handle all possible edge cases or network issues.

## Usage
Clone the repository or download the script (flipkart_scraper.py).
Install the required Python dependencies (requests, beautifulsoup4, pandas).
Run the script (python flipkart_scraper.py) and follow the prompts to search for a product on Flipkart.
The script will generate a CSV file containing the product details in the current directory.
Additionally, you can run the script from a Jupyter Notebook (flipkart_scraper.ipynb) for interactive usage and analysis.

## Example Inputs
Macbook,
Mobile,
Washing Machine,
Front Load Washing Machine,
Refrigerator

## Dependencies
Python 3.x,
requests,
beautifulsoup4,
pandas

These example inputs provide users with ideas of the types of products that can be search for using the script. It can be replace other specific product searches.
