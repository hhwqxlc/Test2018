import time

from Page.page_exit import PageExit
import unittest
class TestLogin(unittest.TestCase):
    def setUp(self):
        # 切记 实例化一次
        page=PageExit()
        self.page_login=page.page_get_login_object()
        self.page_logout=page.page_get_logout_object()
        self.page_login.driver.get("http://localhost/iwebshop/")
    def tearDown(self):
        time.sleep(3)
        self.page_login.driver.quit()
    def test_login(self):
        # 第一输入用户名和密码
        self.page_login.page_login("admin","123456")
        # 断言

        # 退出
        time.sleep(3)
        self.page_logout.page_logout_login()
if __name__ == '__main__':
    unittest.main()