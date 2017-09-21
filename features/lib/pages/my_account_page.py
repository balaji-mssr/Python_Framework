from features.lib import mysky_constants


class MyAccountPage:
    locator_dictionary = {
        mysky_constants.MY_ACCOUNT_BUY_PASS_BUTTON: ".//*[@name='MyAccountPage']/MarkupList/RenderableNode/Button/Label[@text='Buy pass']",
        mysky_constants.MY_ACCOUNT_FOCUSED_BUTTON: ".//*[@name='MyAccountPage']/MarkupList/RenderableNode/Button[@focused='true']"
    }

    def __init__(self, context):
        self.xpath_key = context.xpath
        self.timeout = 30