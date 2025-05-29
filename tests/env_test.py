import unittest
import os
from dotenv import load_dotenv

class TestModelEnvVar(unittest.TestCase):
    def setUp(self):
        load_dotenv()  # Load .env variables before each test

    def test_model_env_variable_exists(self):
        model = os.getenv("MODEL")
        self.assertIsNotNone(model, "MODEL environment variable should not be None")
        self.assertIsInstance(model, str)
        self.assertNotEqual(model.strip(), "", "MODEL environment variable should not be empty")

if __name__ == "__main__":
    unittest.main()
