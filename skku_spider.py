import scrapy


class SkkuSpiderSpider(scrapy.Spider):
    name = "skku_spider"
    allowed_domains = ["forensic.skku.edu"]
    start_urls = ["https://forensic.skku.edu/forensic/community/grad_notice.do"]

    def parse(self, response):
        articles = []
        for article in response.css("ul.board-list-wrap > li"):
            data = {
                "title": article.css("dl > dt a::text").get().replace("\n","").replace("\t", "").replace("  ", ""),
                "link": article.css("dl > dt a::attr(href)").get()
                #"title": article.css("dt.board-list-content-title > a").get(),
                #"link": article.css("dt.board-list-content-title > href").get()
            }
            articles.append(data)
        print(articles)

        ## 다음페이지로 넘어가는 코드 ##
        for page in response.css('ul.paging-wrap li'):
            link = page.css('a::attr(href)').get()
            link_text = page.css('a::text').get()
            if link_text:
                link_text = link_text.strip()
            if link_text and link_text.isdigit() and int(link_text) <= 3:
                yield { 'page_number': link_text, 'link': link}
                yield response.follow(link, self.parse)


#jwxe_main_content > div > div > div.board-name-list.board-wrap > ul > li:nth-child(2) > dl > dt > a

