#!/usr/bin/env python
# coding: utf-8

# In[29]:


import csv
import requests
import tkinter as tk

class Weather:
    def __init__(self, temperature, humidity, pressure, wind_speed):
        self._temperature = temperature 
        self._humidity = humidity
        self._pressure = pressure
        self._wind_speed = wind_speed
    def display_weather(self):
        raise NotImplementedError("Subclass must implement abstract method")
    def save_to_csv(self, location):
        with open('weather_data.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([location,
                             self._temperature, 
                             self._humidity, 
                             self._pressure,
                             self._wind_speed])

class WeatherAPI:
    def __init__(self, api_key):
        self._api_key = api_key
    def fetch_weather(self, location):
        raise NotImplementedError("Subclass must implement abstract method")

class CurrentWeather(Weather):
    def display_weather(self):
        print(f"Current Temperature: {self._temperature}°C")
        print(f"Humidity: {self._humidity}%")
        print(f"Pressure: {self._pressure} hPa")
        print(f"Wind Speed: {self._wind_speed} m/s")

class OpenWeatherAPI(WeatherAPI):
    def fetch_weather(self, location):
        url = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={self._api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        if response.status_code != 200:
            print(f"Error fetching weather data: {data.get('message', 'Unknown error')}")
            return None
        if 'main' not in data or 'wind' not in data:
            print(f"Unexpected API response structure: {data}")
            return None
        weather = CurrentWeather(
            data["main"]["temp"],
            data["main"]["humidity"],
            data["main"]["pressure"],
            data["wind"]["speed"])
        return weather

class UserInput:
    @staticmethod
    def get_location():
        return input("Enter location: ")

class WeatherDisplay:
    @staticmethod
    def show(weather):
        weather.display_weather()

def fetch_and_display_weather():
    location = textbox.get("1.0", tk.END).strip()
    if not location:
        return
    weather_api = OpenWeatherAPI(api_key)
    weather = weather_api.fetch_weather(location)
    if weather:
        label_T1.config(text=f"{weather._temperature}°C")
        label_H1.config(text=f"{weather._humidity}%")
        label_W1.config(text=f"{weather._pressure} hPa")
        label_S1.config(text=f"{weather._wind_speed} m/s")
        weather.save_to_csv(location)

api_key = "8f85c24bd5674261b50236721d2842c9"

# Create the main window
root = tk.Tk()
root.config(bg = "sky blue")
root.geometry("500x500")
root.title("Weather App")

label = tk.Label(root, text = "Weather App", font = ('Arial', 25)) 
label.pack(padx=25, pady=25)

textbox = tk.Text(root, font = ('Arial', 14))
textbox.place(x=80, y=90, height=50, width=350)

label_T = tk.Label(root, text = "Temperature", font = ('Arial', 25)) 
label_T.place(x=15, y=220, height=50, width=210)
label_T1 = tk.Label(root, text = "", font = ('Arial', 25)) 
label_T1.place(x=240, y=220, height=50, width=210)

label_H = tk.Label(root, text = "Humidity", font = ('Arial', 25)) 
label_H.place(x=15, y=280, height=50, width=210)
label_H1 = tk.Label(root, text = "", font = ('Arial', 25)) 
label_H1.place(x=240, y=280, height=50, width=210)

label_W = tk.Label(root, text = "Pressure", font = ('Arial', 20)) 
label_W.place(x=15, y=340, height=50, width=210)
label_W1 = tk.Label(root, text = "", font = ('Arial', 20)) 
label_W1.place(x=240, y=340, height=50, width=210)

label_S = tk.Label(root, text = "Wind Speed", font = ('Arial', 20)) 
label_S.place(x=15, y=400, height=50, width=210)
label_S1 = tk.Label(root, text = "", font = ('Arial', 20)) 
label_S1.place(x=240, y=400, height=50, width=210)

button = tk.Button(root, text="Check Weather", font=('Arial', 15), command=fetch_and_display_weather)
button.pack(padx=50, pady=60)

# Start the Tkinter event loop
root.mainloop()


# In[ ]:




