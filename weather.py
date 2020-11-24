from tkinter import *
import requests
import json

root = Tk()
root.title("Weather App")
root.geometry("450x40")


# https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=7CCB228B-8EA4-464C-909F-8B1A683C56F4

try:
    api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=5&API_KEY=7CCB228B-8EA4-464C-909F-8B1A683C56F4")
    api = json.loads(api_request.content)
except Exception as e:
    api = "Error . . ."

full_statues = api[0]["ReportingArea"] + " " + str(api[0]["AQI"] )+ " " + api[0]["Category"]["Name"]
my_label = Label(root , text = full_statues,font=("Helvetica",20))
my_label.pack()

root.mainloop()