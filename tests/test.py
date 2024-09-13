

def calculate_total(products,discount:float=0):
    total = 0
    for product in products:
        total += product["price"]

    if discount>0:
      total *= 1 - float(discount/100)

    return total


def test_calculate_total_with_empty_list():
  
    assert calculate_total([]) == 0 


def test_calculate_total_with_single_product():
    products = [ 
       {
           "name": "Notebook",
           "price": 5
       }
    ]    
    assert calculate_total(products) == 5

def test_calculate_total_with_multiple_products():
    products = [ 
       {
           "name": "Notebook",
           "price": 5
       },
       {
           "name": "Pen",
           "price": 2
       }

    ]    
    assert calculate_total(products) == 7

def test_calculate_total_with_discount():
   products = [ 
       {
           "name": "Notebook",
           "price": 5000
       },
       {
           "name": "Pen",
           "price": 5
       }

   ]
   #print(round(calculate_total(products,3))) 
   assert round(calculate_total(products,3)) == 4855


if __name__ == "__main__":
  test_calculate_total_with_empty_list()
  test_calculate_total_with_single_product()
  test_calculate_total_with_multiple_products()
  test_calculate_total_with_discount()