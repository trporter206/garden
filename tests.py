import unittest
from gardens import Garden, Plant
from datetime import timedelta

class TestGardenMethods(unittest.TestCase):
    def setUp(self):
        self.garden = Garden("test garden")
        self.garden.add_plant('Korean fir')
        self.garden.add_plant('common aster')
        self.garden.add_plant('beautyberry')

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

    def test_clearplants(self):
        self.garden.clear_plants()
        self.assertEqual(len(self.garden.plants), 0)

    def test_stats(self): # TODO
        pass

class TestPlantMethods(unittest.TestCase):
    def setUp(self):
        self.plant = Plant('Edward Goucher abelia', 'Moderate',
                           "Full sun, Part sun/part shade",
                           "Acidic, Well-drained",
                           'Zone 6: (-23 to -18 C)',
                           'Moderate',
                           2.0,
                           2.0,
                           "Green, Red",
                           "Green, Yellow, Dark-red",
                           "Showy, Pink")

    def test_editNotes(self):
        self.assertEqual(self.plant.notes, "")
        old_note = self.plant.notes
        self.plant.edit_notes("This is really nice")
        self.assertNotEqual(old_note, self.plant.notes)

    def test_age(self):
        self.assertTrue(self.plant.age() > timedelta(seconds=0))
