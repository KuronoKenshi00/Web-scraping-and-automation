import os
import requests
from bs4 import BeautifulSoup

# Function to scrape paragraphs related to a heading
def scrape_paragraphs(url, heading):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all <h2> headings
        headings = soup.find_all('h2')

        # Loop through the <h2> headings and search for the specified heading
        for h2 in headings:
            if h2.text.strip() == heading:
                # Find the next sibling of the heading, which contains the paragraphs
                next_element = h2.find_next_sibling()
                # Loop through the siblings until the next heading is encountered
                while next_element and next_element.name != 'h2':
                    if next_element.name == 'p':
                        paragraphs.append(next_element.text.strip())
                    next_element = next_element.find_next_sibling()
                break
    else:
        print(f"Failed to retrieve the Wikipedia page for heading: {heading}")

# Function to find all headings on the web page
def find_all_headings(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all <h2> headings
        headings = soup.find_all('h2')

        # Extract the text of each heading
        heading_texts = [heading.text.strip() for heading in headings]

        return heading_texts
    else:
        print("Failed to retrieve the Wikipedia page.")
        return []

# URL of the Wikipedia page
url = 'https://en.wikipedia.org/wiki/Wikipedia'

# Find all headings on the web page
headings = find_all_headings(url)

# Prompt the user to select a heading
print("Select a heading from the following list:")
for idx, heading in enumerate(headings):
    print(f"{idx + 1}. {heading}")

selected_index = int(input("Enter the index of the heading you want to search for: "))
selected_heading = headings[selected_index - 1]

# Scrape paragraphs for the selected heading
paragraphs = []
scrape_paragraphs(url, selected_heading)

# Save the scraped paragraphs to a text file
file_path = 'scraped_paragraphs.txt'
with open(file_path, 'w') as file:
    for paragraph in paragraphs:
        file.write(paragraph + '\n')

print(f"Scraped paragraphs saved to '{os.path.abspath(file_path)}'.")

