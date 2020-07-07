import requests
from bs4 import BeautifulSoup

def scrapeContent(url):
    print(url)
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
        
    bikes = soup.find_all('div', class_='productTile__productSummary')
    
    filteredContent = []
    for bike in bikes:
        #print(bike)
        name = bike.find('div', class_='productTile__productName').text.strip()
        #print(name)
        regularPrice = bike.find('div', class_='productTile__priceOriginal').text.strip()[4:-5]
        salePrice = bike.find('div', class_='productTile__priceSale').text.strip()[:-5]
        url = "https://www.canyon.com" + bike.find("meta", itemprop="url").get("content")

        if None in (name, regularPrice, salePrice, url):
            continue
        
        filteredContent.append([name, regularPrice, salePrice, url])
    # print(filteredContent)
    return filteredContent
