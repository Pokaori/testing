from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class TestClass:
    def __init__(self):
        self.driver__ = webdriver.Chrome()
        self.driver__.maximize_window()

    def __del__(self):
        self.driver__.close()

    def search(self, xpath, text):
        search_bar = self.driver__.find_element_by_xpath(xpath)
        search_bar.send_keys(text)
        search_bar.send_keys(Keys.ENTER)

    def test_schedule(self, url):
        self.driver__.get(url)
        self.search(".//*[@class='a4bIc']/input", "Розклад КПІ")
        time.sleep(3)
        self.driver__.find_elements_by_xpath(".//*[@class='yuRUbf']/a")[0].click()
        time.sleep(3)
        self.driver__.find_elements_by_xpath(".//*[@id='ctl00_lBtnSchedule']")[0].click()
        time.sleep(3)
        self.search("//*[@id='ctl00_MainContent_ctl00_txtboxGroup']", "КП-92")
        lecture = self.driver__.find_element_by_xpath("//td[4]/span/a")
        time.sleep(3)
        assert lecture.get_property('textContent') == \
               "Компоненти програмної інженерії 2. Якість та тестування програмного забезпечення", \
               "We don`t have Testing lecture on Wednesday"
        time.sleep(10)

    def test_epicenter(self, url):
        self.driver__.get(url)
        self.search(".//*[@class='a4bIc']/input", "Епіцентр")
        time.sleep(3)
        self.driver__.find_elements_by_xpath(".//*[@class='yuRUbf']/a")[0].click()
        time.sleep(3)
        self.driver__.find_element_by_xpath(".//*[@class='header__info-toggle']").click()
        time.sleep(3)
        self.driver__.find_element_by_xpath(".//*[@title='Контакти']").click()
        time.sleep(3)
        work_time = self.driver__.find_element_by_xpath(".//*[@class='company__content']/h3").get_property('textContent')
        assert work_time.strip() == \
               "Контакт-центр працює для Вас щоденно з 07:30 до 22:30.", \
               "Epicenter doesn`t work from 07:30 to 22:30"
        time.sleep(10)

    def test_anime(self,url):
        self.driver__.get(url)
        self.search(".//*[@class='a4bIc']/input", "Animevost")
        self.driver__.set_page_load_timeout(10)
        try:
            self.driver__.find_elements_by_xpath(".//*[@class='yuRUbf']/a")[0].click()
        except:
            print("We couldn`t load for some time")
        time.sleep(3)
        self.driver__.find_elements_by_xpath(".//*[@id='news_set_sort']/a[2]")[0].click()
        time.sleep(3)
        self.driver__.find_elements_by_xpath(".//*[@class='shortstory']/div/h2/a")[0].click()
        time.sleep(3)
        name=self.driver__.find_elements_by_xpath(".//*[@class='shortstoryContent']//td/h4")[0].get_property("textContent")
        assert  name == \
        "Gekijouban Kimetsu no Yaiba: Mugen Ressha Hen | Demon Slayer the Movie: Mugen Train" \
        " | Истребитель демонов: Бесконечный поезд" , "'Demon Slayer the Movie: Mugen Train' is not the most popular anime"
        time.sleep(10)
