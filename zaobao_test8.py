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


class Test17():
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

    def test_17(self):
        self.driver.get("https://www.zaobao.com/")
        self.driver.set_window_size(1272, 872)
        self.driver.find_element(By.CSS_SELECTOR, ".flex-wrap > .flex > .mgl20:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".tab-tag:nth-child(3)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".flex-wrap .tab-tag:nth-child(1)").click()
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.LINK_TEXT, "港消委会就农夫山泉测试样本归类出现落差致歉").click()
        self.vars["win2176"] = self.wait_for_window(2000)
        self.vars["root"] = self.driver.current_window_handle
        self.driver.switch_to.window(self.vars["win2176"])
        element = self.driver.find_element(By.CSS_SELECTOR, ".nav-item:nth-child(5)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.driver.close()
        self.driver.switch_to.window(self.vars["root"])
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.LINK_TEXT, "俄企发现用人民币直接付款被冻结的情况增多").click()
        self.vars["win309"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win309"])
        self.driver.execute_script("window.scrollTo(0,1)")
        self.driver.close()
        self.driver.switch_to.window(self.vars["root"])
        self.driver.find_element(By.CSS_SELECTOR, ".flex-wrap > .flex > .mgl20:nth-child(2)").click()
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.CSS_SELECTOR, "#real_world > .pdb10:nth-child(3) > .eps").click()
        self.vars["win7103"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win7103"])
        self.driver.execute_script("window.scrollTo(0,657)")
        self.driver.close()
        self.driver.switch_to.window(self.vars["root"])
        self.driver.find_element(By.CSS_SELECTOR, ".tab-tag:nth-child(3)").click()
        self.vars["window_handles"] = self.driver.window_handles
        self.driver.find_element(By.LINK_TEXT, "30亿元洗钱案被告张瑞金 遣送柬埔寨后再被驱逐").click()
        self.vars["win3295"] = self.wait_for_window(2000)
        self.driver.switch_to.window(self.vars["win3295"])
        self.driver.execute_script("window.scrollTo(0,1)")
        self.driver.execute_script("window.scrollTo(0,58)")
        self.driver.execute_script("window.scrollTo(0,64)")
        self.driver.close()
        self.driver.switch_to.window(self.vars["root"])
        self.driver.close()



