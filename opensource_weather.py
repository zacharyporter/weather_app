# Weather API Project 

import tkinter as tk
#Tkinter is used for the GUI 
import requests
# Requests is used for making HTTP request to retrieve data from an API. 

# API Key from openweathermap.org
# Enter API Key from openweathermap.org
api_key =  ""

def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)
    # retrieiving response in json format 
    data = response.json()
    return data



def display_weather():
    location= entry.get()
    weather_data = get_weather(api_key, location)
    if "main" in weather_data:
        temperature = weather_data["main"]["temp"]
        ##converting Kelvin to Farenheight.
        temperature_f = ((temperature - 273.15) * 9/5 + 32)
        description = weather_data["weather"][0]["description"]
        result_label["text"] = f"temperature: {temperature_f} Farenheit \nDescroption: {description}"
    else:
        result_label["text"] = "Unable to retrieve weather data."


# Used to trigger event or (get_weather), used later for displaying weather when enter is hit. 
def on_enter(event):
    display_weather()



# Creating the Tkinter Window 
window = tk.Tk()
window.title("Open-Source Weather App")
window.geometry("300x200")

# Create the input label and entry field 
location_label = tk.Label(window, text ="location: ")
location_label.pack()
entry = tk.Entry(window)
#inserting entry to the .get command above. 
entry.pack()

# This will bind the return key to on_enter to display the weather
entry.bind("<Return>", on_enter) 

# Create the get weather Button
button = tk.Button(window, text="Get Weather", command=display_weather)
button.pack()

# Creating the label that displays the weather result 
result_label = tk.Label(window)
result_label.pack()


#Run the tkiner event loop 
window.mainloop()