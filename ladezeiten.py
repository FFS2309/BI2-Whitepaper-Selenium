import csv
import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.headless = True

results = []

with open('top-25-websites.csv', newline='') as websiteList:
    dialect = csv.Sniffer().sniff(websiteList.read(1024))
    websiteList.seek(0)
    reader = csv.reader(websiteList, dialect)
    startTime = time.time()
    for row in reader:
        browser = webdriver.Chrome(options=options)
        browser.get("https://" + row[1])
        navigationStart = browser.execute_script('return window.performance.timing.navigationStart')
        responseStart = browser.execute_script('return window.performance.timing.responseStart')
        domComplete = browser.execute_script('return window.performance.timing.domComplete')
        backendTime = responseStart-navigationStart
        frontendTime = domComplete-responseStart
        totalTime = backendTime + frontendTime
        nameInDomain = row[1].split('.')[0]
        nameInTitle = nameInDomain.upper() in browser.title.upper()
        titlePercentage = len(nameInDomain)*100 / len(browser.title) if nameInTitle else 0
        results.append((row[1], backendTime, frontendTime, totalTime, nameInTitle, titlePercentage))
        browser.quit()
    endTime = time.time()
    print("Execution time: %ss" % (endTime-startTime))
for row in results:
    print(row)
