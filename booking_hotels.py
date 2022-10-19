import os
import logging
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy import Request
from urllib.parse import urlencode
import urllib.parse

city_list = ["Mont Saint Michel",
"St Malo",
"Bayeux",
"Le Havre",
"Rouen",
"Paris",
"Amiens",
"Lille",
"Strasbourg",
"Chateau du Haut Koenigsbourg",
"Colmar",
"Eguisheim",
"Besancon",
"Dijon",
"Annecy",
"Grenoble",
"Lyon",
"Gorges du Verdon",
"Bormes les Mimosas",
"Cassis",
"Marseille",
"Aix en Provence",
"Avignon",
"Uzes",
"Nimes",
"Aigues Mortes",
"Saintes Maries de la mer",
"Collioure",
"Carcassonne",
"Ariege",
"Toulouse",
"Montauban",
"Biarritz",
"Bayonne",
"La Rochelle"]


class booking_spider(scrapy.Spider):
    # Name of your spider
    name = "booking"

    # These are the urls that we will start scraping
    start_urls = ['https://www.booking.com/searchresults.html?ss=' + urllib.parse.quote(city) for city in city_list]


        # Callback used after login
    def parse(self, response):
        names = response.xpath('//*[@id="search_results_table"]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div[1]/div/div[1]/div/h3/a/div[1]/text()') 
        urls = response.xpath('//*[@id="search_results_table"]/div[2]/div/div/div/div[3]/div/div[1]/div[2]/div/div[1]/div[1]/div/div[1]/div/h3/a')
        scores = response.xpath('//*[@id="search_results_table"]/div[2]/div/div/div/div/div/div[1]/div[2]/div/div/div[2]/div[1]/a/span/div/div[1]/text()')
        
        for name, url, score in zip(names,urls, scores):
            yield {
                'city': urllib.parse.unquote(response.url[response.url.find('ss=')+len('ss='):]),
                'hotel name': name.get(),
                'url': url.attrib["href"][:url.attrib["href"].find('?')],
                'score': score.get()
            }


# Name of the file where the results will be saved
filename = "booking_hotels.json"

#If file already exists, delete it before crawling (because Scrapy will 
#concatenate the last and new results otherwise)
if filename in os.listdir('folder/'):
        os.remove('folder/' + filename)

process = CrawlerProcess(settings = {
    'USER_AGENT': 'Chrome/106.0.5249.62',
    'LOG_LEVEL': logging.INFO,
    "FEEDS": {
        'folder/' + filename : {"format": "json"},
    }
})

process.crawl(booking_spider)
process.start()
