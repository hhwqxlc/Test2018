from Page.page_login import PageLogin
from Page.page_main import PageMain
from selenium import webdriver
class PageExit():
    def __init__(self,brower="firefox"):
        self.driver=None
        if brower=="ie":
            self.driver=webdriver.Ie()
        elif brower=="firefox":
            self.driver=webdriver.Firefox()
        elif brower=="chrome":
            self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.get("http://localhost/iwebshop/index.php")
        self.driver.maximize_window()
    # 获取登录页面对象
    def page_get_login_object(self):
        return PageLogin(self.driver)
    # 获取主页面对象
    def page_get_logout_object(self):
        return PageMain(self.driver)