from browser import Browser
from pages.base_page import BasePage
from pages.homepage import Homepage
from pages.form_page import FormPage
from pages.thanks_page import ThanksPage


def before_all(context):
    context.browser = Browser()
    context.basepage = BasePage(context.browser.driver)
    context.homepage = Homepage(context.browser.driver)
    context.form_page = FormPage(context.browser.driver)
    context.thanks_page = ThanksPage(context.browser.driver)


def after_all(context):
    context.browser.close()