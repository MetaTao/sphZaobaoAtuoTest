import re
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from collections import defaultdict

@pytest.fixture(scope="module")#
# setup_module 是一个模块级别的 fixture，在模块中的所有测试函数运行之前执行一次，并在所有测试函数执行完毕后执行一次。
def setup_module():
    # 初始化 WebDriver
    driver = webdriver.Chrome()
    # yield 关键字，表示在 setup_module fixture 执行完毕后将 driver 对象传递给测试函数，然后暂停执行，直到测试函数执行完毕。
    yield driver
    # 在 setup_module fixture 完成后，关闭浏览器
    driver.quit()

def test_check_article_duplicates(setup_module):
    driver = setup_module

    try:
        # 打开文章列表页面
        driver.get("https://www.zaobao.com/recommend")

        # 获取页面初始高度
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            # 模拟滚动到页面底部
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # 等待加载新内容
            time.sleep(2)  # 可根据实际情况调整等待时间

            # 计算新的页面高度
            new_height = driver.execute_script("return document.body.scrollHeight")

            # 如果新页面高度不再变化，说明已经到达页面底部
            if new_height == last_height:
                break
            last_height = new_height

        # 输出页面加载完成提示
        print("页面已滚动到最底部，加载完所有文章。")

        # 获取所有文章元素的文本
        article_num = driver.find_elements(By.CLASS_NAME, 'f18.m-eps')
        article_texts = [article.text for article in article_num]

        # 处理文章内容，去除多余空格和换行符，转换为小写
        processed_texts = [re.sub(r'\s+', ' ', text).lower() for text in article_texts]

        # 创建了一个 defaultdict 对象，该对象在对尚未出现的键进行访问时会自动设置默认值 int初始值0
        # 使用字典统计每个不同的文章文本在列表中出现的次数
        article_count = defaultdict(int)

        # 遍历 processed_texts 列表中的每个元素（文章文本），并将它们作为键，然后递增该键对应的值
        for text in processed_texts:
            article_count[text] += 1

        # 输出总的文章条数
        total_articles = len(article_texts)
        print(f"总的文章条数: {total_articles}")

        # 打印重复的文章内容及其出现次数大于1的情况
        duplicates_found = False
        for text, count in article_count.items():
            if count > 1:
                duplicates_found = True
                print(f"重复的文章内容: {text}, 出现次数: {count}")

        # 检查文章列表页面内容是否有重复部分
        assert not duplicates_found, "文章列表页面内容包含重复部分"

    finally:
        # 不需要关闭浏览器，因为 setup_module fixture 已经处理了关闭操作
        pass
