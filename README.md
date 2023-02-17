# craw data

from `itviec.com`

```shell
/home/dat/setupfiles/anaconda3/envs/py310/bin/scrapy startproject itviec
cd itviec
/home/dat/setupfiles/anaconda3/envs/py310/bin/scrapy genspider jobs "https://itviec.com/it-jobs"
```

```shell
/home/dat/setupfiles/anaconda3/envs/py310/bin/scrapy crawl itviec
```