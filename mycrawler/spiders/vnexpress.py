import scrapy

class VnexpressSpider(scrapy.Spider):
    name = "vnexpress"
    allowed_domains = ["vnexpress.net"]
    start_urls = ["https://vnexpress.net/"]

    def parse(self, response):
        # Lấy danh sách tiêu đề bài báo
        for article in response.css("h3.title-news a::text"):
            yield {"title": article.get().strip()}

        # Lấy link để crawl tiếp (ví dụ: trang chuyên mục)
        for href in response.css("a::attr(href)").getall():
            if href.startswith("https://vnexpress.net/"):
                yield response.follow(href, callback=self.parse)
