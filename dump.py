import requests

API_KEY = "9b63303a6de581d6c6f2c9edaca25796"

#API CALL FOR INPUT = https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

base_url = f"https://api.openweathermap.org/data/2.5/weather"

while True:

    user_input = input("What city would you like the weather of? \nTo quit, press (q).\n")
    if user_input == "q":
        break

    solid_url = f"{base_url}?q={user_input}&appid={API_KEY}"

    response = requests.get(solid_url)
    data = response.json()
    #print(data)

    def get_data():
        description = data['weather'][0]['description']
        temperature = round(data['main']['temp'] - 273.15, 2)
        feels_like = round(data['main']['feels_like'] - 273.15, 2)
        country = data['sys']['country']
        print("Weather :", description)
        print("The temperature is", temperature, "celsius")
        print("Temperature feels like", feels_like, "celsius")
        print("Country :", country)


    if response.status_code == 200:
        get_data()
        print()

    else:
        print("Error! Invalid city, please re-enter.")
        print()