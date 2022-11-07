from behave import *


@given('I am on the Homepage')
def step_impl(context):
    context.homepage.go_home()


@when('I click the "{page_link_text}" link')
def step_impl(context, page_link_text):
    context.homepage.go_to(page_link_text)


@then('I am redirected to Form page')
def step_impl(context):
    assert context.browser.get_current_url() == context.form_page.URL


@Given("I am on the Homepage")
def step_impl(context):
    context.homepage.go_home()


@When("I click the Components")
def click_components_menu(context, page_link_text):
    context.homepage.go_to(page_link_text)


@Then("Drop down menu with 14 items is displayed")
def step_impl(context):
    pass
