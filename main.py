from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from test_class import TestClass

test=TestClass()
test.test_schedule("https://www.google.com/")
test.test_epicenter("https://www.google.com/")
test.test_anime("https://www.google.com/")