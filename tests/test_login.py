import unittest
import configparser

import HtmlTestRunner
import sys
import os

# Thêm đường dẫn đến thư mục gốc vào sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from utils.browser_setup import BrowserSetup


class LoginTest(unittest.TestCase):

    def setUp(self):
        # Đọc file config.ini
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Lấy URL trang login từ file config
        self.login_url = config['app']['login_url']

        # Khởi tạo trình duyệt
        self.driver = BrowserSetup.get_driver()
        self.driver.get(self.login_url)  # Sử dụng URL từ file config

    def test_valid_login_with_admin_account(self):
        login_page = LoginPage(self.driver)

        login_page.open_login_form()
        # Nhập thông tin đăng nhập
        login_page.enter_username("superadmin@gmail.com")
        login_page.enter_password("admin123")
        login_page.click_login()

        admin_page = AdminPage(self.driver)
        admin_page.check_admin_page_display()
    
    def test_valid_login_with_user_account(self):
        login_page = LoginPage(self.driver)

        login_page.open_login_form()
        # Nhập thông tin đăng nhập
        #1. Enter a valid email in the "E-mail" field
        login_page.enter_username("user@gmail.com")
        
        #2. Enter the correct password in the "Password" field
        login_page.enter_password("Y649394$y")
        
        #3. Click the "Sign In" button
        login_page.click_login()

        # admin_page = AdminPage(self.driver)
        # admin_page.check_admin_page_display()


    def test_Empty_email_and_password_fields_user_account(self):
        login_page = LoginPage(self.driver)

        login_page.open_login_form()
        # Trống trường email và mật khẩu
        #1. Enter a valid email in the "E-mail" field
        login_page.enter_username("user@gmail.com")
        
        #2. Enter an incorrect password in the "Password" field
        login_page.enter_password("Y6493454$23")
        
        #3. Click the "Sign In" button
        login_page.click_login()

        # admin_page = AdminPage(self.driver)
        # admin_page.check_admin_page_display()
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports'))

