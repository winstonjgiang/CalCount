# Winston Giang | CalCounter (Ver.1 Chipotle)

import tkinter
from tkinter import *
from tkinter import ttk

# Application Setup
base = Tk()
base.geometry("510x600")
base.title("CalCounter")
base.iconbitmap('CCIcon.ico')

# Variable Field
total_cal = IntVar()
total_fat = IntVar()
total_protein = IntVar()
total_cal = 0
total_fat = 0
total_protein = 0

# format: protein, fat, calories in grams 
# all information confirmed from Chipotle website as of 01/15/2023

protein_options = {
    'None': [0, 0, 0], 'Chicken': [32, 7, 180], 'Steak': [21, 6, 150], 'Garlic Guajillo Steak': [26, 15, 250], 'Barbacoa': [24, 7, 170], 'Carnitas': [23, 12, 210], 'Sofritas': [8, 10, 150]
}
rice_options = {
    'None': [0, 0, 0], 'White': [4, 4, 210], 'Brown': [4, 6, 210]
}
bean_options = {
    'None': [0, 0, 0], 'Black': [8, 2, 130], 'Pinto': [8, 2, 130]
}
salsa_options = {
    'None': [0, 0, 0], 'Fresh Tomato Salsa' : [0, 0, 25], 'Roasted Chili-Corn Salsa': [3, 2, 80], 'Tomatillo-Green Chili Salsa': [0, 0, 15], 'Tomatillo-Red Chili Salsa': [0, 0, 30]
}
toppings_options = {
    'None': [0, 0, 0], 'Guacamole': [2, 22, 230], 'Sour Cream': [2, 9, 110], 'Fajita Veggies': [1, 0, 20], 'Cheese': [6, 8, 110], 'Romaine Lettuce': [0, 0, 5], 'Queso Blanco': [5, 9, 120]
}

protein_choice = StringVar()
rice_choice = StringVar()
bean_choice = StringVar()
salsa_choice = StringVar()
toppings_choice1 = StringVar()
toppings_choice2 = StringVar()
toppings_choice3 = StringVar()
toppings_choice4 = StringVar()
toppings_choice5 = StringVar()
toppings_choice6 = StringVar()

protein_double = BooleanVar()
rice_double = BooleanVar()
bean_double = BooleanVar()
salsa_double = BooleanVar()

# Functions
def calculate():
    global total_cal, total_fat, total_protein
    total_cal = 0
    total_fat = 0
    total_protein = 0
    for food, nutrition in protein_options.items():
        if food == protein_choice.get():
            total_protein += nutrition[0]
            total_fat += nutrition[1]
            total_cal += nutrition[2]
    if protein_double.get() == True:
        total_protein *= 2
        total_fat *= 2
        total_cal *=2

    for food, nutrition in rice_options.items():
        if food == rice_choice.get():
            total_protein += nutrition[0]
            total_fat += nutrition[1]
            total_cal += nutrition[2]
    if rice_double.get() == True:
        total_protein *= 2
        total_fat *= 2
        total_cal *=2

    for food, nutrition in bean_options.items():
        if food == bean_choice.get():
            total_protein += nutrition[0]
            total_fat += nutrition[1]
            total_cal += nutrition[2]
    if bean_double.get() == True:
        total_protein *= 2
        total_fat *= 2
        total_cal *=2

    for food, nutrition in salsa_options.items():
        if food == salsa_choice.get():
            total_protein += nutrition[0]
            total_fat += nutrition[1]
            total_cal += nutrition[2]
    if salsa_double.get() == True:
        total_protein *= 2
        total_fat *= 2
        total_cal *=2

    for food, nutrition in toppings_options.items():
        if food == toppings_choice1.get():
            total_protein += nutrition[0]
            total_fat += nutrition[1]
            total_cal += nutrition[2]
        if food == toppings_choice2.get():
            total_protein += nutrition[0]
            total_fat += nutrition[1]
            total_cal += nutrition[2]
        if food == toppings_choice3.get():
            total_protein += nutrition[0]
            total_fat += nutrition[1]
            total_cal += nutrition[2]
        if food == toppings_choice4.get():
            total_protein += nutrition[0]
            total_fat += nutrition[1]
            total_cal += nutrition[2]
        if food == toppings_choice5.get():
            total_protein += nutrition[0]
            total_fat += nutrition[1]
            total_cal += nutrition[2]
        if food == toppings_choice6.get():
            total_protein += nutrition[0]
            total_fat += nutrition[1]
            total_cal += nutrition[2]

    calories_label.config(text="Total Calories: " + str(total_cal))
    fat_label.config(text="Total Fat: " + str(total_fat))
    protein_label.config(text="Total Protein: " + str(total_protein))


