import random as rd
import PySimpleGUI as sg 
import pandas as pd

#backend Part
data = pd.read_csv('data.csv')
dataframe = pd.DataFrame(data)
Data_value = dataframe['0'].tolist()
#Data_value1 = Data_value.tolist()
#print(Data_value)
#print(type(Data_value))
def lottery():
	lottery = rd.sample(Data_value,1)
	for item in Data_value[1:500]:
		print(item)
		window['-comment1-'].update(item)
	window['-comment2-'].update(lottery)




#frontend
sg.theme('SandyBeach')
layout = [ [sg.Text(' ')],
         [sg.Text(' ',size=(4,1)),sg.Image('mohsen.png')],
		 [sg.Text('  ',size=(8,1)),sg.Text('قرعه کشی برنج محسن',font=('B Titr',22))],
		 [sg.Text(' نام کاربری شرکت کنندگان ',font=('Iran Sans',16)),sg.Output(size=(20,1),font='arial', key='-comment1-')],
		 [sg.Text('برنده قرعه کشی',font=('Iran Sans',16)),sg.StatusBar('-',size=(20,1), key='-comment2-',font='arial')],
		 [sg.Text('  ',size=(15,1)),sg.Button(button_text='قرعه کشی',button_color=('white','red'),size=(8,2),font=('Iran Sans',16))],
		 ]
window = sg.Window('قرعه کشی', layout)
while True:
	event , values = window.read()
	if event == sg.WINDOW_CLOSED:
		break
	if event == 'قرعه کشی':
		lottery()