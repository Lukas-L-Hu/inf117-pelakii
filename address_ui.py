# Creates a UI to directly enter address to stripe tax, for debugging purposes

import tkinter as tk
from tkinter import messagebox

class UserAddress:
    def __init__(self, root):
        self.root = root
        self.address_current = []

        self.root.title("Address Input")

        # Creates labels and txt entry fields for each part of the address
        labels = ["Street Address", "City", "State", "Postal Code", "Country"]
        self.entries = {}

        for label in labels:
            lbl = tk.Label(root, text=f"Enter {label}:")
            lbl.pack(pady=5)
            
            entry = tk.Entry(root, width=50)
            entry.pack(pady=5)
            
            self.entries[label] = entry

        # Allows for access to the inputs
        self.street_entry = self.entries["Street Address"]
        self.city_entry = self.entries["City"]
        self.state_entry = self.entries["State"]
        self.postal_code_entry = self.entries["Postal Code"]
        self.country_entry = self.entries["Country"]

        # Creates a submit button
        submit_button = tk.Button(root, text="Submit", command=self.submit_address)
        submit_button.pack(pady=20)

    def submit_address(self):
        self.address_current = []
        street = self.street_entry.get()
        city = self.city_entry.get()
        state = self.state_entry.get()
        postal_code = self.postal_code_entry.get()
        country = self.country_entry.get()

        if street and city and state and postal_code and country:
            messagebox.showinfo("Address Submitted", 
                                f"Street Address: {street}\nCity: {city}\nState: {state}\nPostal Code: {postal_code}\nCountry: {country}")
            self.address_current = [street, city, state, postal_code, country]
            self.root.quit()  
            # Closes the UI after submission
        else:
            messagebox.showwarning("Input Error", "Please enter all parts of the address.")


'''
#class user_adress
address_current = []

# Function to handle the submission of the address
def submit_address():
    global address_current
    address_current = []
    street = street_entry.get()
    city = city_entry.get()
    state = state_entry.get()
    postal_code = postal_code_entry.get()
    country = country_entry.get()

    if street and city and state and postal_code and country:
        messagebox.showinfo("Address Submitted", 
                            f"Street Address: {street}\nCity: {city}\nState: {state}\nPostal Code: {postal_code}\nCountry: {country}")
        address_current = [street, city, state, postal_code, country]
    else:
        messagebox.showwarning("Input Error", "Please enter all parts of the address.")
    

# Create the main application window
root = tk.Tk()
root.title("Address Input")

# Create a label and entry for each part of the address
labels = ["Street Address", "City", "State", "Postal Code", "Country"]
entries = {}

for label in labels:
    lbl = tk.Label(root, text=f"Enter {label}:")
    lbl.pack(pady=5)
    
    entry = tk.Entry(root, width=50)
    entry.pack(pady=5)
    
    entries[label] = entry

# Access the individual entries
street_entry = entries["Street Address"]
city_entry = entries["City"]
state_entry = entries["State"]
postal_code_entry = entries["Postal Code"]
country_entry = entries["Country"]

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=submit_address)
submit_button.pack(pady=20)

# Run the application
root.mainloop()
'''