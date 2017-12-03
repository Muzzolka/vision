from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get("https://recepcja.visionexpress.pl")
umow_wizyte = browser.find_element_by_class_name("active")
umow_wizyte.click()
menu = browser.find_elements_by_css_selector("a[href='/wizyta/rodzaj/kolejne-dobranie-okularow']")
menu[0].click()
browser.find_element_by_class_name("icon-link-shop").click()
assert "Dane" in browser.page_source
browser.find_element_by_id("ve_ereception_patient_firstname").send_keys("Anna")
browser.find_element_by_id("ve_ereception_patient_lastname").send_keys("Staniszewska")
browser.find_element_by_id("ve_ereception_patient_age").send_keys("42")
browser.find_element_by_id("ve_ereception_patient_email").send_keys("fake@fake.fake")
field = browser.find_element_by_id("ve_ereception_patient_phone")
field.send_keys("123456789")
field.send_keys(Keys.ENTER)
assert "Wybierz salon" in browser.page_source
browser.find_element_by_css_selector("a.btn.btn-primary.change-city").click()


#browser.find_element_by_xpath("//li[@class='active']")