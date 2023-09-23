'''
Author: Verbit
Date: 23 September 2023
!pip install bs4
'''


from bs4 import BeautifulSoup
import requests
url="https://play.google.com/store/apps/details?id=python.programming.coding.python3.development&hl=en&gl=US"

def return_email(url):
    response = requests.get(url)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all <a> tags with href starting with "mailto:"
        email_links = soup.find_all('a', href=lambda href: href and href.startswith('mailto:'))

        # Extract the email addresses
        for email_link in email_links:
            email = email_link['href'][7:]  # Remove "mailto:" prefix
            return email
    else:
        return ""
    

email=return_email(url)
print(email)
