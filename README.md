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
Download ZIP 放到 d:/Spider 文件夹

cd Scrapping-INC500/INC500LIST/
```
### Install Dependencies:
> We will compile and reinstall Python3

```
pip3 install -r requirment.txt
```

### Run Scrapper:
```sudo bash start.sh```

### Checkout Result:
Results are placed inside the `output` folder.




