import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Test12():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def wait_for_window(self, timeout=2):
        time.sleep(round(timeout / 1000))
        wh_now = self.driver.window_handles
        wh_then = self.vars["window_handles"]
        if len(wh_now) > len(wh_then):
            return set(wh_now).difference(set(wh_then)).pop()

    def test_12(self):
        self.driver.get("https://www.zaobao.com/")
        self.driver.set_window_size(1272, 872)
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.CSS_SELECTOR, ".pdb15-lg > .category-title > .text-track").click()
        self.vars["win6711"] = self.wait_for_window(2000)
        self.vars["root"] = self.driver.current_window_handle
        self.driver.switch_to.window(self.vars["win6711"])
        self.driver.execute_script("window.scrollTo(0,2881)")
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.CSS_SELECTOR, ".col-12:nth-child(24) .f18").click()
        self.vars["win9569"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win9569"])
        self.driver.execute_script("window.scrollTo(0,1)")
        self.driver.execute_script("window.scrollTo(0,317)")
        self.driver.close()



