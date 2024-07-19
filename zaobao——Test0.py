from selenium import webdriver
import re

from selenium.webdriver.common.by import By

# 初始化WebDriver（这里使用Chrome，请根据实际情况选择合适的WebDriver）
driver = webdriver.Chrome()

# 打开网页
# driver.get("https://zaobao.com")
#
# # 等待加载完成，这里可以根据实际情况调整等待时间
# driver.implicitly_wait(10)
#
# article_element = driver.get("https://www.zaobao.com/")
# # 获取id为"real_china"的列表内文章数目
# real_china_articles = driver.find_element(By.ID, 'real_china')
#
# cn_eps_elements = real_china_articles.find_elements(By.CLASS_NAME, 'eps')
#
# # for element in eps_elements:
# #     title = element.text.strip()
# #     print(title)
#
# article_count = 0
# for element in cn_eps_elements:
#     article_count += 1
#
# assert article_count == 15, f"Expected 15 articles, but found {article_count} articles"
# print("验证通过：文章数量等于15条")
#
# real_china_articles = driver.find_element(By.ID, 'real_world')
#
# world_eps_elements = real_china_articles.find_elements(By.CLASS_NAME, 'eps')
#
#
# real_china_articles = driver.find_element(By.ID, 'real_singapore')
#
# singapore_eps_elements = real_china_articles.find_elements(By.CLASS_NAME, 'eps')

driver.get("https://www.zaobao.com/recommend")
driver.implicitly_wait(10)
articles = driver.find_elements(By.CLASS_NAME, 'more-container')
article_texts = [article.text for article in articles]

# 处理文章内容，去除多余空格和换行符，转换为小写
processed_texts = [re.sub(r'\s+', ' ', text).lower() for text in article_texts]

# 检查文章列表页面内容是否有重复部分
words = [text for processed_text in processed_texts for text in processed_text.split()]
unique_words = set(words)

assert len(words) == len(unique_words), "文章列表页面内容包含重复部分"
print("验证通过：推荐列表页-内容无重复")


driver.quit()
