import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class homePage():

    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
        driver = cls.driver
    
    #Set search bar 

    def setSearchBar(self):
        search_field = self.driver.find_element(By.ID,"mainSearchbar")
        return self