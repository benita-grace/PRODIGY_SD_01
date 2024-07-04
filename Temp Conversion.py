import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin * 9/5) - 459.67

def convert_temperature():
    try:
        temp_value = float(entry_temp.get())
        temp_unit = combo_unit.get()

        if temp_unit == 'Celsius (°C)':
            fahrenheit = celsius_to_fahrenheit(temp_value)
            kelvin = celsius_to_kelvin(temp_value)
            result.set(f"{temp_value}°C is {fahrenheit:.2f}°F and {kelvin:.2f}K.")
        elif temp_unit == 'Fahrenheit (°F)':
            celsius = fahrenheit_to_celsius(temp_value)
            kelvin = fahrenheit_to_kelvin(temp_value)
            result.set(f"{temp_value}°F is {celsius:.2f}°C and {kelvin:.2f}K.")
        elif temp_unit == 'Kelvin (K)':
            celsius = kelvin_to_celsius(temp_value)
            fahrenheit = kelvin_to_fahrenheit(temp_value)
            result.set(f"{temp_value}K is {celsius:.2f}°C and {fahrenheit:.2f}°F.")
        else:
            messagebox.showerror("Invalid unit", "Please select a valid unit of measurement.")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid temperature value.")

root = tk.Tk()
root.title("Temperature Converter")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

label_temp = ttk.Label(frame, text="Enter the temperature value:")
label_temp.grid(row=0, column=0, sticky=tk.W)

entry_temp = ttk.Entry(frame)
entry_temp.grid(row=0, column=1, sticky=(tk.W, tk.E))

label_unit = ttk.Label(frame, text="Select the unit of measurement:")
label_unit.grid(row=1, column=0, sticky=tk.W)

combo_unit = ttk.Combobox(frame, values=["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"])
combo_unit.grid(row=1, column=1, sticky=(tk.W, tk.E))
combo_unit.set("Celsius (°C)")  # Default value

button_convert = ttk.Button(frame, text="Convert", command=convert_temperature)
button_convert.grid(row=2, column=0, columnspan=2)

result = tk.StringVar()
label_result = ttk.Label(frame, textvariable=result, foreground="blue")
label_result.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E))

frame.columnconfigure(1, weight=1)

root.mainloop()
