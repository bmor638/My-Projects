import tkinter as tk
import requests

HEIGHT = 500
WIDTH = 600

# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
# 9f07240d9f4e2c8dad6f8489d14bb427

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        if(temp >= 72 and temp < 73):
             poll = "According to a poll\ndone by YouGov America,\nthe majority of Americans agree\nthat this is the ideal temperature!"
             final_str = 'City: %s \nConditions: %s \nTemperature (F): %s\n\nFun fact: %s' % (name, desc, temp, poll)
        else:
             final_str = 'City: %s \nConditions: %s \nTemperature (F): %s' % (name, desc, temp)
    except:
        final_str = 'There was a problem\nretrieving that information.'
    return final_str

def get_weather(city):
    weather_key = '9f07240d9f4e2c8dad6f8489d14bb427'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()
    label['text'] = format_response(weather)

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='C:/Users/Beckett Morris/OneDrive - University of Denver/Documents/UA Keeps/pinky.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#eadfef', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Georgia', 24), fg='#69486f')
entry.place(relwidth=0.65, relheight=1)
entry.focus()          #Makes the cursor start in the entry box

button = tk.Button(frame, text="Get Weather", font=('Georgia', 15), fg='#69486f', command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#eadfef', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=('Georgia', 20), fg='#69486f')
label.place(relwidth=1, relheight=1)

root.mainloop()
