from selenium import webdriver

browser = webdriver.Chrome()
browser.get("https://google.com/search?q=test")
browser.implicitly_wait(10)

browser.find_element_by_xpath("//*[text()='Ich stimme zu']").click()

results = browser.find_elements_by_xpath('//a/h3')

for result in results:
    print(result.text)

browser.quit()