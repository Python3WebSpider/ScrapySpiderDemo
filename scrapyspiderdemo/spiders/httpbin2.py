import scrapy
from scrapy import Request


class HttpbinSpider(scrapy.Spider):
    name = 'httpbin2'
    allowed_domains = ['httpbin.org']
    start_url = 'https://httpbin.org/get'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }
    cookies = {'name': 'germey', 'age': '26'}
    
    def start_requests(self):
        for offset in range(5):
            url = self.start_url + f'?offset={offset}'
            yield Request(url, headers=self.headers,
                          cookies=self.cookies,
                          callback=self.parse_response,
                          meta={'offset': offset})
    
    def parse_response(self, response):
        print('url', response.url)
        print('request', response.request)
        print('status', response.status)
        print('headers', response.headers)
        print('text', response.text)
        print('meta', response.meta)