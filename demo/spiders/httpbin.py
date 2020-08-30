import scrapy
from scrapy.http import JsonRequest, FormRequest


class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    start_url = 'http://httpbin.org/post'
    data = {'name': 'germey', 'age': '26'}
    
    def start_requests(self):
        yield FormRequest(self.start_url,
                          callback=self.parse_response,
                          formdata=self.data)
        yield JsonRequest(self.start_url,
                          callback=self.parse_response,
                          data=self.data)
    
    def parse_response(self, response):
        print('text', response.text)
