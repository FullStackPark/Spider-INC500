# INC500 Spider (世界5000强公司爬虫)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)
[![Build Status](https://travis-ci.org/{ORG-or-USERNAME}/{REPO-NAME}.png?branch=master)](https://travis-ci.org/{ORG-or-USERNAME}/{REPO-NAME})

> Target(目标): https://www.inc.com/inc5000/list/2017

INC500 Spider Scrap all the company detail informations from the target then save it to an excel file, so that you can analysis these information across the INC500 companies (actually 5000 companies will be scrapped)。

## Scrapped Title:
* CompanyID
* Ranking
* CompanyName
* Industry
* Growth
* Revenue
* City
* StateAbbr
* StateName
* YearsOnINCList
* Partner
* BriefDescription
* Description
* Leadership
* Founded
* ThreeYearGrowth
* Employees
* Website
* Location
* WikipediaPage
* WikipediaURL

## Getting Started
### Clone Repository
```
git clone https://github.com/XetRAHF/Scrapping-INC500.git
cd Scrapping-INC500/INC500LIST/
```
### Install Dependencies:
> We will compile and reinstall Python3.6, since the python apt repo doen't work well with Scrapy

```
sudo bash dependencies.sh
pip3.6 install -r requirment.txt
```

### Run Scrapper:
```sudo bash start.sh```

### Checkout Result:
Results are placed inside the `output` folder.

## Compatibility

Tested on Ubuntu-16.04 x64.

## Screenshots


## Contact

-  Mailing me for support: ```zerqqr1@iydhp.com```
-  Connect me on wechat: ```ITXSG_HF```

## Acknowledgments
- My Partner - ZePing Bai - Technology Support - Connect him on QQ by QR:
![ZePing Bai](https://raw.githubusercontent.com/XetRAHF/Scrapping-INC500/master/IMGS/zepingbai.jpg)
- Join our QQ technology forum: ```560956108```

## Computer Requirment
> This is a high-requirment project, you can not run it on a 10-years old Linux Computer with poor internet connection
> You may need 12 hours to run the project.
- CPU: At least 6 Cores, 10+ Cores are recommended.
- Memory: At least 8GB, 16GB are recommended.
> Cloud Server is Highly-Recommended.
