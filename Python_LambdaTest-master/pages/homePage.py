from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.explore_link_xpath= (By.XPATH,"//a[text()='Explore all Integrations']")
        self.footer_css = (By.CSS_SELECTOR,"footer#footer")
        self.logo_id= (By.ID,"header")


    def open(self):
        self.driver.get("https://www.lambdatest.com")

    def wait_for_dom_loaded(self):
        self.wait.until(EC.presence_of_element_located(self.footer_css))
        self.wait.until(EC.presence_of_element_located(self.logo_id))

    def scroll_to_explore_link(self):
        element = self.wait.until(EC.presence_of_element_located(self.explore_link_xpath))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return element

    def click_explore_link(self):
        element = self.scroll_to_explore_link()
        element.click()




