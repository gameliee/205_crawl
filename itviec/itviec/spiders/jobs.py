from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.dupefilters import RFPDupeFilter

class JobsSpider(CrawlSpider):
    name = "jobs"
    allowed_domains = ["itviec.com"]
    start_urls = ["http://itviec.com/it-jobs"]

    custom_settings={
        'FEED_URI': "all_%(time)s.marshal",
        'FEED_FORMAT': 'marshal',
        'DUPEFILTER_CLASS': RFPDupeFilter,
        'AUTOTHROTTLE_ENABLED': True
    }

    rules = (
        Rule(LinkExtractor(restrict_xpaths="//div[@class='job']", tags=('div'), attrs=('data-search--job-selection-job-url-value')), follow=True),
        Rule(LinkExtractor(restrict_xpaths="//div[@class='search-page__jobs-pagination']//li//a[@rel='next']", tags=('a'), attrs=('href')), follow=True),
        Rule(LinkExtractor(allow=r"/it-jobs/.*\?lab_feature=preview_jd_page$"), callback='parse_single_job')
    )

    def parse_single_job(self, response):
        """parse job details"""
        print(f"huhuhu im here at {response.url}")
        yield {
            'url': response.url,
            'job detail header': response.xpath("//div[@class='job-details__header']").get(),
            'top reason to join us': response.xpath("//div[@class='job-details__top-reason-to-join-us']").get(),
            'job detail overview': response.xpath("//div[@class='job-details__overview']").get(),
            'second titles': response.xpath("//div[@class='job-details__second-title']").get(),
            'paragraphs': response.xpath("//div[@class='job-details__paragraph']").get(),
            'employer': response.xpath("//div[@class='jd-page__employer-overview']").get(),
        }