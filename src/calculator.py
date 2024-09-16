

def substract(a, b):
  '''
  >>> substract(2,10)
  -8

  '''
  return a - b


def sum(a, b):
  '''
  >>> sum(5,7)
  12

  >>> sum(4,-4)
  0
  '''
  return a + b


def multiply(a,b):
  '''
  >>> multiply(2,10)
  20
  '''
  return a*b

def division(a,b):
  '''
  >>> division(10,0)
  Traceback (most recent call last):
  ValueError: Numbers non zero are allowed
  
  ''' 

  if b == 0:    
   raise ValueError("Numbers non zero are allowed")
  
  return a / b

    