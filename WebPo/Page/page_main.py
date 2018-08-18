from Base.base import Base

class PageMain(Base):
    def page_logout_login(self):
        self.base_click_element("css",".reg")