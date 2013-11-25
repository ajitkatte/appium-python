#android_calculator_appium.py. Run these test cases on Android 4.2
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver
import unittest

#using Unit Test
class AndroidCalculatorTest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Remote(
		command_executor='http://127.0.0.1:4723/wd/hub',
		#need add two extra capabilities for native app, appium requires app-package and app-activity: testing will start from this activity
		desired_capabilities={'browserName': 'Android',
								'version': '4.2',
								'platform': 'Windows"',
								'app-package': 'com.android.calculator2',
								'app-activity': 'com.android.calculator2.Calculator' })
								
	#test case to test addition operation
	def test_add_operation(self):
		driver = self.driver
		driver.find_element_by_name("2").click()
		driver.find_element_by_name("+").click()
		driver.find_element_by_name("4").click()
		driver.find_element_by_name("=").click()
		result = driver.find_element_by_tag_name("EditText").text
		self.assertIn("6",result)
	
	#test case to test substraction operation	
	def test_sub_operation(self):
		driver = self.driver
		driver.find_element_by_name("9").click()
		driver.find_element_by_name("minus").click()
		driver.find_element_by_name("4").click()
		driver.find_element_by_name("=").click()
		result = driver.find_element_by_tag_name("EditText").text
		self.assertIn("5",result)
		
	#test case to test multiplication operation	
	def test_mul_operation(self):
		driver = self.driver
		driver.find_element_by_name("9").click()
		driver.find_element_by_name("multiply").click()
		driver.find_element_by_name("4").click()
		driver.find_element_by_name("=").click()
		result = driver.find_element_by_tag_name("EditText").text
		self.assertIn("36",result)
	
	#test case to test division operation
	def test_div_operation(self):
		driver = self.driver
		driver.find_element_by_name("9").click()
		driver.find_element_by_name("divide").click()
		driver.find_element_by_name("3").click()
		driver.find_element_by_name("=").click()
		result = driver.find_element_by_tag_name("EditText").text
		self.assertIn("3",result)

	def tearDown(self):
	#close is not working with appium so I've used quit
		self.driver.quit()
		
if __name__ == "__main__":
    unittest.main()