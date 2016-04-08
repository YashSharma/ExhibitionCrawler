import scrapy
import urllib
from exhibitor.items import ExhibitorItem
import requests
from bs4 import BeautifulSoup

class ExhibitorSpider(scrapy.Spider):
    name = 'exhibitor'
    allowed_domains = ['http://s15.a2zinc.net/clients/adtech/adtechny2015/public/']
    start_urls = [
        "http://s15.a2zinc.net/clients/adtech/adtechny2015/public/EventMap.aspx?shmode=E"
    ]
    
#    def spider(max_pages):
#    page = 1
#    while page <= max_pages:
#        url = 'https://www.quora.com/Aman-Srivastava-20/followers'
#        source_code = requests.get(url)
#        plain_text = source_code.text
#        soup = BeautifulSoup(plain_text)
#        for link in soup.findAll('img', {'class': 'profile_photo_img'}):
#            href = link.get('src')
#            print (href)
#            download_web_image(href)
#        page+=1
            
    def parse(self, response):
        domain = 'http://s15.a2zinc.net/clients/adtech/adtechny2015/public/'
        for sel in response.xpath('//a[@class="exhibitorName"]'):
            item = ExhibitorItem()
            ext = sel.xpath('@href').extract()
            follow_up_link = domain + str(ext[0])
            source_code = requests.get(follow_up_link)
            plain_text = source_code.text
            soup = BeautifulSoup(plain_text)
            item['company'] = 'NA'
            item['location'] = 'NA'
            item['country'] = 'NA'
            item['website'] = 'NA'
            item['description'] = 'NA'
            if soup.findAll('h1'):
                item['company'] = str(soup.findAll('h1')[0].get_text())
            if (soup.findAll('span', {'class': 'BoothContactCity'})):
                if soup.findAll('span', {'class': 'BoothContactState'}):
                    item['location'] = str(soup.findAll('span', {'class': 'BoothContactCity'})[0].get_text().split(',')[0]) + ', ' + str(soup.findAll('span', {'class': 'BoothContactState'})[0].get_text().split()[0])
            if soup.findAll('span', {'class': 'BoothContactCountry'}):
                item['country'] = str(soup.findAll('span', {'class': 'BoothContactCountry'})[0].get_text().split(',')[0])
            if soup.findAll('span', {'class': 'BoothContactUrl'}):
                item['website'] = str(soup.findAll('span', {'class': 'BoothContactUrl'})[0].get_text().split(',')[0])
            descrip = ''
            for para in soup.findAll('p'):
                #item['description'] = item['description'] + str(para.get_text())
                descrip = descrip + para.get_text()
            item['description'] = descrip
            yield item