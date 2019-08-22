import requests
import unittest
from unittest import TestCase
import os
import json
import random


class TestCaseCategories(TestCase):

    url = 'http://localhost:3030/categories'

    with open(os.getcwd() + "/helper/category.json") as json_file:
        category = json.load(json_file)

    def test_honors_required_fields_when_validating(self):
        # Post a blank body so we get all the required errors

        result = requests.post(url=self.url)

        self.assertEqual(result.status_code, 400)

        with open(os.getcwd() + "/helper/required_params_categories.json") as json_file:
            data = json.load(json_file)
            len_reg = len(data["required"])

        self.assertEqual(len((result.json())["errors"]), len_reg)

    def test_allows_category_creation_when_valid_category_data_is_passed(self):
        id = "pcat123456" + str(random.randrange(10000, 99999))
        param = {
            "name": "Test Category",
            "id": id
        }
        result = requests.post(url=self.url, data=param)

        self.assertEqual(result.status_code, 201)
        self.assertEqual((result.json())["id"], id)

    def test_can_get_category_by_id(self):
        result = requests.get(url=self.url + "/" + self.category["id"])

        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json(), self.category)
        self.assertEqual(result.json()["name"], self.category["name"])

    def test_can_get_category_by_id_and_select_only_name_and_id(self):
        result = requests.get(url=self.url + "/" + self.category["id"] + "?$select[]=name")

        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json()["id"], self.category["id"])
        self.assertEqual(result.json()["name"], self.category["name"])
        self.assertEqual(len(result.json()), 2)

    def test_returns_404_for_bad_category_id(self):
        result = requests.get(url=self.url + "/" + "123")

        self.assertEqual(result.status_code, 404)

    def test_can_get_default_list(self):
        result = requests.get(url=self.url)
        print(result.json())

        self.assertEqual(result.status_code, 200)
        self.assertTrue(result.json()["total"])
        self.assertEqual(len(result.json()["data"]), 10)

    def test_allows_pagination(self):
        result = requests.get(url=self.url + "?$limit=15&$skip=15")

        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json()["skip"], 15)
        self.assertEqual(len(result.json()["data"]), 15)

    def test_can_search_on_partial_category_name(self):
        result = requests.get(url=self.url + "?name[$like]=*TV*")

        self.assertEqual(result.status_code, 200)
        self.assertTrue(len(result.json()["data"]) > 0)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCaseCategories)
    unittest.TextTestRunner(verbosity=2).run(suite)
