import requests


class AbstractAPI:
    '''
    This class sets up an API that converts USD to another currency 
    '''

    def __init__(self, target):
        '''
        This function takes target as an argument which is defined in main. target is the currency that is being converted to
        '''
        self.api_url = f'https://exchange-rates.abstractapi.com/v1/live/?api_key=44a798b260654b7885facc0c3ffb7c8c&base=USD&target={target}'
        self.target = target

    def get(self):
        '''
        This function querys the api and returns the exchange rate of the currency specified in target
        '''
        r = requests.get(self.api_url)
        response = r.json()

        if "exchange_rates" in response:
            return response["exchange_rates"][self.target]
        return ""
