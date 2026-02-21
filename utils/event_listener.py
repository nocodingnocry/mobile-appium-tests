import logging
import allure
from selenium.webdriver.support.events import AbstractEventListener

logger = logging.getLogger(__name__)

class MyListener(AbstractEventListener):
    def before_find(self, by, value, driver):
        logger.debug(f"Поиск элемента: {by} = {value}")

    def before_click(self, element, driver):
        label = element.get_attribute("label") or element.get_attribute("name") or element.tag_name
        message = f"Клик по элементу с тегом <{label}>"
        logger.info(message)
        with allure.step(message):
            pass 

    #def after_change_value_of(self, element, driver): 
    #    logger.info(f"Значение в элементе изменено")

    def on_exception(self, exception, driver):
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Screenshot on failure",
            attachment_type=allure.attachment_type.PNG
        )
        logger.error(f"Ошибка в драйвере: {exception}")