from selenium.webdriver import Chrome
import time 

browser = Chrome()
url = 'https://curso-python-selenium.netlify.app/exercicio_02.html'
browser.get(url)

time.sleep(3)

button = browser.find_element_by_tag_name('a')
tags_p = browser.find_elements_by_tag_name('p')
get_value = lambda: int(tags_p[-1].text[-2:])
value = get_value()

while True:
    button.click()
    tags_p = browser.find_elements_by_tag_name('p')
    if get_value() == value:
        print(tags_p[-1].text)
        break

browser.quit()
