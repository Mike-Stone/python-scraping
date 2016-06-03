from selenium import webdriver
import time
#用PlantomJS浏览器加载
driver = webdriver.PhantomJS(executable_path='')
driver.get("http://pythonscraping.com/pages/javascript/ajaxDemo.html")
time.sleep(3)
#静等三秒，期望JS已经加载完成
print(driver.find_element_by_id("content").text)
driver.close()
