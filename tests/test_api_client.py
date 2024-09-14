import unittest

from unittest.mock import patch
from src.api_client import get_location 


class ApiClientTests(unittest.TestCase):
    
    # al realizar la prueba se conecta al api externa 
    @unittest.skip
    def test_get_location_return_expected_data(self):
        result = get_location("8.8.8.8")
        self.assertEqual(
            result.get("country"),
            "United States of America"
        )
    
    @patch('src.api_client.requests.get')
    def test_get_location_mocked_return_expected_data(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "countryName": "USA",
            "regionName": "FLORIDA",
            "cityName": "MIAMI",
        }

        result = get_location("8.8.8.8")
        self.assertEqual(result.get("country"), "USA")
        self.assertEqual(result.get("region"), "FLORIDA")
        self.assertEqual(result.get("city"), "MIAMI")
         
        # valida que se llame al api con la url correcta  
        mock_get.assert_called_once_with("https://freeipapi.com/api/json/8.8.8.8") 
