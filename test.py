#!/usr/bin/env python3

import unittest
import json
import app

class TestHello(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.client = app.app.test_client()

    def test_home(self):
        rv = self.client.get("/")
        data = json.loads(rv.data)

        self.assertEqual(rv.status_code, 200)
        self.assertEqual(data["message"], "Hello World!")

    def test_hello_root(self):
        rv = self.client.get("/hello")
        data = json.loads(rv.data)

        self.assertEqual(rv.status_code, 200)
        self.assertEqual(data["message"], "Hello World!")

    def test_hello_user(self):
        name = "Simon"
        rv = self.client.get(f"/hello/{name}")
        data = json.loads(rv.data)

        self.assertEqual(rv.status_code, 200)
        self.assertEqual(data["message"], f"Hello {name}!")

if __name__ == "__main__":
    unittest.main()