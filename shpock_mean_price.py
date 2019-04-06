# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6  2019

@author: GerH
"""

from selenium import webdriver
from time import sleep


#Change these values accordingly
searchUrls = ["https://www.shpock.com/de-at/search?q=iphone%208", 
              "https://www.shpock.com/de-at/search?q=iphone%207", 
              "https://www.shpock.com/de-at/search?q=iphone%206", 
              "https://www.shpock.com/de-at/search?q=iphone%205", 
              "https://www.shpock.com/de-at/search?q=iphone%204", 
              "https://www.shpock.com/de-at/search?q=iphone%203", 
              "https://www.shpock.com/de-at/search?q=samsung%20galaxy%20S8", 
              "https://www.shpock.com/de-at/search?q=samsung%20galaxy%20S7", 
              "https://www.shpock.com/de-at/search?q=samsung%20galaxy%20S6", 
              "https://www.shpock.com/de-at/search?q=samsung%20galaxy%20S5", 
              "https://www.shpock.com/de-at/search?q=samsung%20galaxy%20S4", 
              "https://www.shpock.com/de-at/search?q=samsung%20galaxy%20S3"]
#Strings you don't want among your results (in lowercase)
excludeStrings = ["samsung",
                  "samsung",
                  "samsung",
                  "samsung",
                  "samsung",
                  "samsung",
                  "iphone",
                  "iphone",
                  "iphone",
                  "iphone",
                  "iphone",
                  "iphone"]
minPrice = 60.0
maxPrice = 1000.0
scrollAmounts = 10
currencySign = "€"
wait = .5


#Round a float number up
def roundUp(number):
    return int(( number * 100 ) + 0.5) / float(100)

#Calculate mean value
def mean(numbers):
    return float(sum(numbers)) / max(len(numbers), 1)


#Perform searches for all URLs
searchNumber = 0
for searchUrl in searchUrls:
    #Go to search URL
    driver = webdriver.Firefox()
    driver.get(searchUrl)
    
    #Click cookie warning away
    driver.find_element_by_class_name("Button-sc-1mt1e5c-0.OwBcJ").click()
    sleep(wait)
    #Click "show more" button
    driver.find_element_by_class_name("Button-sc-1mt1e5c-0.kUjfGx").click()
    sleep(wait)
    
    #scroll down to show more products
    for i in range(scrollAmounts):
        driver.execute_script("window.scrollTo(0, " + str(2000*i) + ")")
        sleep(wait)
    
    #Don't change these values
    sumPrices = 0.0
    prices = []
    
    #Find all prices, add them to the sum
    priceElems = driver.find_elements_by_class_name("StyledAssets__Title-sc-1ojzb7j-0.ItemCard__Price-cy8zy7-0.gXQMNR")
    titleElems = driver.find_elements_by_class_name("StyledAssets__Title-sc-1ojzb7j-0.iFPzQi")

    for i in range(len(priceElems)):
        if(currencySign in priceElems[i].text):
            priceFloat = float(priceElems[i].text.split('€')[1].replace(".","").replace(",","."))
            if(priceFloat > minPrice and priceFloat < maxPrice):
                #Make sure that an excluded String isn't contained in the title
                excludeString = excludeStrings[searchNumber]
                currentTitle = titleElems[i].text.lower()
                if(excludeString not in currentTitle):
                    prices.append(priceFloat)
                    sumPrices += priceFloat
    
    print("\n\n\nSearch finished! \nURL: "+searchUrl+"\n\nNumber of entries found: " + str(len(prices)))
    
    #output Sum
    sumPricesRounded = roundUp(sumPrices)
    print("Sum:        "+ currencySign + " " +str(sumPricesRounded))
    
    #calculate and output Mean
    meanPriceRounded = roundUp(mean(prices))
    print("Mean price: " + currencySign + " " + str(meanPriceRounded))
    
    searchNumber+=1
    driver.close()