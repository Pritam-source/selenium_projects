from selenium import webdriver
driver = webdriver.Chrome()

driver.get('https://www.lazada.com.ph/shop-laptops/')

xpath='//*[@data-qa-locator="product-item"]//a[text()]'
link_elements = driver.find_elements_by_xpath(xpath)
links=[]
for link_el in link_elements:
    href=link_el.get_attribute("href")
    print(href)
    links.append(href)

driver.quit()
print(len(links))