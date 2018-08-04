# -*- coding: utf-8 -*-
import scrapy


class StatsSpider(scrapy.Spider):
    name = 'Stats'
    start_urls = ['https://www.appbrain.com/stats/stats-index']

    def parse(self, response):
        for section in response.css('div.col-md-6'):
            section_title = section.css('h2::text')
            sub_sections = response.css('div.info-box').extract()
            for sub_section in sub_sections:
                yield {
                    'subtitles': section.css('div.info-box::text').extract_first(),
                    'numbers': section.css('span.number::text').extract_first(),
                }
