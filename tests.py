import unittest
from gardens import Garden, Plant

class TestGardenMethods(unittest.TestCase):
    def setUp(self):
        self.garden = Garden("test garden")
        self.garden.add_plant('Korean fir')
        self.garden.add_plant('common aster')
        self.garden.add_plant('beautyberry ')

    def test_addPlant_pass(self):
        self.garden.add_plant('grand fir')
        self.assertEqual(len(self.garden.plants), 4)

    def test_addPlant_fail(self):
        self.garden.add_plant('fake plant')
        self.assertEqual(len(self.garden.plants), 3)

    def test_removePlant_pass(self):
        self.garden.remove_plant('Korean fir')
        self.assertEqual(len(self.garden.plants), 2)

    def test_removePlant_fail(self):
        self.garden.remove_plant('fake fir')
        self.assertEqual(len(self.garden.plants), 3)

    def test_filterplants(self):
        f1 = self.garden.filter_plants('name', 'Korean fir')
        self.assertEqual(len(f1), 1)
        f2 = self.garden.filter_plants('water','Moderate')
        self.assertEqual(len(f2), 2)
