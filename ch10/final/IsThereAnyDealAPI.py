import requests


class IsThereAnyDealAPI:
    '''
    This class sets up the API to retrive the price of a game from steam
    '''

    def __init__(self, game):
        '''
        This function takes the game name as an argument defined in main. The game is input into the url
        '''
        self.api_url = f'https://api.isthereanydeal.com/v01/game/prices/?key=03922ad0282e94bc15dbbc1717955cbb1af78906&plains={game}&region=us&country=US&shops=steam'
        self.game = game

    def get(self):
        '''
        This function creates a request that gets the price of the game and returns the price
        '''
        r = requests.get(self.api_url)
        response = r.json()
        list = response["data"][self.game]["list"]
        print(response)
        if len(list) != 0:
            for item in list:
                if "price_new" in item:
                    return item["price_new"]
        return ""