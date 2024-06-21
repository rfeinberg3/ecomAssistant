import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By # Locator object
import time

from oauthlibrary.oauth_authentication import oauth_authentication


class scraper:
    def __init__(self, environment_type='sandbox'):
        self.environment_type = environment_type

    def _get_authentication_token(self):
        return oauth_authentication().get_authentication_token()

    # Uses drivers to parse javascript for item description
    def _extract_item_description(self, url):
        options = Options() 
        options.add_argument('--headless') # Run browser in the background
        browser = webdriver.Chrome(options=options) 

        browser.get(url) # Load the browser with the given url
        time.sleep(5) # Wait to let javascript load

        description_iframe = browser.find_element(By.TAG_NAME, 'iframe') # Locate the first iframe tag in the webpage HTML (this is where the formated description is)
        
        if description_iframe:
            item_description_url = description_iframe.get_attribute('src') # src contains the link to the item description page
            browser.get(item_description_url) # Open item description url
            time.sleep(5) # Wait to let javascript load
            item_description = browser.find_element(By.TAG_NAME, 'body') # Body contains the text attribute
            return item_description.text
        else:
            raise Exception("Failed to find the description iframe in the HTML content")
        
    # Search for items
    def search_and_scrape(self, keyword, limit='1', offset='0', deep_search=False):
        """
        Be sure to include reference about the lines of code below.
        https://developer.ebay.com/api-docs/buy/browse/resources/item_summary/methods/search
        """
        # Setup parameters for API call
        oauth_token = self._get_authentication_token()
        headers = {
            'Content-Type' : 'application/json',
            'Authorization' : 'Bearer ' + oauth_token
        }
        params = {
            'q': keyword, # Item type to search for.
            'fieldgroups' : 'EXTENDED,MATCHING_ITEMS', # Extended will work for production ebay calls to return short descriptions of items.
            'limit': limit,  # Number of items to return.
            'offset': offset # Skip this number of items before scanning items to return in the response load.
        }
        if deep_search:
            params['filter'] = 'searchInDescription:true'
        api_url = 'https://api.sandbox.ebay.com/buy/browse/v1/item_summary/search'
        # Send API call request
        response = requests.get(api_url, headers=headers, params=params)
        response.raise_for_status()
        # Get item data
        content = response.json()
        if "itemSummaries" in content:
            for item_data in content["itemSummaries"]:
                  ##print(json.dumps(item_data, indent=4))
                # Add item description to item data dictionary
                try:
                    item_description = self._extract_item_description(item_data["itemWebUrl"])
                    item_data["item_description"] = item_description
                    yield item_data # Makes dataset builder faster!
                except Exception as e:
                    print(e)
        else:
            return [""]

    @DeprecationWarning
    def extract_item_specifics(url): 
        # Send a GET request to the URL
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Failed to load page. Status code: {response.status_code}")
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        # Identify and extract the specifics section
        description_section = soup.find('div', {'id': 'viTabs_0_is'}) # 
        if description_section:
            #description_html = description_section.decode_contents(indent_level=4)  # Extract HTML content as a string
            description_text = description_section.get_text(separator=" ", strip=True) # Extract plain text content
            return description_text
        else:
            raise Exception("Failed to find the specifics section in the HTML content")
