import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By # Locator object
import time
from .oauthlibrary import oauth

SANDBOX = 'SANDBOX'
PRODUCTION = 'PRODUCTION'

class scraper:
    '''
      Takes in a environement type, 'SANDBOX' or 'PRODUCTION', to initialize an eBay item datascraper. \n
    Calling the main method `search_and_scrape` with desired parameters returns a generator which returns \n
    all available item details on each iteration.

    Args:  
        environement (str): 'SANDBOX' or 'PRODUCTION' for sandbox or production keyset respectively.
        keyset (str): Name of your keyset.
        keysetConfigPath (str): Path to you keyset config file containing your keyset credentails.
    '''
    def __init__(
            self,
            environment: str,
            keyset: str,
            keysetConfigPath: str,
        ) -> None:
        self.environment = environment
        self.keyset = keyset
        self.keysetConfigPath = keysetConfigPath

       # Search for items
    def search_and_scrape(
            self,
            keyword: str,
            limit: str = '1',
            offset: str = '0',
            deepSearch: bool = False):
        '''
          See how POST requests for RESTful API search calls are formatted below: \n
        https://developer.ebay.com/api-docs/buy/browse/resources/item_summary/methods/search

          Max limit is 200 and offset must be a multiple of limit or error will occur. \n
        deepSearch=True looks into an items description for keyword references.

        Args:
            - keyword: A string word used by eBay's search call to find pertinent item listings.
            - limit: The max number of items to return from the search call. Max limit is 200.
            - offset: how many items to skip over before beginning to return them. Must be a multiple of limit or error will occur.
            - deepSearch: If True, looks an items description for instances of keywords. (Should usually be ignored).
        '''
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
        params['filter'] = 'searchInDescription:true' if deepSearch == True else 'searchInDescription:false'
        # Setup Environment
        if self.environment == SANDBOX:
            apiUrl = 'https://api.sandbox.ebay.com/buy/browse/v1/item_summary/search'
        elif self.environment == PRODUCTION:
            apiUrl = 'https://api.ebay.com/buy/browse/v1/item_summary/search'
        else:
            raise ValueError("environment parameter must either 'SANDBOX' or 'PRODUCTION'.")
        # Send API call request
        response = requests.get(apiUrl, headers=headers, params=params)
        response.raise_for_status()
        # Get item data
        content = response.json()
        if "itemSummaries" in content:
            for item_data in content["itemSummaries"]:
                # Add item description to item data dictionary
                try:
                    itemDescription = self._extract_item_description(item_data["itemWebUrl"])
                    item_data["itemDescription"] = itemDescription
                    yield item_data # Makes dataset builder faster!
                except Exception as e:
                    print(e)
        else:
            return [""]

    def _get_authentication_token(self) -> str:
        ''' Call oauth to get authentication token for eBay API calls '''
        return oauth(
            environment=self.environment,
            keyset=self.keyset,
            keysetConfigPath=self.keysetConfigPath
        ).get_authentication_token()

    # Uses drivers to parse javascript for item description
    def _extract_item_description(self, url: str) -> str:
        '''
          Uses Selenium Chrome webdrivers to extract descriptions from items with the web url \n
        returned from the search_and_scrape() method. This has to be done because eBay's \n
        search API doesn't return these descriptions.

        Args:
            - url: String to the web address of the posted item.
        Returns:
            - The items description parsed from HTML.
        '''
        options = Options() 
        options.add_argument('--headless') # Run browser in the background
        browser = webdriver.Chrome(options=options) 

        browser.get(url) # Load the browser with the given url
        #time.sleep(5) # Wait to let iframe load. (Might not actually be needed)

        description_iframe = browser.find_element(By.TAG_NAME, 'iframe') # Locate the first iframe tag in the webpage HTML (this is where the formated description is)
        
        if description_iframe:
            item_description_url = description_iframe.get_attribute('src') # src contains the link to the item description page
            browser.get(item_description_url) # Open item description url
            item_description = browser.find_element(By.TAG_NAME, 'body') # Body contains the text attribute
            return item_description.text
        else:
            raise Exception("Failed to find the description iframe in the HTML content")

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
