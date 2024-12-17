from django.test import TestCase
from django.contrib.auth.models import User
from items.models import (
    LengthUnit, WeightUnit, Item, Material, Color, Shape,
    Currency, Tag, TagItem, MaterialItem, ColorItem, ShapeItem,
    Comment, Condition, Hardness
)

class ModelsTestCase(TestCase):
    def setUp(self):
        # Create User
        self.user = User.objects.create(username="testuser", password="testpass")
        
        # Create LengthUnit and WeightUnit
        self.length_unit = LengthUnit.objects.create(title="cm")
        self.weight_unit = WeightUnit.objects.create(title="kg")
        
        # Create Condition and Hardness
        self.condition = Condition.objects.create(title="New")
        self.hardness = Hardness.objects.create(title="Hard")

        # Create Item
        self.item = Item.objects.create(
            name="Mystery Box",
            description="A wooden box of unknown origin.",
            functionality="Storage",
            taste=None,
            smell="Woody",
            age="100 years",
            width=10,
            length=15,
            height=5,
            length_unit=self.length_unit,
            weight=2,
            weight_unit_id=self.weight_unit.id,
            price=100,
            currency_id=1,
            hardness_id=self.hardness.id,
            condition_id=self.condition.id,
            user=self.user,
            latitude=40.7128,
            longitude=-74.0060,
            date="2024-01-01",
            active=1
        )

    # Test LengthUnit model
    def test_length_unit_creation(self):
        length_unit = LengthUnit.objects.get(title="cm")
        self.assertEqual(length_unit.title, "cm")

    # Test Item model
    def test_item_creation(self):
        item = Item.objects.get(name="Mystery Box")
        self.assertEqual(item.description, "A wooden box of unknown origin.")
        self.assertEqual(item.user.username, "testuser")
        self.assertEqual(item.weight, 2)
        self.assertEqual(item.length_unit.title, "cm")
        self.assertEqual(item.condition_id, self.condition.id)
        self.assertEqual(item.latitude, 40.7128)
        self.assertEqual(item.longitude, -74.0060)

    # Test Condition model
    def test_condition_creation(self):
        condition = Condition.objects.get(title="New")
        self.assertEqual(condition.title, "New")

    # Test Comment model
    def test_comment_creation(self):
        comment = Comment.objects.create(
            title="Interesting find!",
            item=self.item,
            user=self.user,
            date="2024-06-12"
        )
        self.assertEqual(comment.title, "Interesting find!")
        self.assertEqual(comment.item.name, "Mystery Box")
        self.assertEqual(comment.user.username, "testuser")
        self.assertEqual(comment.date, "2024-06-12")
