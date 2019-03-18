import titles
import time
from selenium import webdriver
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
def check_men_page(driver):
	swap_pages(3,driver)
	driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div/div[3]/a").click()
	if driver.current_url != 'http://35.182.179.24:4502/content/we-retail/us/en/products/men.html':
		return 0
	swap_pages(3, driver)
	driver.find_element_by_xpath('//*[@id="root_responsivegrid/articles_list"]/ul/li[1]/div/a/div/img')
	if driver.current_url != 'http://35.182.179.24:4502/content/we-retail/us/en/experience/arctic-surfing-in-lofoten.html':
		return 0
	return 1

def check_women_page(driver):
	swap_pages(4, driver)
	driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[3]/a')
	if driver.current_url != 'http://35.182.179.24:4502/content/we-retail/us/en/products/women.html':
		return 0
	return 1

def check_equipment_page(driver):
	swap_pages(5, driver)
	driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div/div[2]/div/a')
	if driver.current_url != 'http://35.182.179.24:4502/content/we-retail/us/en/products/equipment/hiking.html':
		return 0
	return 1

def swap_pages(number, driver):
	if(number == 2):
		driver.find_element_by_xpath('//*[@id="we-example-navbar-collapse-inverse"]/ul/li[2]/a').click()
	if (number == 3):
		driver.find_element_by_xpath('//*[@id="we-example-navbar-collapse-inverse"]/ul/li[3]/a').click()
	if (number == 4):
		driver.find_element_by_xpath('//*[@id="we-example-navbar-collapse-inverse"]/ul/li[4]/a').click()
	if (number == 5):
		driver.find_element_by_xpath('//*[@id="we-example-navbar-collapse-inverse"]/ul/li[5]/a').click()
	if (number == 6):
		driver.find_element_by_xpath('//*[@id="we-example-navbar-collapse-inverse"]/ul/li[6]/a').click()


def main():
	options = Options()
	options.add_argument('--headless')
	options.add_argument('--disable-gpu')
	



	options.add_argument("--window-size=1920,1080")
	options.add_argument("--disable-gpu")
	options.add_argument("--disable-extensions")
	options.add_argument("--proxy-server='direct://'")
	options.add_argument("--proxy-bypass-list=*")
	options.add_argument("--start-maximized")
	options.add_argument("--headless")
	pass_test = 1
	driver = webdriver.Chrome("./chromedriver", options=options)
	driver.get("http://35.182.179.24:4502/content/we-retail/us/en.html	")
	#driver.find_element_by_xpath('//*[@id="username"]').send_keys("admin")
	#driver.find_element_by_xpath('//*[@id="password"]').send_keys("xvfT9T4FRCWV=W@v?=+Q}GHL")
	#driver.find_element_by_xpath('//*[@id="submit-button"]').click()
	time.sleep(1)
	titles_name = titles.Titles(driver)
	#titles.check_first_page()

	if(int(titles_name.check_page(1)) == 0):
		pass_test = 0

	for i in range(2,6):

		swap_pages(i, driver)
		if(int(titles_name.check_page(i)) == 0):
			pass_test = 0
	check_men_page(driver)
	check_women_page(driver)
	check_equipment_page(driver)
	return pass_test
if __name__ == "__main__":
	main()
