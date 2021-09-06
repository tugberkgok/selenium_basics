from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import keyword
import loginInfo
import time
browser = webdriver.Chrome()

browser.get("https://twitter.com/?lang=tr")
time.sleep(2)

alredy = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div[1]/div/div[3]/div[4]/span/span")
alredy.click()

time.sleep(2)

number_or = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div[1]/div/div[3]/a/div/span/span")
number_or.click()

time.sleep(2)

username = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")
password = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")

username.send_keys(loginInfo.username)
password.send_keys(loginInfo.password)

login = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span")
login.click()

time.sleep(3)

searcArea = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input")
searcArea.send_keys("berkironrob")
searcArea.send_keys(Keys.ENTER)
time.sleep(3)

kisiler = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[1]/div[2]/nav/div/div[2]/div/div[3]/a")
kisiler.click()
time.sleep(2)

mehmetemin = browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/section/div/div/div[1]/div/div/div/div[2]/div[1]/div[1]/a/div/div[1]/div[1]/span")
mehmetemin.click()
time.sleep(2)

tweets = set()
elements = browser.find_elements_by_css_selector(".css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0")
for element in elements:
    tweets.add(element.text)
### Sayfada Aşağıya İnme İleride Lazım olabilir. Js İle Yapıldı.###

lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage")
match = False
while (match==False):
    lastCount = lenOfPage
    time.sleep(2)
    elements = browser.find_elements_by_css_selector(".css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0")
    for element in elements:
        tweets.add(element.text)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage")
    if lastCount == lenOfPage:
        match = True

time.sleep(5)
tweetCount = 1

with open("Tweets.txt", "w", encoding="UtF-8") as file:
    for tweet in tweets:
        file.write(str(tweetCount) + "\n" + tweet + "\n")
        file.write("***********************************\n")
        tweetCount += 1

browser.close()
