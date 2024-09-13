import unittest

class AllAsertsTests(unittest.TestCase):
    
    def test_assert_equal(self):
        self.assertEqual(10,10)
        self.assertEqual("Hola","Hola")

    def test_assert_true_or_false(self):
        self.assertTrue(True)
        self.assertFalse(False)

    def test_assert_raises(self):
       with self.assertRaises(ValueError):
           int("no_soy_un_numero")        
    
    def test_assert_in(self):
        self.assertIn(10,[2,4,5,10])
        self.assertNotIn(6,[2,4,5,10])

    def test_assert_dicts(self):
        user = {"first_name":"Pedro","last_name":"Madera"}

        self.assertDictEqual(
            {"first_name":"Pedro","last_name":"Madera"},
            user
        )
        
        self.assertSetEqual(
            {1,2,3},
            {1,2,3}
        )