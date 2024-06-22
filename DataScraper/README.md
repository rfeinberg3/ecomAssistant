# eBay Item Data Scraper

## Setup

### Install External Libraries
- Using conda:
```bash
conda env create --file requirements.txt --name scraper
conda activate scraper
```
- Using pip:
```bash
pip install requests
pip install selenium
```
- Using Docker:
```bash
docker build -t eas:scraper .
docker run eas:scraper
```

- Eventually this will be its own container.

### Code

Open a script in the `src` directory and start with the imports below to get started. 

```
import json
from scraper import scraper
```

`main.py` demonstrates how to use the scraper class, specifically its search_and_scrape() method provides. An important note about this method is that it returns a generator where each iteration is a single search result providing all of an items data. 

`main.py` iterates through a list of newline seperated keywords searching for up to 200 results for each keyword.


## Data

`outputs` was generated using eBay API search calls on a set of keywords with the limit set to 200 (`scraper.search_and_scrape(keyword, 200)`).

Keyword text file examples can be seen in the `src/keywords` directory. To obtain the lists, ChatGPT-4o was prompted for a keywords list. An example prompt:

"""Give me a common and diverse set of items you would typically find on eBay such as these:
Watch
Technology
Cars
Games
Shoes
Clothes

I am prompting a datascraper to search these items and collect there data for model training. Extend the list above with as many items as you deem necessary for a diverse model training dataset. Format your response as newline seperated item keywords like above."""

## Background

### Why eBay?

With numerous e-commerce websites available, why choose eBay? While it may not be everyone's favorite e-commerce platform, eBay stands out for several critical reasons:

1. **Open-Source API Support:** eBay is the most well-known e-commerce website that supports open-source RESTful API calls. Unlike more popular services like Facebook Marketplace and OfferUp, eBay offers public APIs.

2. **Extensive Developer Support:** eBay provides consistent updates, maintenance, and community engagement events, ensuring a reliable and up-to-date API service.

3. **Vast and High-Quality Data:** eBay offers superior data quantity and quality compared to sites like Etsy or Shopify. This data is crucial for training a model to generate descriptions of everyday items for resale. Unlike Shopify and Etsy, which cater more to entrepreneurial startups, eBay's data is well-suited for this purpose.

#### eBay’s RESTful APIs

Another reason for using eBay’s API service is its transition from traditional APIs to REST-based APIs. This shift justifies using this service due to several advantages:

- **Scalability:** REST APIs are stateless, making them highly scalable and capable of handling large volumes of requests efficiently.

- **Atomicity of Calls:** Each API call in a RESTful system is atomic, meaning it is complete and self-contained, simplifying error handling and ensuring consistent interactions.

- **Flexibility:** REST APIs are flexible, supporting multiple types of calls and data formats. They can adapt and evolve without breaking existing integrations.

- **Performance:** REST APIs leverage HTTP caching mechanisms, reducing server load and improving response times for better overall performance.


## Notes 

### Sandbox Mode
Unfortunately, eBay's production API keys cannot be granted to developer simply because they want to work on a personal project, and will only be granted to companies or individuals under strict contract and monetary promise. However, eBay's generously has created and maintained a rich sandbox environment that allows developers to work/test on a simulated eBay website with all the same API's (for free)! Due to the large amount of quality item postings on sandbox eBay, this means developing this project in this environment hardly comes with any downsides!

