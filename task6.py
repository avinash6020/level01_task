import requests
from bs4 import BeautifulSoup

def fetch_data(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup
    else:
        print("Failed to fetch data from the website.")
        return None

def present_data(soup):
    # Example: Display the titles of all <h1> tags
    headings = soup.find_all('h1')
    for heading in headings:
        print(heading.text)

# Main function
def main():
    # Step 1: Select a website and identify the data to be scraped
    url = input("Enter the URL of the website you want to scrape: ")
    
    # Step 2: Utilize a web scraping library to fetch the data
    soup = fetch_data(url)
    
    if soup:
        # Step 3: Design a user-friendly presentation format
        present_data(soup)

# Execute the main function
if __name__ == "__main__":
    main()
