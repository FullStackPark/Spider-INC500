#!/usr/bin/env bash
sudo mkdir temp
sudo mkdir temp/html
sudo mkdir temp/INC500_company_details
sudo mkdir temp/wikipedia_list
sudo mkdir output
sudo mkdir output/wikipedia_search

sudo docker run -p 8050:8050 -d scrapinghub/splash
sudo scrapy crawl INC500_1
sudo scrapy crawl INC500_2
sudo python3.6 spider/INC500_3.py
sudo python3.6 spider/INC500_3.py

sudo mv temp/INC500_4.xlsx output/companies.xlsx
sudo mv temp/html/wikipedia_list/* output/wikipedia_search
sudo rm -rf temp

echo You can now Find the excel output and wikipedia search pages inside the output directory