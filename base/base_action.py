from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10, poll=1):
        """
        根据元组的feature在timeout时间之内每poll秒照一次，找到对应的一个元素
        :param feature: 元素的特征
        :param timeout: 超时时间
        :param poll: 频率
        :return: 元素
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*feature))
        # return self.driver.find_element(*feature)

    def find_elements(self, feature, timeout=10, poll=1):
        """
        根据元组的feature在timeout时间之内每poll秒照一次，找到对应的一组元素
        :param feature: 元素的特征
        :param timeout: 超时时间
        :param poll: 频率
        :return: 元素
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*feature))

    def click(self, feature):
        self.find_element(feature).click()

    def input(self, feature, value):
        self.clear(feature)
        self.find_element(feature).send_keys(value)

    def clear(self, feature):
        self.find_element(feature).clear()
