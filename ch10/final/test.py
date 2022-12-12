import requests

response = requests.get(
    "https://api.isthereanydeal.com/v01/game/prices/?key=03922ad0282e94bc15dbbc1717955cbb1af78906&plains=game&region=us&country=US&shops=steam&added=0"
)
print(response.status_code)
print(response.content)
