# items/tests/test_views.py

from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from items.models import Item, LengthUnit
from django.utils.http import urlencode
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image
import tempfile

class ViewTests(TestCase):
    
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(username='testuser', password='testpass')

        # Create some test data for the Item model
        self.length_unit = LengthUnit.objects.create(title='cm')
        self.item = Item.objects.create(
            name="Test Item",
            description="Test Description",
            user=self.user,
            length_unit=self.length_unit,
            price=100,
            weight=50,
            height=10,
            width=5,
            active=1
        )
    
    def test_items_view(self):
        """Test the 'items' view to display items for the logged-in user."""
        self.client.login(username='testuser', password='testpass')
        
        response = self.client.get(reverse('items'))  # Use the URL name for the items view
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Item")
        self.assertContains(response, "Test Description")
    
    def test_new_item_view(self):
        """Test the 'new_item' view for creating an item."""
        self.client.login(username='testuser', password='testpass')

        # Create a sample image to upload
        image_file = self.create_test_image()

        # POST data for creating a new item
        post_data = {
            'name': 'New Item',
            'description': 'New Description',
            'width': 10,
            'length': 20,
            'height': 30,
            'length_unit_id': self.length_unit.id,
            'weight': 200,
            'weight_unit_id': 1,
            'price': 500,
            'currency_id': 1,
            'condition_id': 1,
            'hardness_id': 1,
            'taste': 'Sweet',
            'smell': 'Fresh',
            'functionality': 'Useful',
            'age': '2 years',
            'latitude': 12.345,
            'longitude': 67.890,
            'image': image_file,
            'tag_labels': 'tag1, tag2',
            'tag_ids': '1, 2',
            'materials[]': [1, 2],
            'colors[]': [1],
            'shapes[]': [1],
        }

        response = self.client.post(reverse('new_item'), post_data, format='multipart')

        self.assertEqual(response.status_code, 302)  # Should redirect after saving
        self.assertRedirects(response, reverse('items'))  # Ensure it redirects to the item list

        # Verify the new item is created
        item = Item.objects.get(name="New Item")
        self.assertEqual(item.description, "New Description")
    
    def test_show_item_view(self):
        """Test the 'show_item' view to display a single item."""
        self.client.login(username='testuser', password='testpass')

        response = self.client.get(reverse('show_item', args=[self.item.id]))  # Use the correct URL pattern name
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.item.name)
        self.assertContains(response, self.item.description)
    
    def test_delete_item_view(self):
        """Test the 'delete_item' view to delete an item."""
        self.client.login(username='testuser', password='testpass')

        # Perform the delete action via a POST request
        response = self.client.post(reverse('delete_item', args=[self.item.id]))
        
        self.assertEqual(response.status_code, 302)  # Should redirect after deletion
        self.assertRedirects(response, reverse('items'))  # Should go back to the items list
        with self.assertRaises(Item.DoesNotExist):
            Item.objects.get(id=self.item.id)  # Ensure item is deleted
    
    def test_inactivate_item_view(self):
        """Test the 'inactivate_item' view to toggle an item's active state."""
        self.client.login(username='testuser', password='testpass')

        # Perform inactivate action
        response = self.client.get(reverse('inactivate_item', args=[self.item.id]))
        
        self.assertEqual(response.status_code, 302)  # Should redirect after updating
        self.item.refresh_from_db()  # Reload item from DB
        self.assertEqual(self.item.active, 0)  # Check if the item is inactive
    
    def create_test_image(self):
        """Helper function to create an in-memory image."""
        image = Image.new('RGB', (100, 100), color='red')
        image_file = BytesIO()
        image.save(image_file, 'PNG')
        image_file.seek(0)
        return InMemoryUploadedFile(image_file, None, 'test_image.png', 'image/png', len(image_file.getvalue()), None)
