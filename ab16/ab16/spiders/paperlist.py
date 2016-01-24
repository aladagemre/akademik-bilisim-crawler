# -*- coding: utf-8 -*-
import scrapy
from ..items import PaperItem

class PaperlistSpider(scrapy.Spider):
    name = "paperlist"
    allowed_domains = ["ab.org.tr"]
    start_urls = (
        'http://ab.org.tr/ab16/kabul.html',
    )

    def parse(self, response):
        for row in response.xpath('//table/tr')[1:]:
            cols = row.xpath('td')
            pid = cols[0].xpath('p/text()').extract()[0]
            title = cols[1].xpath('p/a/text()').extract()[0]
            details = cols[1].xpath('p/a/@href').extract()[0]
            authors = ", ".join(
                        map(lambda x:x.strip(),
                            cols[2].xpath('p/text()').extract()
                        )
            )
            url = cols[3].xpath('p/a/@href').extract()
            if url:
                url = url[0]
            else:
                url = ""

            item = PaperItem()
            item['pid'] = pid
            item['title'] = title
            item['details'] = details
            item['authors'] = authors
            item['url'] = url
            yield item
