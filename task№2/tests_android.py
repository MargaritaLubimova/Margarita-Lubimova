import os
import unittest
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import random

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class AndroidTests(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '9'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['automationName'] = 'UiAutomator2'
        desired_caps['app'] = PATH(
            os.getcwd() + '/GnucashAndroid_v2.4.0.apk'
        )
        desired_caps['appPackage'] = 'org.gnucash.android'
        desired_caps['appActivity'] = 'org.gnucash.android.ui.account.AccountsActivity'
        desired_caps['noReset'] = 'true'

        self.driver = webdriver.Remote('http://0.0.0.0:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_01_install_app_and_check_main_screen(self):
        elem = self.driver.find_element_by_id("btn_save")
        # check page
        title_welcome_page = self.driver.find_element_by_id("android:id/title")
        self.assertEqual(title_welcome_page.text, "Welcome to GnuCash")

        elem.click()  # switch to next page "Default currency"

        # check page
        title_default_currency = self.driver.find_element_by_id("android:id/title")
        self.assertEqual(title_default_currency.text, "Default Currency")

        elem.click()  # switch to next page "Account Setup"

        # check page
        title_account_setup = self.driver.find_element_by_id("android:id/title")
        self.assertEqual(title_account_setup.text, "Account Setup")

        elem.click()  # switch to next page "Feedback Option"

        # check page
        title_feedback_options = self.driver.find_element_by_id("android:id/title")
        self.assertEqual(title_feedback_options.text, "Feedback Options")

        choose_option = self.driver.find_elements_by_id("android:id/text1")
        choose_option[0].click()

        elem.click()  # switch to next page "Review"

        # check page
        title_review = self.driver.find_element_by_id("android:id/title")
        self.assertEqual(title_review.text, "Review")

        elem.click()  # switch to next page "Account"

        dismiss = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id("android:id/button1"))
        dismiss.click()

        toolbar = self.driver.find_element_by_id("org.gnucash.android:id/toolbar")
        title_account = toolbar.find_elements_by_class_name("android.widget.TextView")

        self.assertEqual(title_account[0].text, "Accounts")  # Check that page was opened have a title - "Account"

        tabbar = self.driver.find_element_by_id("org.gnucash.android:id/tab_layout")
        titles_in_tabbar = tabbar.find_elements_by_class_name("android.widget.TextView")
        self.assertEqual(titles_in_tabbar[0].text, "RECENT")  # Check name section RECENT
        self.assertEqual(titles_in_tabbar[1].text, "ALL")  # Check name section ALL
        self.assertEqual(titles_in_tabbar[2].text, "FAVORITES")  # Check name section FAVORITES

    def test_02_check_accounts_page(self):

        categories = self.driver.find_elements_by_id("org.gnucash.android:id/primary_text")

        elem = [elem for elem in categories if elem.text == 'Income']

        elem[0].click()  # Click on Income account

        toolbar = WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_id("org.gnucash.android:id/toolbar"))

        title_income = toolbar.find_elements_by_class_name("android.widget.TextView")
        self.assertEqual(title_income[0].text, "Income")  # Check that page was opened have a title - "Income"

        sub_account_page = self.driver.find_element_by_id("org.gnucash.android:id/pager")
        sub_accounts = sub_account_page.find_elements_by_class_name("android.widget.FrameLayout")
        create_transaction_button = (random.choice(sub_accounts)).\
            find_element_by_id("org.gnucash.android:id/create_transaction")  # Choose one of all sub-accounts

        create_transaction_button.click()  # Click on image "plus"

        description = WebDriverWait(self.driver, 10).\
            until(lambda x: x.find_element_by_id("org.gnucash.android:id/input_transaction_name"))
        description.send_keys("desc")  # Full a description
        amount = self.driver.find_element_by_id("org.gnucash.android:id/input_transaction_amount")
        amount.send_keys("1000")  # Full amount
        transaction_type_switch = self.driver.find_element_by_id("org.gnucash.android:id/input_transaction_type")
        transaction_type_switch.click()  # Set a transaction type (set income)
        save_button = self.driver.find_element_by_id("org.gnucash.android:id/menu_save")
        save_button.click()  # Save the transaction


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
