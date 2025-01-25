import time
import unittest
from backend.app import create_app
from backend.app.database import db


class FlaskRouteTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Run once before all tests."""

        config = {
            'TESTING': True,
            'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:'
        }

        cls.app = create_app(test_config=config)
        cls.app_context = cls.app.app_context()
        cls.app_context.push()
        db.create_all()

    @classmethod
    def tearDownClass(cls):
        """Run once after all tests."""
        db.session.remove()
        db.drop_all()
        cls.app_context.pop()
        time.sleep(1)

    def setUp(self):
        """Run before each test."""
        self.client = self.app.test_client()
        self.app.testing = True

    def tearDown(self):
        """Run after each test."""
        db.session.remove()
        db.drop_all()
        db.create_all()

    def test_index_route(self):
        """Test the index route."""
        response = self.client.get('/')
        self.assertEqual(200, response.status_code)

    def test_404_route(self):
        """Test the 404 route."""
        response = self.client.get('/notfound')
        self.assertEqual(404, response.status_code)

    def test_api_sensors_route(self):
        """Test the api/sensors route."""

        # Wait for the first reading to be generated
        time.sleep(11)

        # Get the first reading
        response = self.client.get('/api/sensors')
        self.assertEqual(200, response.status_code)

        # Check the response length
        sample_01 = response.get_json()
        self.assertEqual(1, len(sample_01))

        # Wait for another reading to be generated
        time.sleep(11)

        # Get the next reading
        response = self.client.get('/api/sensors')
        self.assertEqual(200, response.status_code)

        # Check the response length
        sample_02 = response.get_json()
        self.assertEqual(2, len(sample_02))