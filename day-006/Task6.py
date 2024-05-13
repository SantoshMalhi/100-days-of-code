import requests
import matplotlib.pyplot as plt

def fetch_weather_data():
    api_key = '1539e50fd697f00366550471d6b1fc63'
    city = 'Umerkot'
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    print(data)  # Print the data received from the API
    return data

def visualize_temperature(data):
    dates = []
    temperatures = []

    for entry in data['list']:
        dates.append(entry['dt_txt'])
        temperatures.append(entry['main']['temp'])

    plt.figure(figsize=(10, 5))
    plt.plot(dates, temperatures, marker='o', linestyle='-', color='b')
    plt.title('Temperature Trends in Umerkot')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    weather_data = fetch_weather_data()
    visualize_temperature(weather_data)

if __name__ == "__main__":
    main()
