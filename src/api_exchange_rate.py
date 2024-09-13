

class Api_Exchange_Rate:
    
    exchange_rate = 3.75
    available = False
    
    def __init__(self):
      pass

    def get_exchange_rate(self):
       if self.available:          
          return self.exchange_rate
       else:
          return 0  
     
    def is_available(self):
       return self.available
    
    
    