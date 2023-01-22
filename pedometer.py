import tkinter as tk

def calculate_value(distance):
    return distance/0.762

def on_submit():
    input_number = int(input_field.get())
    result = calculate_value(input_number)
    result_label.config(text="Steps walked: " + str(round(result)))

root = tk.Tk()
root.title("Enter distance in metres")

input_field = tk.Entry(root)
input_field.pack()

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
