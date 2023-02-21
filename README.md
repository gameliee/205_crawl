# craw data

from `itviec.com`

## start project

```shell
/home/dat/setupfiles/anaconda3/envs/py310/bin/scrapy startproject itviec
cd itviec
/home/dat/setupfiles/anaconda3/envs/py310/bin/scrapy genspider jobs "https://itviec.com/it-jobs"
```

```shell
cd itviec
/home/dat/setupfiles/anaconda3/envs/py310/bin/scrapy crawl jobs
```

data will then save in `.marshal` format, read it by

```shell
python read_marshal.py
```

```shell
/home/dat/setupfiles/anaconda3/envs/py310/bin/scrapy parse --spider=jobs -c parse_single_job -d 2 'https://itviec.com/it-jobs/remote-senior-devops-engineers-aws-101-digital-0110?lab_feature=preview_jd_page'
```

## note

single job parser

| name | xpath | note |
|------|-------|------|
|job detail header |"//div[@class='job-details__header']"||
|top reason to join us |"//div[@class='job-details__top-reason-to-join-us']"||
|job detail overview |  "//div[@class='job-details__overview']" ||
|second title | "//div[@class='job-details__second-title']"| may have many |
|paragraph | "//div[@class='job-details__paragraph']"| may have many |
| employer | "//div[@class='jd-page__employer-overview']" ||

```python
'job-details__title': response.xpath("//h1[@class='job-details__title']/text()").get(),
'job-details__save-job': response.xpath("//div[@class='job-details__save-job']/@data-jobs--save-data-layer-value").get(),
# 'job-details__header': response.xpath("//div[@class='job-details__header']").get(),
'top reason to join us': response.xpath("//div[@class='job-details__top-reason-to-join-us']").get(),
'job detail overview': response.xpath("//div[@class='job-details__overview']").get(),
'second titles': response.xpath("//div[@class='job-details__second-title']").get(),
'paragraphs': response.xpath("//div[@class='job-details__paragraph']").get(),
'employer': response.xpath("//div[@class='jd-page__employer-overview']").get(),
'employer-long-overview__short-desc': response.xpath("//div[@class='employer-long-overview__short-desc']/text()").get(),
```