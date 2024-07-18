import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="module")
def browser():
    # 初始化 WebDriver
    driver = webdriver.Chrome()
    yield driver
    # 测试完成后关闭 WebDriver
    driver.quit()


def test_news_functionality(browser):
    # 打开网页
    browser.get("https://zaobao.com")

    # 等待页面加载完毕
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "news-container")))

    # 验证分类按钮功能
    categories = ["中国", "国际", "新加坡"]
    for category in categories:
        # 点击分类按钮
        category_button = browser.find_element(By.XPATH, f"//button[text()='{category}']")
        category_button.click()

        # 等待新闻加载
        WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "news-list")))

        # 检查新闻列表中是否有12条新闻
        news_items = browser.find_elements(By.CLASS_NAME, "news-item")
        assert len(news_items) == 12

    # 验证新闻详情页功能
    first_news_title = browser.find_element(By.CLASS_NAME, "news-item-title")
    first_news_title_text = first_news_title.text
    first_news_title.click()

    # 等待新闻详情页加载
    WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "news-detail")))

    # 验证是否成功打开了正确的新闻详情页
    assert browser.find_element(By.CLASS_NAME, "news-detail-title").text == first_news_title_text

    # 返回新闻列表页面
    browser.back()

    # 验证“更多”按钮功能
    more_buttons = browser.find_elements(By.CLASS_NAME, "more-button")
    for more_button in more_buttons:
        more_button.click()

        # 等待跳转到更多列表页面
        WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "more-news-list")))

        # 验证是否成功跳转到了更多列表页面
        assert "more-news" in browser.current_url.lower()

        # 返回原页面
        browser.back()

