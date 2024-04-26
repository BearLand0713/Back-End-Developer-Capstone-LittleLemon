from django.test import TestCase
import sys
sys.path.append(r'C:\Users\dd121\OneDrive\desktop\Online Courses\Coursera\Meta Back-end\LittleLemon\LittleLemon\env\littlelemon\restaurant')
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")