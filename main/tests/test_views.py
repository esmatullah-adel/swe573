from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from items.models import Item, LengthUnit, WeightUnit, Currency, Condition, Hardness
from django.utils.http import urlencode
import json


class ViewTests(TestCase):

    def setUp(self):
        """Setup test data for views."""
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create test instances for related models
        self.length_unit = LengthUnit.objects.create(title='cm')
        self.weight_unit = WeightUnit.objects.create(title='kg')
        self.currency = Currency.objects.create(title='USD')
        self.condition = Condition.objects.create(title='New')
        self.hardness = Hardness.objects.create(title='Hard')

        # Create an item using model instances for foreign keys
        self.item = Item.objects.create(
            name="Test Item",
            description="Test Description",
            user=self.user,
            length_unit=self.length_unit,  # Pass the model instance, not just the ID
            weight_unit_id=self.weight_unit.id,  # Use ID for weight_unit_id
            price=100,
            currency_id=self.currency.id,  # Use ID for currency_id
            condition_id=self.condition.id,  # Use ID for condition_id
            hardness_id=self.hardness.id,  # Use ID for hardness_id
            weight=50,
            height=10,
            width=5,
            active=1
        )

    def test_dashboard_view(self):
        """Test the dashboard view with GET and POST request."""
        self.client.login(username='testuser', password='testpass')

        # Test GET request to fetch the dashboard with item data
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Item")  # Check if the item appears on the dashboard

        # Prepare data for the POST request
        post_data = {
            'name': 'Test Item',
            'description': 'Test Description',
            'width': '5',
            'min_width': '',
            'max_width': '',
            'length': '10',
            'min_length': '',
            'max_length': '',
            'height': '5',
            'min_height': '',
            'max_height': '',
            'length_unit_id': self.length_unit.id,  # Use ID for length_unit_id
            'weight': '50',
            'min_weight': '',
            'max_weight': '',
            'weight_unit_id': self.weight_unit.id,  # Use ID for weight_unit_id
            'price': '100',
            'min_price': '',
            'max_price': '',
            'currency_id': self.currency.id,  # Use ID for currency_id
            'condition_id': self.condition.id,  # Use ID for condition_id
            'hardness_id': self.hardness.id,  # Use ID for hardness_id
            'taste': 'Sweet',
            'smell': 'Fresh',
            'functionality': 'Useful',
            'age': '2 years',
            'min_age': '',
            'max_age': '',
            'date': '',
            'latitude': '',
            'longitude': ''
        }

        # Test POST request to filter items based on criteria
        response = self.client.post(reverse('dashboard'), json.dumps(post_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertTrue(response_data['success'])

        print(response_data)  # Debug the response data

    def test_logout_view(self):
        """Test the logout view."""
        self.client.login(username='testuser', password='testpass')

        # Test POST request for logout
        response = self.client.post(reverse('logout'))
        self.assertRedirects(response, '/')  # It should redirect to the home page ("/")
        # Check if the user is logged out
        user = self.client.session.get('_auth_user_id')
        self.assertIsNone(user)  # Ensure the user session is cleared after logout
