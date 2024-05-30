
## Setup

### Install External Libraries
- `selenium`
- `requests`

### Code

Open a script in the `src` directory and start with the imports below to get started. 

```
import os, sys
sys.path.append('..')
import json
from src.scraper import scraper
```

`main.py` demonstrates how to use the scraper class, specifically its search_and_scrape() method provides. An important note about this method is that it returns a generator where each iteration is a single search result providing all of an items data. 

`main.py` iterates through a list of newline seperated keywords searching for up to 200 results for each keyword.

## eBay’s RESTful APIs

Yet another reason for using eBay’s API service is its transition from traditional API services to REST-based APIs. This shift is so profound that it alone justifies using this service. 

There are many reasons why REST-based APIs are superior to traditional services:

- **Scalability:** REST APIs are stateless, making them highly scalable and capable of handling large volumes of requests efficiently.
   
- **Atomicity of Calls:** Each API call in a RESTful system is atomic, meaning it is complete and self-contained. This simplifies error handling and ensures consistent interactions.

- **Flexibility:** REST APIs are flexible, allowing for multiple types of calls and data formats. They can adapt and evolve without breaking existing integrations.

- **Performance:** REST APIs leverage HTTP caching mechanisms, reducing server load and improving response times, leading to better overall performance.

## Sandbox Mode
Unfortunately, eBay's production API keys cannot be granted to developer simply because they want to work on a personal project, and will only be granted to companies or individuals under strict contract and monetary promise. However, eBay's generously has created and maintained a rich sandbox environment that allows developers to work/test on a simulated eBay website with all the same API's (for free)! Due to the large amount of quality item postings on sandbox eBay, this means developing this project in this environment hardly comes with any downsides!

### Signing Up to be a Developer
Signing up with eBay's developer program to access their sandbox APIs is simple and only takes a day for verification. Follow this link to sign up for API access (it's free!): [eBay Developer Program](https://developer.ebay.com/develop/get-started)

## The Right API: Buy APIs -> Browse API
With so many APIs to choose from, which one should we use? The goal is to obtain as much information about as many items as possible with minimal effort. eBay's Browse API (from the home developer page go to APIs -> RESTful APIs -> Buy APIs -> Browse API) provides the one golden call we'll need to collect tons of high-quality data: the **search** call.

Example Call Request Using search:
https://api.sandbox.ebay.com/buy/browse/v1/item_summary/search?q=watch&limit=3

Respective Output Example:
`{"itemId": "v1|110554920324|0", "title": "Szanto Heritage Aviator Watches, Black Dial, Tan Strap, Gun Gray, One : SZ 2757", "leafCategoryIds": ["31387"], "categories": [{"categoryId": "31387", "categoryName": "Wristwatches"}, {"categoryId": "281", "categoryName": "Jewelry & Watches"}, {"categoryId": "260324", "categoryName": "Watches, Parts & Accessories"}, {"categoryId": "260325", "categoryName": "Watches"}], "price": {"value": "225.00", "currency": "USD"}, "itemHref": "https://api.sandbox.ebay.com/buy/browse/v1/item/v1%7C110554920324%7C0", "seller": {"feedbackScore": 500}, "condition": "New with tags", "conditionId": "1000", "shippingOptions": [{"shippingCostType": "FIXED", "shippingCost": {"value": "0.00", "currency": "USD"}}], "buyingOptions": ["FIXED_PRICE", "BEST_OFFER"], "itemWebUrl": "http://www.sandbox.ebay.com/itm/Szanto-Heritage-Aviator-Watches-Black-Dial-Tan-Strap-Gun-Gray-One-SZ-2757-/110554920324?hash=item19bd963584:i:110554920324", "itemLocation": {"city": "Northbrook", "postalCode": "600**", "country": "US"}, "adultOnly": false, "legacyItemId": "110554920324", "availableCoupons": false, "itemCreationDate": "2024-05-02T20:25:40.000Z", ...`

## Selenium and the Description Parsing Issue
You may have noticed that the output is missing a crucial detail: the item description. According to eBay’s documentation, the shortDescriptions key should hold a short text description of the item. However, this key is not present for most sandbox items.

Since eBay formats their item descriptions as markups, effort is needed to scrape the markup data for the item description text. We can retrieve the item listing URL from the `"itemWebUrl"` field, as shown above. This URL can be opened with a Selenium WebDriver, using Chrome in this case.

Despite testing simple request parsing, it became clear that the URL must be loaded in a browser to obtain the necessary script containing the item description text. For more details, see `DataScraper/src/scraper.py`.

The same sample after adding the item description to the dictionary:
```{
    "itemId": "v1|110554920324|0",
    "title": "Szanto Heritage Aviator Watches, Black Dial, Tan Strap, Gun Gray, One : SZ 2757",
    "leafCategoryIds": [
        "31387"
    ],
    "categories": [
        {
            "categoryId": "31387",
            "categoryName": "Wristwatches"
        },
        {
            "categoryId": "281",
            "categoryName": "Jewelry & Watches"
        },
        {
            "categoryId": "260324",
            "categoryName": "Watches, Parts & Accessories"
        },
        {
            "categoryId": "260325",
            "categoryName": "Watches"
        }
    ],
    "price": {
        "value": "225.00",
        "currency": "USD"
    },
    "itemHref": "https://api.sandbox.ebay.com/buy/browse/v1/item/v1%7C110554920324%7C0",
    "seller": {
        "feedbackScore": 500
    },
    "condition": "New with tags",
    "conditionId": "1000",
    "shippingOptions": [
        {
            "shippingCostType": "FIXED",
            "shippingCost": {
                "value": "0.00",
                "currency": "USD"
            }
        }
    ],
    "buyingOptions": [
        "FIXED_PRICE",
        "BEST_OFFER"
    ],
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

## Notes for Future Endevor
- For production keysets API usage ratings must be obeyed. See `SEE URL` for more details.
- This is SLOW. Look into threading requests or generally implementing multiprocessing techniques. 
