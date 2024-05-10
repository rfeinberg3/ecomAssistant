# ebay_Auto_Seller
Generates descriptions for images of items users would like to sell/resell (on eBay).
[Uploading project_graph.pdf…]()

## Component Plan

Defining inputs for three microservices:
 
###	API scraping service: This tool obtains product information from eBay and sends it to a preprocessor to be placed in a database.
-	Inputs: 
1.	Developer Parameters: ( type = strings )
There will be a few tweakable parameters in the API scraping service to allow for simple and robust data scraping. 
2.	Raw Seller Data: ( type = tuple(strings) )
This data will be returned to the scraping service based on format that the API calls return.
-	Outputs: 
1.	Refined Seller Data: ( type = (string, string) )
List of string pairs describing products. Formatted as (description, item name) pairs.
 
###	Database preprocessing service: This tool obtains lists of product information from API scraper and organizes them for model training/lookup.
-	Input: 
1.	Refined Seller Data: ( type = (string, string) )
List of string pairs describing products. Formatted as (description, item name) pairs.
-	Output:
1.	Training Files: ( type = json )
json files designed for a model training scheme.
2.	Database Push Request: (type = string )
Requests to push the json file to a database.
 
###	RAG model service: This tool obtains queries from a user and consults a database before returning a prompt
-	Inputs: 
1.	Image: ( type = tensor )
This is given by the user as their only input. Its processed by an image classifier, and based on that classification a relevant query prompt is generated and sent to the a RAG model.
2.	Training Data: ( type = dict(str) )
The RAG model receives data from the database based on its prompt and its lookup request. It then trains on this data.
 
-	Outputs:
1.	Database Lookup: ( type = string )
Requests data from the database to train on based on its prompt.
2.	Description of User Image: ( type = string )
Ideally the description of the users item in the most attractive style to a potential buyer.
 
![project_graph](https://github.com/rfeinberg3/ebay_Auto_Seller/assets/95943957/a0a61ac8-52f8-4a5b-b588-9d5fa1e9c21d)



