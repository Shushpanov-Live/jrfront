from scrapy import Request
from parser.parser.items import PostItem, CategoryItem
from asgiref.sync import sync_to_async, async_to_sync
from article.models import Post, Category

import re
import scrapy

class ConsultantSpider(scrapy.Spider):
    name = "consultant"
    allowed_domains = ['consultant.ru']
   
    @sync_to_async
    def pipline(self, item):
        category = Category.objects.get_or_create(title=item['category_title'])
        post = Post.objects.create(title=item['title'], content=item['content'], category_id=category[0].id)
        print('post:',post )
    
    def start_requests(self):
        urls = [
            'https://www.consultant.ru/document/cons_doc_LAW_5142/',
            'https://www.consultant.ru/document/cons_doc_LAW_51057/',
            'https://www.consultant.ru/document/cons_doc_LAW_19671/',
            'https://www.consultant.ru/document/cons_doc_LAW_34683/',
            'https://www.consultant.ru/document/cons_doc_LAW_10699/',
            'https://www.consultant.ru/document/cons_doc_LAW_34661/',
            'https://www.consultant.ru/document/cons_doc_LAW_19702/',
            'https://www.consultant.ru/document/cons_doc_LAW_215315/',
            'https://www.consultant.ru/document/cons_doc_LAW_37800/',
            'https://www.consultant.ru/document/cons_doc_LAW_33773/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse_codex)
   
    def parse_codex(self, response):
        articles = response.css('html body div.content.document-page section.document-page__main.width-container.page-fields div.external-block div.external-block__content div.document-page__toc ul>li')
        for article in articles:
            articleLink = article.css('a::attr(href)').extract()[0]
            yield Request(url=f'https://www.consultant.ru{articleLink}', callback=self.parse_article)

    def parse_article(self, response):
        item = PostItem()
        t = response.css('.document-page__title-link a::text').get()
        cat=re.split('Российской', t)
        text = response.css('html body div.content.document-page section.document-page__main.width-container.page-fields div.external-block div.external-block__content div.document-page__content.document-page_left-padding p::text')
        item['category_title'] = cat[0][1:-1]
        item['title'] = text.extract()[0]
        item['content'] = text.extract()[1]
        return self.pipline(item)

    

