import time
from collections import defaultdict

from selenium import webdriver
from selenium.webdriver.common.by import By
import re

# 初始化 WebDriver
driver = webdriver.Chrome()

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

    #articles = driver.find_elements(By.ID, 'more-container')

    article_num = driver.find_elements(By.CLASS_NAME, 'f18.m-eps')

    article_texts = [article.text for article in article_num]
    print(article_texts)



    # 处理文章内容，去除多余空格和换行符，转换为小写
    processed_texts = [re.sub(r'\s+', ' ', text).lower() for text in article_texts]

    # 使用字典统计文章内容的出现次数
    article_count = defaultdict(int)
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
    if duplicates_found:
        raise AssertionError("文章列表页面内容包含重复部分")
    else:
        print("验证通过：推荐列表页-内容无重复")


    # # 检查文章列表页面内容是否有重复部分
    # words = [text for processed_text in processed_texts for text in processed_text.split()]
    # unique_words = set(words)
    #
    #
    #
    # assert len(words) == len(unique_words), "文章列表页面内容包含重复部分"
    # print("验证通过：推荐列表页-内容无重复")


finally:
    # 关闭浏览器
    driver.quit()
