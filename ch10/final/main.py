import AbstractAPI
import IsThereAnyDealAPI


def main():
    '''
    This function combines the two APIs where it will ask the user what game they want the price of.
    Then it asks the user what currency they want the price of the game to be in.
    Then returns the information in a string
    '''

    #loop until an game is entered and a price is found
    while True:
        #ask the user what game they want the price of
        game = input(
            "Enter a game that is availabe on Steam (default is Deep Rock Galactic):"
        ).replace(" ", "").lower()
        #sets default game if no game is input above
        if game == '':
            game = "deeprockgalactic"
        #query api and get price for game
        itad = IsThereAnyDealAPI.IsThereAnyDealAPI(game)
        price = itad.get()
        #if price is found
        if price != "":
            break
        #error messege and reset input
        print("Game not found")

    #loop until a currency is entered and a rate is found
    while True:
        #asks user what currency they would like to convert to
        currency = input(
            "What currency would you like to exchange to (Default EUR):"
        ).upper()
        #sets default currency if no currency is input above
        if currency == '':
            currency = "EUR"
        #query api and get conversion rate for USD to specified currency
        target = AbstractAPI.AbstractAPI(currency)
        rate = target.get()

        #if rate is found
        if rate != "":
            break
        #error message and reset input
        print("Currency not found")

    #calculates the price of game by multiplying conversion rate to price of game
    converted = price * rate
    #prints the information of the game currency and what the converted price will be
    print(f'The price of {game} in {currency} is {converted}.')


main()
