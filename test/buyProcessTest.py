import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pyunitreport import HTMLTestRunner
import page.HomePage

class searchBarTests(unittest.TestCase):

    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        driver = cls.driver
        driver.get('https://www.liverpool.com.mx/tienda/home') #
        driver.maximize_window()
        driver.implicitly_wait(15)
    
    def test_search_text_field(self):
        search_field = self.driver.find_element(By.ID,"mainSearchbar")
        #search_field = page.HomePage.homePage.setSearchBar()
        search_field.send_keys("Camara")
        search_buttom = self.driver.find_element(By.CLASS_NAME,'input-group-text')
        search_buttom.click()
        select_camera = self.driver.find_element(By.XPATH,'/html/body/div/div[1]/div[1]/div/div[4]/main/div[2]/div/div/ul/li[1]/a/div')
        select_camera.click()
        buy_buttom = self.driver.find_element(By.ID, 'opc_pdp_buyNowButton')
        buy_buttom.click()
        email = self.driver.find_element(By.ID, 'username')
        password = self.driver.find_element(By.ID, 'password')
        email.send_keys('feragtest@gmail.com')
        password.send_keys('T3st123!')
        password.submit()


    def tearDown(cls) -> None:
        cls.driver.quit()
    
if __name__ == "__main__":
		unittest.main()