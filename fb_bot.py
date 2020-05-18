import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

from time import sleep
option = Options()

option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})


path = "C:\Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome( options= option,executable_path= path)



def login():
    email_user, password_user = "ip_sapkota@hotmail.com", "Nishant&Mancity487"
    login_page = driver.get("https://www.facebook.com/")
    email = driver.find_element_by_id("email")
    password = driver.find_element_by_id("pass")
    email.send_keys(email_user)
    password.send_keys(password_user)
    email.send_keys(Keys.RETURN)
    sleep(10)



def search_name():
    person = "Ps Singh"
    input_text = driver.find_element_by_name("q")
    input_text.send_keys(person)
    input_text.send_keys(Keys.RETURN)
    sleep(3)
    name = driver.find_element_by_link_text(person)
    name.click()
    sleep(6)

def hit_like():
    page = driver.find_element_by_tag_name('html')
    for i in range(6):
        page.send_keys(Keys.END)
        sleep(6)
    page.send_keys(Keys.HOME)
    sleep(3)
    likes = driver.find_elements_by_link_text("Like")
    for like in likes:
        like.click()

def main():
    login()
    search_name()
    hit_like()

main()





