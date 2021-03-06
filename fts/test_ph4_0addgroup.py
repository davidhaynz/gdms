# These tests are all based on the tutorial at http://killer-web-development.com/
# if registration is successful this may work but lets
# try and get user logged in first

from functional_tests import FunctionalTest, ROOT, USERS
import time
from selenium.webdriver.support.ui import WebDriverWait


class AddEvent (FunctionalTest):

    def setUp(self):
        self.url = ROOT + '/default/user/login'        
        get_browser = self.browser.get(self.url)

        mailstring = USERS['USER5'] + '@user.com'

        email = WebDriverWait(self, 10).until(lambda self: self.browser.find_element_by_name("email"))
        email.send_keys(mailstring)

        password = self.browser.find_element_by_name("password")    
        password.send_keys(USERS['PASSWORD5'])    
  
        submit_button = self.browser.find_element_by_css_selector("#submit_record__row input")
        submit_button.click()  
        time.sleep(1)  
        
        self.url = ROOT + '/accessgroups/new_group'
        get_browser = self.browser.get(self.url)
        time.sleep(1)

    def test_has_right_heading(self):        
        body = self.browser.find_element_by_tag_name('body')
        self.assertIn('Create Group', body.text)

    def test_group(self):
   
        # questiontext = self.browser.find_element_by_name('questiontext')
        event_name = WebDriverWait(self, 10).until(lambda self: self.browser.find_element_by_id('access_group_group_name'))
        event_name.send_keys("Ph4TestGroup")

        eventdesc = self.browser.find_element_by_id('access_group_group_desc')
        eventdesc.send_keys("Ph4 test public group fuller description")

        submit_button = self.browser.find_element_by_css_selector("#submit_record__row input")
        submit_button.click()
        time.sleep(1)

        welcome_message = self.browser.find_element_by_css_selector(".w2p_flash")
        self.assertIn('Group Created', welcome_message.text)
