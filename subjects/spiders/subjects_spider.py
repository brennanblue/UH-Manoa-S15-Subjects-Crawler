import scrapy
from subjects.items import SubjectsItem

class SubjectsSpider(scrapy.Spider):
	name = "subjects"
	allowed_domains = ["scsis.hawaii.edu/"]
	start_urls = [
		"https://www.sis.hawaii.edu/uhdad/avail.classes?i=MAN&t=201530"
	]

	def parse(self, response):
		for sel in response.xpath('//ul/li'):
			item = SubjectsItem()
			item['subjectCode'] = sel.xpath('a/text()').re('\(([^)]*)\)')
			item['name'] = sel.xpath('a/text()').re('(.*?)\s*\(')
			yield item