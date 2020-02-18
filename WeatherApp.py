# Python program to find current 
# weather details of any city 
# using openweathermap api 

# import required modules 
import requests, json			# HTTP Request modules
from tkinter import *			# Tkinter module (main)
from tkinter import ttk			# Tkinter ttk/grid submodule
from tkinter import messagebox	# Tkinter messagebox submodule
import yaml						# yaml config file module

# Enter your API key here 
data = ""
with open('api_key.yaml') as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
api_key = data

# base_url variable to store url 
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# User-defined functions
def query_weather(*args):
	try:
		# complete_url variable to store 
		# complete url address 
		complete_url = base_url + "appid=" + api_key + "&q=" + city_name.get() 

		# get method of requests module 
		# return response object 
		response = requests.get(complete_url) 

		# json method of response object 
		# convert json format data into 
		# python format data 
		result = response.json() 

		if result["cod"] != "404": 
			y = result["main"] 
			if temp_format.get() == 2:
				current_temperature.set(str(y["temp"]))
			else:
				current_temperature.set(str(round(y["temp"]-273.15,1)))
			current_pressure.set(str(y["pressure"])) 
			current_humidity.set(str(y["humidity"])) 
			z = result["weather"] 
			weather_description.set(str(z[0]["description"]))
			return result
		#elif result["cod"] == "404": 
		#	current_temperature.set("")
		#	current_pressure.set("")
		#	current_humidity.set("")
		#	weather_description.set("")
		#	messagebox.showerror(title="Error Found!", message="City came could not be found!")
		#	return "NA"
		else:
			current_temperature.set("")
			current_pressure.set("")
			current_humidity.set("")
			weather_description.set("")
			messagebox.showerror(title="Error Found!", message="City came could not be found!")
			return "NA"
	except:
		pass

# Initialize Desktop GUI
root = Tk()
root.title("City Weather App")

# Layout of GUI

#T	City Weather App
#		Column 1		|	Column 2					|	Column 3
#1	Enter City Name:	|	(city_name_entry)			|
#2	Query Results:
#3	Current Temperature:|	(current_temperature_text)	|	() degC
#4														|	() kelvin
#5	Current Pressure:	|	(current_pressure_text)		|	hPa
#6	Current Humidity:	|	(current_humidity_text)		|	%
#7	Weather Description:|	(weather_description_text)		
#8														|  |QUERY|

# TK GUI Intialization
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)	

# GUI variable declaration and intialization
city_name = StringVar()
current_temperature = StringVar()
current_pressure = StringVar()
current_humidity = StringVar()
weather_description = StringVar()
temp_format = IntVar()
temp_format.set(1)

# GUI implementation
# Row One - City Name (Entry)
ttk.Label(mainframe, text="Enter city name :").grid(column=1, row=1, sticky=W)
city_name_entry = ttk.Entry(mainframe, width=15, textvariable=city_name)
city_name_entry.grid(column=2, row=1, sticky=(W, E))

# Row Two
ttk.Label(mainframe, text="----  Query Results  ----").grid(column=1, row=2, columnspan=3)

# Row Three - Temperature (result)
ttk.Label(mainframe, text="Current Temperature :").grid(column=1, row=3, sticky=W)
ttk.Label(mainframe, textvariable=current_temperature).grid(column=2, row=3, sticky=(E))
# ttk.Label(mainframe, text="degC").grid(column=3, row=3, sticky=W)
ttk.Radiobutton(mainframe, text='degC', variable=temp_format, value=1).grid(column=3, row=3, sticky=W)
ttk.Radiobutton(mainframe, text='Kelvin', variable=temp_format, value=2).grid(column=3, row=4, sticky=W)

# Row Four - Pressure (result)
ttk.Label(mainframe, text="Current Pressure :").grid(column=1, row=5, sticky=W)
ttk.Label(mainframe, textvariable=current_pressure).grid(column=2, row=5, sticky=(E))
ttk.Label(mainframe, text="hPa").grid(column=3, row=5, sticky=W)

# Row Five - Humidity (result)
ttk.Label(mainframe, text="Current Humidity :").grid(column=1, row=6, sticky=W)
ttk.Label(mainframe, textvariable=current_humidity).grid(column=2, row=6, sticky=(E))
ttk.Label(mainframe, text="%").grid(column=3, row=6, sticky=W)

#Row Six - Weather Description (result)
ttk.Label(mainframe, text="Description :").grid(column=1, row=7, sticky=W)
ttk.Label(mainframe, textvariable=weather_description).grid(column=2, row=7, sticky=(W, E), columnspan=3)

# Row Seven - Query (Button)
ttk.Button(mainframe, text="QUERY", command=query_weather).grid(column=3, row=8, sticky=W)

# Padding to frame edges
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

# Other bindings
city_name_entry.focus()
root.bind('<Return>', query_weather)

#GUI loop
root.mainloop()