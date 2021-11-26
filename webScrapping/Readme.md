# WebScraping

* pip install requests
* pip install bs4

basics - link: https://pythonizing.github.io/data/example.html

Request Headers to Enable Web Scraping
Important note:

r = requests.get("https://pythonizing.github.io/data/example.html", headers={'User-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0'})

Explanation:
As you can see in the new code, we are changing the domain name from pythonhow.com to pythonizing.github.io and we are also adding a headers argument. We are changing the domain because the new domain now contains the data we want to scrape. And we are adding request headers because that allows the Python script to impersonate a web browser. Of course, you don't need the header argument for every website, but i's good to have it just in case.