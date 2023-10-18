import csv

def get_last_xyz(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        last_row = None
        for row in reader:
            last_row = row
        if last_row:
            x, y, z = last_row[2], last_row[3], last_row[4]
            return x, y, z
        else:
            return None, None, None

# Get blade and element numbers from the user
blade_number = input("Please enter the blade number: ")
element_number = input("Please enter the element number: ")

# Construct the filename based on the provided numbers and folder structure
folder_path = "postProcessing/actuatorLineElements/0/"
filename = f"{folder_path}turbine.blade{blade_number}.element{element_number}.csv"

x, y, z = get_last_xyz(filename)
if x and y and z:
    print(f"Last x, y, z values: {x}, {y}, {z}")
else:
    print("The file appears to be empty or there was an issue reading it.")

