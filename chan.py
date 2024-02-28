# 南京工业职业技术大学校园网自动登录脚本
from time import sleep
from selenium.webdriver.support.select import Select
from selenium import webdriver
# 打开浏览器
from selenium.webdriver.chrome.options import Options  # 解决不打开浏览器问题
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By  # 解决browser.find_element_By_

# 校园网ip
login_ip = "http://10.255.200.11"  # 南工大校园网ip
# 配置
username = ""  # 账号
password = ""  # 密码
yys = "@ctcc"  # 运营商（通过下方对应关系来确定符号）

# 联通-> "@cucc"
# 移动-> "@cmcc"
# 电信-> "@ctcc"
# 校园网->""

def login():
    # 配置浏览器
    options = Options()
    # user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
    # options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--window-size=1920,1050") 
    options.add_argument('headless')  # 隐藏浏览器
    # 获取驱动
    # service = ChromeService(executable_path=r"C:\Program Files\Google\Chrome\Application\chromedriver-win64\chromedriver.exe")  # 具体地址为下载的浏览器驱动所在位置
    service = ChromeService(executable_path=r".\chromedriver.exe")  # 具体地址为下载的浏览器驱动所在位置
    driver = webdriver.Chrome(service=service, options=options)
    # 启动浏览器
    driver.get(login_ip)

    # 设置定位等待时间(因网速原因需要等待网页加载好)
    driver.implicitly_wait(3)

    # 判断是否已经登录,已经登录则直接退出
    # noinspection PyBroadException
    # try:
    #     driver.find_element(By.ID, "ispLogoutBtn")
    #     print("already login")
    #     driver.quit()
    #     return
    # # 通过捕获"找不到登出元素异常"来判断未登录
    # except Exception:
    #     print("no login")

    # 设置定位等待时间
    driver.implicitly_wait(1)

    # 定位输入账号处并输入账号
    driver.find_element(By.ID, "username").send_keys(username)

    # 定位密码并输入密码
    driver.find_element(By.ID, "password").send_keys(password)

    # # 定位网络选择并选择网络
    select_ele = driver.find_element(By.ID, "domain")
    select_obj = Select(select_ele)
    select_obj.select_by_value("telecom")

    # 定位登录并点击登录
    driver.find_element(By.ID, "loginBtn").click()

    # 设置定位等待时间
    sleep(1)

    # 关闭浏览器
    driver.quit()


if __name__ == '__main__':
    login()