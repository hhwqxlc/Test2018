import time
from selenium import webdriver
class Base():
    def __init__(self,driver):
        self.driver=driver
    # 查找元素
    def base_find_element(self,type,value):
        el=None
        if type=="id":
            el=self.driver.find_element_by_id(value)
        elif type=="class_name":
            el=self.driver.find_element_by_class_name(value)
        elif type=="css":
            el=self.driver.find_element_by_css_selector(value)
        elif type=="xpath":
            el=self.driver.find_element_by_xpath(value)
        elif type=="name":
            el=self.driver.find_element_by_name(value)
        elif type=="tag_name":
            el=self.driver.find_element_by_tag_name(value)
        elif type=="plink":
            el=self.driver.find_element_by_partial_link_text(value)
        elif type=="link":
            el=self.driver.find_element_by_link_text(value)
        if el is not None:
            return el

    # 输入元素
    def base_input_text(self,type,value,input_text):
        self.base_find_element(type,value).send_keys(input_text)
    # 点击元素
    def base_click_element(self,type,value):
        self.base_find_element(type,value).click()
    # 获取截屏
    def get_screen_shot(self):
        # 时间戳
        time_stamp=time.strftime("%Y_%m_%d %H_%M_%S")
        self.driver.get_screenshot_as_file("../Image/%s.png"%time_stamp)
