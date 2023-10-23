import request,json

api_key = "d529f7fbf53552967edf9220ea99cc08"
nome da cidade = "Rio de janeiro"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
complete_url = base_url + "appid=" + api_key + "&q=" + nome_da_cidade

response = requests.get(complete_url)
x = response.json()
print(x)