# Total Nutrition Labels
calories_label = Label(base, text="Total Calories: " + str(total_cal), font=("Arial", 25), fg="green")
calories_label.pack()
fat_label = Label(base, text="Total Fat: " + str(total_fat), font=("Arial", 25), fg="red")
fat_label.pack()
protein_label = Label(base, text="Total Protein: " + str(total_protein), font=("Arial", 25), fg="brown")
protein_label.pack()

# Main Function Button
customize_button = Button(base, text="Customize!", width=25, height=2, command=calculate).pack(pady=15)

# Protein/Meat
meat_label = Label(base, text="Pick a protein:").pack()
protein_pick = OptionMenu(base, protein_choice, *protein_options).pack()
protein_choice.set("None")

# Rice
rice_label = Label(base, text="Pick your rice option:").pack()
rice_pick = OptionMenu(base, rice_choice, *rice_options).pack()
rice_choice.set("None")

# Bean
bean_label=Label(base, text="Pick your bean choice:").pack()
bean_pick = OptionMenu(base, bean_choice, *bean_options).pack()
bean_choice.set("None")

# Salsa
salsa_label = Label(base, text="Pick your salsa choice: ").pack()
salsa_pick = OptionMenu(base, salsa_choice, *salsa_options).pack()
salsa_choice.set("None")

# Toppings
topping_title = Label(base, text="Pick your toppings (Choose twice for doubled): ").pack()

topping_label1 = Label(base, text="Topping 1:").place(x=60, y=430)
topping_pick1 = OptionMenu(base, toppings_choice1, *toppings_options).place(x=50, y=450)
toppings_choice1.set("None")
topping_label2 = Label(base, text="Topping 2:").place(x=225, y=430)
topping_pick2 = OptionMenu(base, toppings_choice2, *toppings_options).place(x=215, y=450)
toppings_choice2.set("None")
topping_label3 = Label(base, text="Topping 3:").place(x=390, y=430)
topping_pick3 = OptionMenu(base, toppings_choice3, *toppings_options).place(x=380, y=450)
toppings_choice3.set("None")
topping_label4 = Label(base, text="Topping 4:").place(x=60, y=495)
topping_pick4 = OptionMenu(base, toppings_choice4, *toppings_options).place(x=50, y=515)
toppings_choice4.set("None")
topping_label5 = Label(base, text="Topping 5:").place(x=225, y=495)
topping_pick5 = OptionMenu(base, toppings_choice5, *toppings_options).place(x=215, y=515)
toppings_choice5.set("None")
topping_label6 = Label(base, text="Toppings 6:").place(x=390, y=495)
topping_pick6 = OptionMenu(base, toppings_choice6, *toppings_options).place(x=380, y=515)
toppings_choice6.set("None")

# Double option
doubleProtein_checkButton = Checkbutton(base, text='Double It!', variable=protein_double).place(x=325, y=225)
doubleRice_checkButton = Checkbutton(base, text='Double It!', variable=rice_double).place(x=325, y=280)
doubleBean_checkButton = Checkbutton(base, text='Double It!', variable=bean_double).place(x=325, y=330)
doubleSalsa_checkButton = Checkbutton(base, text='Double It!', variable=salsa_double).place(x=325, y=385)


base.mainloop()