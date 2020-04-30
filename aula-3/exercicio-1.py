from selenium.webdriver import Chrome
import time

browser = Chrome()
url = 'https://curso-python-selenium.netlify.app/exercicio_01.html'
browser.get(url)

time.sleep(3)

tags_p = browser.find_elements_by_tag_name('p')

elements = {'h1': []}

for p in tags_p:
    elements['h1'].append({p.get_attribute('atributo'): p.text})

print(elements)

browser.quit()
