from behave import *


@Given("I am on the Form page")
def step_impl(context):
    context.form_page.go_home()


@When("I fill out the form")
def step_impl(context):
    context.form_page.input_first_name("Lidia")
    context.form_page.input_last_name("Ian")
    context.form_page.input_job("social worker")


@When("I click Submit")
def step_impl(context):
    context.form_page.click_submit()


@Then("I am redirected to the Thanks page")
def step_impl(context):
    assert context.browser.get_current_url() == context.thanks_page.URL


@Then("I get a success message")
def step_impl(context):
    assert context.thanks_page.get_message_text() == "The form was successfully submitted!"




@Given("I am on the Form page")
def step_impl(context):
    context.form_page.go_home()


@When("I clear out the form")
def step_impl(context):
    context.form_page.clean_first_name


@When("I click Submit")
def step_impl(context):
    context.form_page.click_submit()


@Then("I am redirected to the Thanks page")
def step_impl(context):
    assert context.browser.get_current_url() == context.thanks_page.URL


@Then("I get a success message")
def step_impl(context):
    assert context.thanks_page.get_message_text() == "The form was successfully submitted!"
