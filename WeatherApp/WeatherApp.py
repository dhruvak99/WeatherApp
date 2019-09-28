import Tkinter as tk
from PIL import ImageTk,Image 
import tkFont
import requests
HEIGHT = 500
WIDTH=600
#api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
#523b3bcb8ae5ae17f70896907c5a79d4
def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']/10
		final_str= "City: "+str(name)+"\nCondition: " + str(desc)+ "\nTemperature :" + str(temp)+"'C"
	except:
		final_str = "Not available"
	return final_str
def get_weather(city):
	weather_key = '523b3bcb8ae5ae17f70896907c5a79d4'
	url = 'http://api.openweathermap.org/data/2.5/weather'
	params = {'APPID':weather_key,'q':city,'units':'Celsius'}
	response = requests.get(url,params=params)
	weather = response.json()

	label['text'] = format_response(weather)

root = tk.Tk()
root.title("Weather App")
canvas = tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()
#setting the background image
background_image = Image.open("landscape.jpg")
#background_image = tk.PhotoImage(file="landscape.png")
background_image = background_image.resize((1400,800))
background_image = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root,image=background_image)
background_label.place(relx=0,rely=0,relheight=1,relwidth=1)

frame  = tk.Frame(root,bg='#F1ED95',bd=5)
frame.place(relx=0.5,rely=0.1,relheight=0.1,relwidth=0.75,anchor='n')

entry = tk.Entry(frame,font=("Modern", "13"),bg='white')
entry.place(relwidth=0.65,relheight=1)

button = tk.Button(frame,bg='white',text="Get Weather",font='40',command=lambda:get_weather(entry.get()))
button.place(relx=0.7,relwidth=0.3,relheight=1)

lower_frame = tk.Frame(root,bg='#F1ED95',bd=10)
lower_frame.place(relx=0.5,rely=0.25,relheight=0.6,relwidth=0.75,anchor='n')

label = tk.Label(lower_frame,bg='white',font=("Courier", "18"),anchor='nw',justify='left')
label.place(relwidth=1,relheight=1)
root.mainloop()