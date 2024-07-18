import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import re

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_count_real_china(browser):
    browser.get("https://zaobao.com")
    browser.implicitly_wait(10)
    real_china_articles = browser.find_element(By.ID, 'real_china')
    cn_eps_elements = real_china_articles.find_elements(By.CLASS_NAME, 'eps')

    article_count = 0
    for element in cn_eps_elements:
        article_count += 1

    assert article_count == 15, f"Expected 15 articles, but found {article_count} articles"
    print("验证通过：即时-中国-文章数量等于15条")


def test_count_real_world(browser):
    browser.get("https://zaobao.com")
    browser.implicitly_wait(10)
    real_world_articles = browser.find_element(By.ID, 'real_world')
    world_eps_elements = real_world_articles.find_elements(By.CLASS_NAME, 'eps')

    article_count = 0
    for element in world_eps_elements:
        article_count += 1

    assert article_count == 15, f"Expected 15 articles, but found {article_count} articles"
    print("验证通过：即时-国际-文章数量等于15条")

def test_count_real_singapore(browser):
    browser.get("https://zaobao.com")
    browser.implicitly_wait(10)
    real_singapore_articles = browser.find_element(By.ID, 'real_singapore')
    singapore_eps_elements = real_singapore_articles.find_elements(By.CLASS_NAME, 'eps')

    article_count = 0
    for element in singapore_eps_elements:
        article_count += 1

    assert article_count == 15, f"Expected 15 articles, but found {article_count} articles"
    print("验证通过：即时-新加坡-文章数量等于15条")


def test_real_click_more(browser):
    browser.get("https://zaobao.com")
    browser.implicitly_wait(10)
    browser.find_element(By.CSS_SELECTOR, ".mgb15 > .pdb5 > .text-track").click()
    browser.switch_to.window(browser.window_handles[1])
    browser.implicitly_wait(10)

    assert "即时新闻 | 联合早报网" in browser.title, "未成功跳转至文章列表页面"
    print("验证通过：点击更多 跳转到-即时列表页")


if __name__ == "__main__":
    pytest.main(["-v", "-s", "--html=report.html"])