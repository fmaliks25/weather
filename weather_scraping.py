import tkinter as tk
from tkinter import ttk, messagebox
import requests

def fetch_weather(api_key, city):
    base_url = f' http://api.openweathermap.org/data/2.5/weather?q=London&appid=6e93b3d15872f914c6929fed9ea71e9a'

    response = requests.get(base_url)

    if response.status_code == 200:
        data = response.json()
        weather_desc = data['weather'][0]['description'].capitalize()
        temp = data['main']['temp']
        humidity = data['main']['humidity']

        return f"Weather: {weather_desc}\nTemperature: {temp}°C\nHumidity: {humidity}%"
    else:
        raise Exception(f"Failed to retrieve data from {base_url}. Status code: {response.status_code}")

def on_fetch_button_click():
    api_key = api_key_entry.get()
    city = city_entry.get()

    if not api_key:
        messagebox.showerror('Error', 'Please enter your OpenWeatherMap API Key.')
        return

    if not city:
        messagebox.showerror('Error', 'Please enter a city.')
        return

    try:
        weather_data = fetch_weather(api_key, city)

        result_text.configure(state='normal')
        result_text.delete('1.0', tk.END)
        result_text.insert(tk.END, weather_data)
        result_text.configure(state='disabled')

        messagebox.showinfo('Success', 'Weather data fetched successfully.')
    except Exception as e:
        messagebox.showerror('Error', f'Failed to fetch weather data.\nError: {str(e)}')

root = tk.Tk()
root.title('Weather Data Fetcher')

api_key_label = ttk.Label(root, text='OpenWeatherMap API Key:')
api_key_entry = ttk.Entry(root, width=40)
city_label = ttk.Label(root, text='City:')
city_entry = ttk.Entry(root, width=40)
fetch_button = ttk.Button(root, text='Fetch Weather', command=on_fetch_button_click)
result_label = ttk.Label(root, text='Weather Data:')
result_text = tk.Text(root, wrap=tk.WORD, width=40, height=6, state='disabled')

api_key_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
api_key_entry.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)
city_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
city_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)
fetch_button.grid(row=2, column=0, columnspan=2, pady=10)
result_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
result_text.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
