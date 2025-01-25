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
        self.assertEqual(response.status_code, 200)

    def test_404_route(self):
        """Test the 404 route."""
        response = self.client.get('/notfound')
        self.assertEqual(response.status_code, 404)

    def test_api_sensors_route(self):
        """Test the sensor route."""

        # Test the GET method
        response = self.client.get('/api/sensors')
        self.assertEqual(response.status_code, 200)

        # Check the default response length
        data = response.get_json()
        self.assertIsNotNone(data)