import scrapy
from ..items import MyprojectItem

class ProductsSpider(scrapy.Spider):
    name = 'products'
    allowed_domains = ['kikomilano.com.tr/']
    #page_number = 2
    start_urls = ['https://www.kikomilano.com.tr/makyaj/?page=1',
                  'https://www.kikomilano.com.tr/makyaj/?page=2']
    
    #response.css('div.list-Result span::text').get()
    
    for i in range(3,80):
        start_urls.append(f'https://www.kikomilano.com.tr/makyaj/?page={i}')
    
    for i in range(0,9):    
        start_urls.append(f'https://www.kikomilano.com.tr/cilt-bakimi/?page={i}')
        
    for i in range(0,9):    
        start_urls.append(f'https://www.kikomilano.com.tr/aksesuarlar/?page={i}')
    
    def parse(self, response):
        
        items = MyprojectItem()
        
        all_div_response = response.css('div.productDe')
        
        for response in all_div_response:
            name = response.css('div.addButtons pz-button::attr(data-name)').extract()
            data_product = response.css('div.addButtons pz-button::attr(data-product)').extract()
            action = response.css('div.addButtons pz-button::attr(action)').extract()
            service = response.css('div.addButtons pz-button::text').extract()
            link = response.css('a::attr(data-url)').extract()
            
            items['name'] = name
            items['data_product'] = data_product
            items['action'] = action
            items['service'] = service
            items['link'] = link
            
            yield items
        
        """    
        next_page = 'https://www.kikomilano.com.tr/makyaj/?page='+str(ProductsSpider.page_number)
        if ProductsSpider.page_number < 3:
            ProductsSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
        """
