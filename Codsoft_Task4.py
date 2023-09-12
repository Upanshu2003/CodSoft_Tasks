from tkinter import *
import requests
import json
from datetime import datetime
 
root =Tk()
root.geometry("500x500") 
root.resizable(0,0) 
root.title("Weather forecaster")
 
city_value = StringVar()
 
def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()
 
city_value = StringVar()
 
def showWeather():
    
    api_key = "51f2f03e2a609ab85f5854748f04c5af"
 
    city_name=city_value.get()
 
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key
 
    response = requests.get(weather_url)
 
    weather_info = response.json()
 
    tfield.delete("1.0", "end")
 
    if weather_info['cod'] == 200:
        cod = 200
        
        temp = int(weather_info['main']['temp'] - cod)                                     
        feels_like_temp = int(weather_info['main']['feels_like'] - cod)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']
 
        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)
 
        weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"
 
    tfield.insert(INSERT, weather)  
 
#------------------------------Frontend part Interface
 
city_head= Label(root, text = 'Enter City Name', font = 'Arial 12 bold', fg="red").pack(pady=10) 
 
inp_city = Entry(root, textvariable = city_value,  width = 24, font='Arial 14 bold').pack()
 
Button(root, command = showWeather, text = "Check Weather", font="Arial 10", bg='lightblue', fg='darkblue', activebackground="teal", padx=6, pady=6 ).pack(pady= 30)
 
weather_now = Label(root, text = "The Weather is:", font = 'arial 12 bold', bg="darkblue", fg="white").pack(pady=20)
 
tfield = Text(root, width=46, height=10)
tfield.pack()
 
root.mainloop()