#### Signing Up to be a Developer
Signing up with eBay's developer program to access their sandbox APIs is simple and only takes a day for verification. Follow this link to sign up for API access (it's free!): [eBay Developer Program](https://developer.ebay.com/develop/get-started)

### The Right API: Buy APIs -> Browse API
With so many APIs to choose from, which one should we use? The goal is to obtain as much information about as many items as possible with minimal effort. eBay's Browse API (from the home developer page go to APIs -> RESTful APIs -> Buy APIs -> Browse API) provides the one golden call we'll need to collect tons of high-quality data: the **search** call.

Example Call Request Using search:
https://api.sandbox.ebay.com/buy/browse/v1/item_summary/search?q=watch&limit=3

Respective Output Example (some lines redacted):
`{"itemId": "v1|110554920324|0", "title": "Szanto Heritage Aviator Watches, Black Dial, Tan Strap, Gun Gray, One : SZ 2757", ...REDACTED LINES..., "itemWebUrl": "http://www.sandbox.ebay.com/itm/Szanto-Heritage-Aviator-Watches-Black-Dial-Tan-Strap-Gun-Gray-One-SZ-2757-/110554920324?hash=item19bd963584:i:110554920324", "itemLocation": {"city": "Northbrook", "postalCode": "600**", "country": "US"}, "adultOnly": false, "legacyItemId": "110554920324", "availableCoupons": false, "itemCreationDate": "2024-05-02T20:25:40.000Z", ...REDACTED LINES...}`

### Selenium and the Description Parsing Issue
You may have noticed that the output is missing a crucial detail: the item description. According to eBay’s documentation, the shortDescriptions key should hold a short text description of the item. However, this value is not present for most sandbox items.

Since eBay formats their item descriptions as markups, effort is needed to scrape the markup data from the item description text. We can retrieve the item listing URL from the `"itemWebUrl"` field, as shown above. This URL can be opened with a Selenium WebDriver, using Chrome in this case.

Despite testing simple request parsing, it became clear that the URL must be loaded in a browser to obtain the necessary script containing the item description text. For more details, see `DataScraper/src/scraper.py`.

The same sample after adding the item description to the dictionary (some lines redacted):
```{
    "itemId": "v1|110554920324|0",
    "title": "Szanto Heritage Aviator Watches, Black Dial, Tan Strap, Gun Gray, One : SZ 2757",
    ...REDACTED...
    "itemWebUrl": "http://www.sandbox.ebay.com/itm/Szanto-Heritage-Aviator-Watches-Black-Dial-Tan-Strap-Gun-Gray-One-SZ-2757-/110554920324?hash=item19bd963584:i:110554920324",
    "itemLocation": {
        "city": "Northbrook",
        "postalCode": "600**",
        "country": "US"
    },
    "adultOnly": false,
    "legacyItemId": "110554920324",
    "availableCoupons": false,
    "itemCreationDate": "2024-05-02T20:25:40.000Z",
    "topRatedBuyingExperience": false,
    "priorityListing": false,
    "listingMarketplaceId": "EBAY_US",
    "item_description": "Featured Items\nSport Optics\nHunting\nShooting Gear\nOutdoor Gear\nApparel\nEyewear\nMilitary & Tactical\nPolice, EMS & Fire\nSports & Hobbies\nLab & Science\nEverything Else\nCategories\nApparel\nUndershirts\nEverything Else\nCamera Cases\nHunting\nRiflescope Mounts and Bases\nShooting Gear\nTargets\nSport Optics\nBinoculars\nOpen Box Specials\nPopular Brands\nZeiss\nVortex\nBurris\nBushnell\nLeopold\nNightforce\nNikon\nThis Stock Photo may not match the actual item listed.\nThis listing is for Model # SZ-2757\nSzanto Heritage Aviator Watches\nSpecification: Szanto Heritage Aviator Watches, Black Dial, Tan Strap, Gun Gray, One Size, SZ 2757\nProduct Code: SZA-WT-HL04-SZ-2757\nModel Number: 
    ... 30 lines redacted ... 
    phone call, e-mail, fax and even livechat, so don't hesitate to contact us!\nSign up for our Newsletter\nSubscribe to our newsletter to stay up to date with the latest products from OpticsPlanet\nSIGN UP\nWhy Buy From Us?\nFree Shipping on Most Orders\nNo Sales Tax for Most Orders\nSafe & Secure Shopping\nCustomer Feedback\nWe Value Your Privacy\nCustomer Service\nReturns & Exchanges\nShipping Policy\nContact Us\nHours of Operation\n9am - 5:30pm CT Mon-Fri (Calls, Chats & Emails)\n\u00a9 Copyright 1999-2017 OpticsPlanet"
}
```


## Future Work
- Finding the length in of time an item was listed for before it was sold would a fantastic statistic to have. This would allow for a profound recognition of what items are selling well.
    - This would only matter for production key calls, as sandbox listing dates most likely hardly mean anything.
    -  This would likely involve using a Sell API or Analytics API call.
- For production keysets API usage ratings must be obeyed. Production development will need caching and retry mechanisms to handle rate limit exceedances gracefully. 
- This is SLOW. Look into threading requests or implementing multiprocessing techniques. 
