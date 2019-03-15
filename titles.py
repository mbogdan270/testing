import getpass

class Titles:
	def __init__(self, driver):
		self.driver = driver
	def check_page(self, number):

		title = self.driver.title
		if number == 1 and "English" not in title:
			return 0
		if number == 2 and "Experience" not in title:
			return 0
		if number == 3 and "Men" not in title:
			return 0
		if number == 4 and "Women" not in title:
			return 0
		if number == 5 and "Equipment" not in title:
			return 0
		if number == 6 and "Communities" not in title:
			return 0
		return 1