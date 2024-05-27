from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Testing():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.link = None
        

    def test_link(self, file_path):
        
        page_address = 'file://' + file_path
        self.driver.get(page_address)
        links = self.driver.find_elements(By.TAG_NAME, 'a')

        for link in links:
            href = link.get_attribute('href')

            link.click()
            time.sleep(2)

            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

            if self.driver.current_url == href:
                print("Link is working")

            else:
                print("Link is broken")
            
            self.driver.back()

if __name__ == "__main__":
    test = Testing()
    links = ['C:\\Users\\VINAMRA\Desktop\\Hackone\\landing\\final web pages\\2_login.html',
             'C:\\Users\\VINAMRA\Desktop\\Hackone\\landing\\final web pages\\4_1_studentfeedbackselect.html',
             'C:\\Users\\VINAMRA\Desktop\\Hackone\\landing\\final web pages\\4_2_table.html',
             'C:\\Users\\VINAMRA\Desktop\\Hackone\\landing\\final web pages\\3_dashboard.html']

    for link in links:
        test.test_link(link)
        