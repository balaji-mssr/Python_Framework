from selenium import webdriver
# If you don't see colors (RED and GREEN) on command line, add the below lines
# from colorama import init
# init()
import logging

from features.lib import mysky_constants


def before_all(context):
     print("Executing before all")

def before_feature(context, feature):
     print("Before feature\n")
     # Create logger
     context.logger = logging.getLogger('mysky_tests')
     hdlr = logging.FileHandler('./mysky_tests.log')
     formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
     hdlr.setFormatter(formatter)
     context.logger.addHandler(hdlr)
     context.logger.setLevel(logging.DEBUG)

# Scenario level objects are popped off context when scenario exits

def before_scenario(context, scenario):

    # behave -D XPATHKEY=myaccountpage.buy_pass_button -D

    if 'XPATHKEY' in context.config.userdata.keys():
        context.xpath = context.config.userdata['XPATHKEY']
    else:
        print ("Provide the XPATH Key to extract, Using the Default")
        context.xpath = mysky_constants.MY_ACCOUNT_PAGE + "." + mysky_constants.MY_ACCOUNT_BUY_PASS_BUTTON

    if 'SOURCEXML' in context.config.userdata.keys():
        context.sourceXML = context.config.userdata['SOURCEXML']
    else:
        print ("XML Source File not provided, Using the Default")
        context.sourceXML = './features/data/MyAccount.xml'

    # behave -D BROWSER=chrome
    # Enable the following web driver invocation for Browser based Tests
    # if 'BROWSER' in context.config.userdata.keys():
    #     if context.config.userdata['BROWSER'] is None:
    #         BROWSER = 'chrome'
    #     else:
    #         BROWSER = context.config.userdata['BROWSER']
    # else:
    #     BROWSER = 'chrome'
    #
    # if BROWSER == 'chrome':
    #     context.browser = webdriver.Chrome()
    # elif BROWSER == 'firefox':
    #     context.browser = webdriver.Firefox()
    # elif BROWSER == 'safari':
    #     context.browser = webdriver.Safari()
    # elif BROWSER == 'ie':
    #     context.browser = webdriver.Ie()
    # elif BROWSER == 'opera':
    #     context.browser = webdriver.Opera()
    # elif BROWSER == 'phantomjs':
    #     context.browser = webdriver.PhantomJS()
    # else:
    #     print("Browser you entered:", BROWSER, "is invalid value")
    #
    # context.browser.maximize_window()
    print("Before scenario\n")


def after_scenario(context, scenario):
    print("scenario status" + scenario.status)
    # Capture the failed tests - Screenshots
    # if scenario.status == "failed":
    #     if not os.path.exists("failed_scenarios_screenshots"):
    #         os.makedirs("failed_scenarios_screenshots")
    #     os.chdir("failed_scenarios_screenshots")
    #     context.browser.save_screenshot(scenario.name + "_failed.png")
    # context.browser.quit()

def after_feature(context, feature):
            print("\nAfter Feature")

def after_all(context):
    print("Executing after all. User data:", context.config.userdata)


