#pip install lxml
#pip install requests
from lxml import html
import requests
page = requests.get('https://www.ffxiah.com/item/4059/pluton')
tree = html.fromstring(page.content)
print ('fromstring:', tree)
# https://www.w3schools.com/xml/xpath_syntax.asp
lastPrice = tree.xpath('//span[@id="sales-last"]')
print ('Last Sell Price: ', lastPrice)
salesPerDay = tree.xpath('//span[@id="sales-per-day"]')
salesPerDayNode = salesPerDay[0]
salesPerDay2 = tree.xpath('//span[@id="sales-per-day"]/title')
salesPerDay3 = tree.xpath('//span[@id="sales-per-day"]/text()')
salesPerDay4 = tree.xpath('//span[@id="sales-per-day"]/..')
salesPerDay5 = tree.xpath('//span[@id="sales-per-day"]/.')
salesPerDay6 = tree.xpath('//span[@id="sales-per-day"][text()]')
# salesPerDay7 = tree.xpath('//span[@id="sales-per-day",text()]')
stackPrice = tree.xpath('//tr[td="Stack Price"]')
medianPrice = tree.xpath('//td[text()="Median"]/following-sibling::td/span/text()')
print ('median price:', medianPrice)
print ('sales per day: ', salesPerDay)
# page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
# tree = html.fromstring(page.content)
# #This will create a list of buyers:
# buyers = tree.xpath('//div[@title="buyer-name"]/text()')
# #This will create a list of prices
# prices = tree.xpath('//span[@class="item-price"]/text()')
# print ('Buyers: ', buyers)
# print ('Prices: ', prices)
