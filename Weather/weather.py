import requests
import datetime


def weather(city, open_weather_token):
    code_to_smile = {
        "Clear" : "Ясно \U00002600",
        "Clouds" : "Облачно \U00002601",
        "Rain" : "Дождь \U00002614",
        "Drizzle" : "Дождь \U00002614",
        "Thunderstorm" : "Гроза \U000026A1",
        "Snow" : "Снег \U0001F328",
        "Mist" : "Туман \U0001F32B"
    }

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()

        city = data["name"]
        cur_weather = data["main"]["temp"]

        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Посмотри в окно!!!"

        hundity = data["main"]["hundity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        lenght_of_the_day = sunset_timestamp - sunrise_timestamp

        return (f"***{datetime.datetime.now().strftime("%d-%m-%Y %H:%M")}***\n"
              f"Погода в {city}\nТемпература: {cur_weather} °C {wd}\n"
              f"Влажность: {hundity}%\nДавление: {pressure} мм.рт.ст\nВетер: {wind} м/с\n"
              f"Восход солнца: {sunrise_timestamp}\nЗакат солнца: {sunset_timestamp}\nПродолжительность дня: {lenght_of_the_day}"
              )

    except:
        return "\U00002620 Проверь название города! \U00002620"

