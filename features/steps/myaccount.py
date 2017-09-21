from behave import *
from lxml import etree as ET

from features.lib import mysky_constants
from features.lib.pages.my_account_page import MyAccountPage
import xmlunittest

use_step_matcher("re")
test_case = xmlunittest.XmlTestMixin()


@given('I have my sky account subscription details page')
def step_impl(context):
    context.tree = ET.parse(context.sourceXML)
    context.root = context.tree.getroot()
    test_case.assertXmlDocument(ET.tostring(context.tree))


@when("I check for page elements")
def step_impl(context):
    xpath_keys_list = context.xpath.split(",")
    for xpath in xpath_keys_list:
        page_name, xpath_key = xpath.split(".")
        # TO - DO
        # Using PageFactory to get the specific page object by given page_name
        page = MyAccountPage(context)
        button_labels = context.root.findall(page.locator_dictionary[xpath_key])
        assert len(button_labels) > 0
        findTheElementsByXPath(button_labels, context, xpath_key)


def findTheElementsByXPath(button_labels, context, xpath_key):
    displayed_page_elements = []
    for button_label in button_labels:
        button = button_label.getparent() if xpath_key == mysky_constants.MY_ACCOUNT_BUY_PASS_BUTTON else button_label
        displayed_page_elements.append(str.format(button.get('name')))
        context.displayedPageElements = ','.join(displayed_page_elements)


@then("the page elements are displayed")
def step_impl(context):
    assert len(str(context.displayedPageElements)) > 0
    print ("Retrieving the page element for given XPath " + context.xpath + " : " + context.displayedPageElements)


