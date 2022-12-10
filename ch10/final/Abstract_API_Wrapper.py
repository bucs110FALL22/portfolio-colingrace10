import requests 

class Abstract:
  
  def __init__(self, api_key = ):
    self.api_url = "https://www.cheapshark.com/api/1.0/"
    self.url = f'https://opentdb.com/api.php?amount={amount}&category={category}'

  def get(self, game_name):
    parameters = {
      title: game_name
    }
    r = request.get(self.api_url) 
    response = r.json()
       