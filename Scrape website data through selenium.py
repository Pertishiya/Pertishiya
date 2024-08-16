from selenium import webdriver
from selenium.webdriver.common.by import By

#Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# driver.get("https://www.amazon.in/BROTHERS-Silent-Ticking-Operated-Decorative/dp/B0BN25CM3K/ref=sr_1_23_sspa?crid=26BDC9B7W7Z9A&dib=eyJ2IjoiMSJ9.ObUoZYKRiZ324eObexNe9YivLvlItXTkwoR31sv_7U0yzQKqnelyKYSsH2PcRbAA2YPfSADvs38GnRyXOPk3bGvn9aBvpBn9A6EsAKJ2c9t15hNq2qPektkMwPZGZUKExXwUgSztbVDEYtdPJ462gmS_kKPu7Bs5nyAiguzcYKK3gHimqHHXbXg6xTzUJzgv0HdScTf_EXhWC2z5q9pA564fK1sv3D1FuJe9HQ4aBLj1p_sXnEKxpL8xjgC4aS874nGaQ_W0ihGxciQQo3wI6Xe5oNFRQG8l7fR4dyufKKY.Ye2uuGu_B2iVreuJ3ke44CWjDLr6ePn_l7wCJ88ybRE&dib_tag=se&keywords=custom+wall+clock&qid=1723568274&sprefix=customise+wall+clock%2Caps%2C196&sr=8-23-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9tdGY&psc=1")

#By.CLASS_NAME
price = driver.find_element(By.CLASS_NAME, "a-price-whole")
# print(f"The price is {price.text}")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))

#By.ID
button = driver.find_element(By.ID, value = "submit")
# print(button.size)

#By.CSS_SELECTOR - # for id and . for class
documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)

#By.XPath
#click F12 -> Inspect -> Right click -> Copy -> Copy XPath -> Paste here
bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

tier_1 = driver.find_elements(By.CLASS_NAME, value="tier-1")


#Print event dates from python.org
event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

events = {}

for n in range(0,len(event_times)):
    events[n]={
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

print(events)

# for time in event_times:
#     print(time.text)

# for name in event_names:
#     print(name.text)

    

#driver.close() #close single tab
driver.quit() #close entire browswe