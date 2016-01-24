# -*- coding: utf-8 -*-
import scrapy

from ..items import SessionItem

class SessionsSpider(scrapy.Spider):
    name = "sessions"
    allowed_domains = ["ab.org.tr"]
    start_urls = (
        'file:///Users/research/tmp/ab16/ab16/ab16/cerceve.html',
    )

    def parse(self, response):
        trs = response.xpath("//tr")
        ths = trs[0].xpath('th/text()').extract()
        salloon_names = map(lambda x:x.strip(), ths[1:])
        current_date = ths[0]

        for tr in trs[1:]:
            tds = tr.xpath('td/text()').extract()
            if "/" in tds[0]:
                current_date = tds[0]
                continue

            if len(tds) == 2:
                # All sallons
                continue

            time = tds[0].replace("_", "-")
            cells = tds[1:]
            for i, cell in enumerate(cells):
                if ":" not in cell and "(" not in cell and "." not in cell:
                    topic = ""
                    numlist = cell
                else:
                    cell = cell.replace(" (", ": ").replace(")", "").replace(".",":")
                    topic, numlist = cell.split(":")


                item = SessionItem()
                item['salloon'] = salloon_names[i]
                item['date'] = current_date.strip()
                item['time'] = time.strip()
                item['topic'] = topic.strip()
                item['ids'] = map(lambda x: x.strip(), numlist.strip().split(","))
                yield item
