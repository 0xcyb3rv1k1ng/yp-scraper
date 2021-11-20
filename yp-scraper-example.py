import requests
import csv
from bs4 import BeautifulSoup

placeHolder = []

urls = ["https://www.yellowpages.com/search?search_terms=<STORE NAME>&geo_location_terms=<STATE ABBREVIATION>&page={}".format(page) for page in range(1,2)]
for url in urls:
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "lxml")

    def get_text(item,path): return item.select_one(path).text if item.select_one(path) else ""

    for item in soup.select(".info"):
      d = {}
      d['name'] = get_text(item,"a.business-name span")
      d['streetAddress'] = get_text(item,".street-address")
      d['addressLocality'] = get_text(item,".locality")
      d['addressRegion'] = get_text(item,".locality + span")
      d['postalCode'] = get_text(item,".locality + span + span")
      d['phone'] = get_text(item,".phones")
      placeHolder.append(d)

with open("<FILENAME.csv","w",newline="") as infile:
  writer = csv.DictWriter(infile,['name','streetAddress','addressLocality','addressRegion','postalCode','phone',])
  writer.writeheader()
  for elem in placeHolder:
    writer.writerow(elem)

/* These are the ones that need to be changed */
// Examples:
// urls = ["https://www.yellowpages.com/search?search_terms=bi-lo&geo_location_terms=GA&page={}".format(page) for page in range(1,2)]
// with open("bi-lo-ga.csv","w",newline="") as infile:
