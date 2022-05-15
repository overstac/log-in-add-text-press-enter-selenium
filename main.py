from selenium import webdriver
def get_driver():
  #face cautarea mai usoara
  options= webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("exculdeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-featureas=AutomationControlled")
  
  driver= webdriver.Chromei(options)
  driver.get("https://automated.pythonanywhere.com/")
  return driver

def main ():
  driver= get_driver()
  element = driver.find_element_by_xpath("/html/body/div[1]/div/h1[1]/text()")
  return element

print(main())