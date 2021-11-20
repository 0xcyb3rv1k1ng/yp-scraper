# This code is an example of how to use this web scraper to scrape data from the Yellow Pages website. 

Certain parameters must be specified such as 'STORE NAME', 'STATE ABBREVIATION', and 'page' in the 'urls' variable, which should be around line 7.
Additionally, the name of the file, 'FILENAME.csv', which will be exported as a csv file, will need to be changed. This should be around line 24.
This is also demonstrated in the commented out section of code at the bottom.

Here is an example:

// Example:
// urls = ["https://www.yellowpages.com/search?search_terms=bi-lo&geo_location_terms=GA&page={}".format(page) for page in range(1,2)]
// with open("bi-lo-ga.csv","w",newline="") as infile:

In this example, the name of the business being searched is bi-lo. The location being searched is the state of Georgia. 
The page range for the search is pages 1 to 2. The name of the file being exported is 'bi-lo-ga.csv'.

Note: It helps the scraper if the page range is specified. Searching more pages obviously takes more time. 
