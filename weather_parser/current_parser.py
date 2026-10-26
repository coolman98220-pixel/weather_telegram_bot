import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 55.4410,
    "longitude": 65.3410,
    "current_weather": True
}

def get_weather_description(code: int):
    
    weather_mapping = {
        0: "Ясно",
        1: "Преимущественно ясно",
        2: "Переменная облачность",
        3: "Пасмурно",
        45: "Туман",
        48: "Осаждающийся изморось (туман с инеем)",
        51: "Слабая морось",
        53: "Умеренная морось",
        55: "Плотная морось",
        56: "Слабая замерзающая морось",
        57: "Плотная замерзающая морось",
        61: "Слабый дождь",
        63: "Умеренный дождь",
        65: "Сильный дождь",
        66: "Слабый замерзающий дождь",
        67: "Сильный замерзающий дождь",
        71: "Слабый снегопад",
        73: "Умеренный снегопад",
        75: "Сильный снегопад",
        77: "Снежная крупа",
        80: "Слабый ливневый дождь",
        81: "Умеренный ливневый дождь",
        82: "Сильный ливневый дождь",
        85: "Слабый ливневый снегопад",
        86: "Сильный ливневый снегопад",
        95: "Гроза (слабая или умеренная)",
        96: "Гроза со слабым градом",
        99: "Гроза с сильным градом"
    }

    if code in weather_mapping:
        return weather_mapping.get(code)
    else:
        return "ошибка"

def get_weather():
    response = requests.get(url, params = params)
    js_data = response.json()

    temp = js_data['current_weather']['temperature']
    windspeed = js_data['current_weather']['windspeed']
    weather_code = get_weather_description(js_data['current_weather']['weathercode'])
    if js_data['current_weather']['is_day'] == 0:
        is_day = 'Солнце за горизонтом'
    else:
        is_day = 'Солнце над горизонтом'     

    description = {
        'temperature': temp,
        'windspeed': windspeed,
        'weathercode': weather_code,
        'is_day': is_day,
    }
    return description

if __name__ == '__main__':
    print(get_weather())