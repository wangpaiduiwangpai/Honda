import time
from selenium import webdriver
import requests
 
# 请求URL
url = '<https://weibo.com/>'
# 请求头部
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}
 
# 解析页面函数
def parse_html(html):
 print(html)
 
# 保存数据函数
def save_data():
 f = open('weibo.txt', 'w', encoding='utf-8')
 browser = webdriver.Chrome()
 browser.get(url)
 time.sleep(10)
 browser.find_element_by_name('username').send_keys('username')
 browser.find_element_by_name('password').send_keys('password')
 browser.find_element_by_class_name('W_btn_a').click()
 time.sleep(10)
 response = requests.get(url, headers=headers, cookies=browser.get_cookies())
 parse_html(response.text)
 browser.close()
 f.close()
 
if __name__ == '__main__':
     save_data()
