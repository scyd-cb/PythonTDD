from selenium import webdriver

try: 
    browser = webdriver.Firefox()
    browser.get('http://localhost:8000')
except Exception as ex:
    print("error: %s",ex)
else: 
    print('ok')
finally:
    assert 'To-Do' in browser.title, "Browser title is:" + browser.title



