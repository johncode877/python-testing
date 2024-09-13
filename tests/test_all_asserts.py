import unittest

SERVER = "server_a"
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

    @unittest.skip("Trabajo en progreso, será habilitada nuevamente")
    def test_skip(self):
        self.assertEqual("hola","chao")

    #@unittest.skip(True,"Saltado porque no estamos en el servidor")
    ##
    # Si queremos saltar la prueba porque es muy pesada la prueba
    # y se necesita un servidor con muchos recursos
    ##
    @unittest.skipIf(SERVER == "server_a", "Saltado porque no estamos en el servidor")
    def test_skip_if(self):
       self.assertEqual(100,100)

    # Se espera este error en la aplicacion    
    @unittest.expectedFailure
    def test_expected_failure(self):
       self.assertEqual(100,150)