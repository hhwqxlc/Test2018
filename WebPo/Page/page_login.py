from Base.base import Base
class PageLogin(Base):

    # 输入用户名和密码
    def page_login(self,username,password):
        # 跳转定位页面 调用base类点击元素方法
        self.base_click_element("plink","登录")
        # 输入用户名和密码
        self.base_input_text("css","[name='login_info']",username)
        self.base_input_text("css","[name='password']",password)
        # 点击登录
        self.base_click_element("css","[value='登录']")

