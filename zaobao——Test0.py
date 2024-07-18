from selenium import webdriver
import re

from selenium.webdriver.common.by import By

# 初始化WebDriver（这里使用Chrome，请根据实际情况选择合适的WebDriver）
driver = webdriver.Chrome()

# 打开网页
driver.get("https://zaobao.com")

# 等待加载完成，这里可以根据实际情况调整等待时间
driver.implicitly_wait(10)
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

driver.find_element(By.CSS_SELECTOR, ".mgb15 > .pdb5 > .text-track").click()
 driver.switch_to.window(browser.window_handles[1]))

driver.quit()
