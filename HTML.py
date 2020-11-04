import requests
url = "https://weather167.p.rapidapi.com/clima"
headers = {
    'x-rapidapi-host': "weather167.p.rapidapi.com",
    'x-rapidapi-key': "06caedb4ecmsha598b4fa137ab19p19771cjsne879c4977c8f"
    }
response = requests.request("GET", url, headers=headers)
print(response.text)