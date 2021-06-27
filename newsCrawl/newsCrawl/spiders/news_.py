import scrapy


class NewsSpider(scrapy.Spider):
    name = "News"

    def start_requests(self):
        urls = [
            'https://news.naver.com/main/ranking/popularDay.nhn?mid=etc&sid1=111',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # for j in range(12):
        div_sels = response.css('#wrap > div:nth-of-type(4) > div:nth-of-type(2) > div')
        for i in range(1):
            newspaper = response.css('div:nth-of-type(' + str(i+1) + ')').get()
            print(newspaper)
        # for div_sel in div_sels:
        #     newspaper = response.css('.rankingnews_box > ul.rankingnews_list > li')
        #     for i in range(5):
        #         url = response.css('li:nth-child(' + str(i+1) + ') > .list_content > a::attr(href)').extract()[0]
        #         title = response.css('li:nth-child(' + str(i+1) + ') > .list_content > a::text').get()
        #         print(title)
        # for i in range(5):
        #     url = response.css('li:nth-child(' + str(i+1) + ') > .list_content > a::attr(href)').extract()[0]
        #     title = response.css('li:nth-child(' + str(i+1) + ') > .list_content > a::text').get()
        #     print(title)
        # for j in div_finding:
        #     news_sels = response.css('ul.rankingnews_list > li')
        #     for i in range(5):
        #         url = response.css('li:nth-child(' + str(i+1) + ') > .list_content > a::attr(href)').extract()[0]
        #         title = response.css('li:nth-child(' + str(i+1) + ') > .list_content > a::text').get()
        #         print(title)
        # for j in div_sels:
        #     news_sels = response.css('.rankingnews_box > ul.rankingnews_list > li')