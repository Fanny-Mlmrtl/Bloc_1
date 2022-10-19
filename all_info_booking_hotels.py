import os 
import logging
import scrapy
from scrapy.crawler import CrawlerProcess

my_file = open("folder/url_booking_hotels.txt", "r")
content = my_file.read()
content_list = content.split("\n")[:-1]

class booking_spider(scrapy.Spider):
    # Name of your spider
    name = "booking"

    # Url to start your spider from 
    start_urls = content_list

    def parse(self, response):
        return {
            "address": response.xpath('//*[@id="showMap2"]/span[1]/text()').get(),
            "hotel name": response.xpath('//*[@id="hp_hotel_name"]/div/div/h2/text()').get(),
            "score": response.xpath('//*[@id="js--hp-gallery-scorecard"]/a/div/div/div/div/div[1]/text()').get(),
            "url": response.url,
            "coordinates": response.xpath('//*[@id="hotel_address"]').attrib['data-atlas-latlng'],
            "description": response.xpath('//*[@id="property_description_content"]/p/text()').getall(),
        }

# Name of the file where the results will be saved
filename = "all_info_booking_hotels.json"

# If file already exists, delete it before crawling (because Scrapy will 
# concatenate the last and new results otherwise)
if filename in os.listdir('folder/'):
        os.remove('folder/' + filename)


process = CrawlerProcess(settings = {
    'USER_AGENT': 'Chrome/106.0.5249.62',
    'LOG_LEVEL': logging.INFO,
    "FEEDS": {
        'folder/' + filename : {"format": "json"},
    },
})

# Start the crawling using the spider you defined above
process.crawl(booking_spider)
process.start()