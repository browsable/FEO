from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.PhantomJS(executable_path='/Users/browsable/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs')
driver.command_executor._commands['executePhantomScript'] = ('POST', '/session/$sessionId/phantom/execute')
driver.get("http://www.naver.com")
imgs = driver.find_elements('img')
for img in imgs:
    print(imgs)
print(len(imgs))
driver.quit()

#driver.close()