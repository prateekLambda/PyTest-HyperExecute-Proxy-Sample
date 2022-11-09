import os

import pytest
import sys
import requests
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json


@pytest.mark.usefixtures('driver')
class TestLink:
    def test_title(self, driver):
        driver.get('https://lambdatest.github.io/sample-todo-app/')
        driver.find_element_by_name("li1").click()
        driver.find_element_by_name("li2").click()

        title = "Sample page - lambdatest.com"
        assert title == driver.title


    def test_item(self, driver):
        driver.get('https://lambdatest.github.io/sample-todo-app/')
        sample_text = "Happy Testing at LambdaTest"
        email_text_field = driver.find_element_by_id("sampletodotext")
        email_text_field.send_keys(sample_text)

        driver.find_element_by_id("addbutton").click()

        li6 = driver.find_element_by_name("li6")
        sys.stderr.write('li6')


    def test_data(self, driver):
        proxies = {
            'http': os.getenv('LT_PROXY_HOST')+':'+os.getenv('LT_PROXY_PORT'),
            'https': os.getenv('LT_PROXY_HOST')+':'+os.getenv('LT_PROXY_PORT'),
        }
        print(proxies)
        driver.get('https://lambdatest.github.io/sample-todo-app/')
        response = requests.get(f"https://ipinfo.io/", proxies=proxies)
        # self.formatted_print(response.json())

        if response.status_code == 200:
            print("sucessfully fetched the data")
            print(json.dumps(response.json(), indent = 1))
        else:
               print(f"Hello person, there's a {response.status_code} error with your request")
