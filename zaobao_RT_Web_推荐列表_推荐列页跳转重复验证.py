import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import re

@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_front_duplicate(browser):
    browser.get("https://zaobao.com")
    browser.implicitly_wait(10)

    try:
        article_element = browser.find_element(By.ID, 'recommend_block')
        article_text = article_element.text
        processed_text = re.sub(r'\s+', ' ', article_text).lower()
        words = processed_text.split()
        unique_words = set(words)
        assert len(words) == len(unique_words), "文章内容包含重复部分。"
        print("验证通过：首页推荐文章无重复")

    finally:
        pass

def test_front_click(browser):
    browser.get("https://zaobao.com")
    browser.implicitly_wait(10)
    browser.find_element(By.CSS_SELECTOR, ".pdb15-lg > .category-title > .text-track").click()
    browser.switch_to.window(browser.window_handles[1])
    browser.implicitly_wait(10)

    assert "推荐列表" in browser.title, "未成功跳转至文章列表页面"
    print("验证通过：点击“更多”跳转到-推荐列表页面")

def test_list_page(browser):
    browser.get("https://www.zaobao.com/recommend")
    browser.implicitly_wait(10)
    articles = browser.find_elements(By.ID, 'more-container')
    article_texts = [article.text for article in articles]

    # 处理文章内容，去除多余空格和换行符，转换为小写
    processed_texts = [re.sub(r'\s+', ' ', text).lower() for text in article_texts]

    # 检查文章列表页面内容是否有重复部分
    words = [text for processed_text in processed_texts for text in processed_text.split()]
    unique_words = set(words)

    assert len(words) == len(unique_words), "文章列表页面内容包含重复部分"
    print("验证通过：推荐列表页-内容无重复")


if __name__ == "__main__":
    pytest.main(["-v", "-s", "--html=report.html"])
