import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import re


class ZaobaoHomePage:
    def __init__(self, driver):
        self.driver = driver

    def get_article_text(self):
        article_element = self.driver.find_element(By.ID, 'recommend_block')
        return article_element.text


class ZaobaoArticleListPage:
    def __init__(self, driver):
        self.driver = driver

    def get_article_texts(self):
        articles = self.driver.find_elements(By.CLASS_NAME, 'more-container')
        return [article.text for article in articles]


@pytest.fixture(scope="module")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def zaobao_home_page(browser):
    return ZaobaoHomePage(browser)


@pytest.fixture
def zaobao_article_list_page(browser):
    return ZaobaoArticleListPage(browser)


@pytest.mark.parametrize("url", ['https://zaobao.com', 'https://www.zaobao.com/recommend'])
def test_front_duplicate_and_click(browser, zaobao_home_page, zaobao_article_list_page, url):
    browser.get(url)
    browser.implicitly_wait(10)

    if url == 'https://zaobao.com':
        article_text = zaobao_home_page.get_article_text()
    else:
        article_texts = zaobao_article_list_page.get_article_texts()

    processed_texts = [re.sub(r'\s+', ' ', text).lower() for text in article_texts]
    words = [text for processed_text in processed_texts for text in processed_text.split()]
    unique_words = set(words)

    assert len(words) == len(unique_words), f"页面 {url} 内容包含重复部分"

    if url == 'https://zaobao.com':
        article_link = browser.find_element(By.CSS_SELECTOR, ".pdb15-lg > .category-title > .text-track")
        article_link.click()
        browser.switch_to.window(browser.window_handles[1])
        browser.implicitly_wait(10)

        assert "推荐列表" in browser.title, "未成功跳转至文章列表页面"


if __name__ == "__main__":
    pytest.main(["-v", "-s", "--html=report.html"])