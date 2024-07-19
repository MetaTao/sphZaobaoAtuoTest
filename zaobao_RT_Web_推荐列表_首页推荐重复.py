from selenium import webdriver
import re

from selenium.webdriver.common.by import By

# 初始化WebDriver（这里使用Chrome，请根据实际情况选择合适的WebDriver）
driver = webdriver.Chrome()

# 打开网页
driver.get("https://zaobao.com")

# 等待加载完成，这里可以根据实际情况调整等待时间
driver.implicitly_wait(10)

try:
    # 定位文章内容的元素

    article_element = driver.find_element(By.ID, 'recommend_block')

    # 获取文章内容文本
    article_text = article_element.text

    print(article_text)

    # 处理文章内容，例如去除多余空格和换行符，转换为小写 ，使用 re.sub() 方法替换字符串中的匹配项；
    processed_text = re.sub(r'\s+', ' ', article_text).lower()

    # 检查是否有重复内容  ，split() 方法用于根据指定的分隔符将字符串分割成多个子字符串，并返回一个包含这些子字符串的列表。
    # len获取对象的长度或者元素个数的函数， set(words)列表转换为集合，集合去重，
    words = processed_text.split()
    unique_words = set(words)

    if len(words) == len(unique_words):
        print("文章内容没有重复部分。")
    else:
        print("文章内容包含重复部分。")

finally:
    # 关闭WebDriver，结束测试
    driver.quit()
