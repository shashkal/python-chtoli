from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter.ttk import Combobox


class my_combobox:
    def __init__(self, list, font, x, y, width, window):
        self.x = x
        self.y = y
        self.list = list
        self.font = font
        self.width = width
        self.window = window


        self.combobox = Combobox(values=self.list, font=self.font, state="readonly", style="TCombobox")
        self.combobox.place(x=self.x, y=self.y, width=self.width)
        self.combobox.bind('<<ComboboxSelected>>', lambda event: self.select())

    def select(self):
        global price, servis
        if self.combobox.get() == self.list[0]:
            self.price = 1000
        elif self.combobox.get() == self.list[1]:
            self.price = 2008
        elif self.combobox.get() == self.list[2]:
            self.price = 1500
        elif self.combobox.get() == self.list[3]:
            self.price = 3060
        elif self.combobox.get() == self.list[4]:
            self.price = 5000
        elif self.combobox.get() == self.list[5]:
            self.price = 3500
        elif self.combobox.get() == self.list[6]:
            self.price = 1000
        else:
            self.price = 0

        price = self.price
        servis = self.combobox.get()
        self.new_label = MyLabel("Цена: " + str(self.price) + " руб.", "Arial 15", "white", 450, 250)

class MyWindow:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("700x700")
        self.window.title("АВТОСЕРВИС CAT & Co")
        self.window.configure(bg="black")
        self.window.resizable(width=False, height=False)
        self.__my_canvas()
        self.__new_label()
        self.__new_entry()
        self.__new_button()
        self.__new_combobox()
        self.window.mainloop()

    def __my_canvas(self):
        self.canvas = Canvas(self.window, width=670, height=670, bg="gray")
        self.canvas.pack()

    def __new_label(self): 
        self.label_title = MyLabel("АВТОСЕРВИС САТ & Co", "Arial 20", "white", 180, 50)
        self.label_marka = MyLabel("Марка автомобиля:", "Arial 15", "white", 50, 150)
        self.label_model = MyLabel("Модель автомобиля:", "Arial 15", "white", 50, 200)
        self.label_color = MyLabel("Цвет:", "Arial 15", "white", 50, 250)
        self.year_build = MyLabel("Год производства:", "Arial 15", "white", 50, 300)
        self.car_number = MyLabel("Номер автомобиля:", "Arial 15", "white", 50, 350)
        self.car_servise = MyLabel("Наименование услуги:", "Arial 15", "white", 450, 150) 

    def __new_entry(self):
        self.entry_marka = MyEntry(270, 150, 150)
        self.entry_model = MyEntry(270, 200, 150)
        self.entry_color = MyEntry(270, 250, 150)
        self.entry_year_build = MyEntry(270, 300, 150)
        self.entry_number = MyEntry(270, 350, 150)

    def __new_button(self):
        self.write_btn = MyButton("Записать", "Arial 15", 500, 600, 100, self)

    def __new_combobox(self):
        self.list = [
            'Замена детали', 'Технический осмотр',
            'Покраска', 'Ремонт детали', 'Замена масла',
            'Замена шин', 'Мойка'
        ]
        self.services_combobox = my_combobox(self.list, "Arial 13", 450, 200, 200, self)

class MyLabel:
    def __init__(self, text, font, color, x, y):
        self.label = Label(text=text, font=(font, 12), bg=color)
        self.label.place(x=x, y=y)

class MyEntry:
    def __init__(self, x, y, width):
        self.value = StringVar()
        self.entry = Entry(textvariable=self.value, font=("Arial", 12))
        self.entry.place(x=x, y=y, width=width)

class MyButton:
    def __init__(self, text, font, x, y, width, window):
        self.text = text
        self.font = font
        self.x = x
        self.y = y
        self.width = width
        self.window = window
        self.button = Button(text=self.text, font=self.font, command=self.click)
        self.button.place(x=self.x, y=self.y, width=self.width)

    def click(self):
        self.value_marka = self.window.entry_marka.value.get()
        messagebox.showinfo("Внимание!", self.value_marka)
        self.value_marka = self.window.entry_marka.value.get()
        self.value_model = self.window.entry_model.value.get()
        self.value_color = self.window.entry_color.value.get()
        self.value_year_build = self.window.entry_year_build.value.get()
        self.value_number = self.window.entry_number.value.get()
        messagebox.showinfo("Сообщение", "Данные успешно загружены!")
        self.print_file()

    def print_file(self):
        file = open('new_otchet.txt', 'w', encoding="utf8")
        file.write("Марка машины:" + self.value_marka + "\n")
        file.write("Модель машины:" + self.value_model + "\n")
        file.write("Цвет машины:" + self.value_color + "\n")
        file.write("Год производства:" + self.value_year_build + "\n")
        file.write("Номер машины:" + self.value_number + "\n")
        file.write("Услуга" + servis + "\n")
        file.write("Стоимость" + str(price) + "\n")        
        file.close()

new_window = MyWindow()