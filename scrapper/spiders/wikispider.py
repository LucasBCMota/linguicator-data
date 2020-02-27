import scrapy

class WikiSpider(scrapy.Spider):
  name = 'wikispider'
  start_urls = ['https://pt.wikipedia.org/wiki/Ci%C3%AAncia']

  def parse(self, response):
    title = response.xpath('//title/text()').get()
    divs = response.xpath('//div/text()')
    spans = response.xpath('//span/text()')
    ps = response.xpath('//p/text()')
    for index,p in enumerate(ps.getall()):
      yield {'index':index, 'text':p }
    