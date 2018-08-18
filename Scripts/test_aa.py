import allure
import pytest
class Test():
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step('我是测试步骤001')
    def test001(self):
        allure.attach('执行步骤', '我是测试步骤001的描述～～～')
        print("我被执行了")
        assert 0
    @allure.step('我是测试步骤002')
    def test002(self):
        allure.attach('执行步骤', '我是测试步骤002的描述～～～')
        print("我被执行了")
        assert 1