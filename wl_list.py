import os
from statistics import mode, mean
from tkinter import Tk, filedialog, Label, Entry, Button, Text, END

def process_data():
    # Retrieve user input values
    first_scan_index = int(first_scan_entry.get())
    last_scan_index = int(last_scan_entry.get())
    channels = [int(channel) for channel in channels_entry.get().split(",")]

    # Initialize a dictionary to store the wavelengths, mode, and average for each channel
    channel_stats = {}

    # For each filename number, get the ra1, ra2, ra3
    for channel in channels:
        # Initialize an empty wavelength list for the current channel
        wavelengths = []

        for scan_index in range(first_scan_index, last_scan_index + 1):
            # Create the filename based on channel and scan_index
            filename = f"{scan_index:05d}.RA{channel}"
            full_path = os.path.join(directory, filename)

            if os.path.exists(full_path):
                # Open the file and read the second line
                with open(full_path, "r") as f:
                    file_lines = f.readlines()
                    second_line = file_lines[1]
                    second_line_list = second_line.split()
                    second_line_second_last = second_line_list[-2]
                    file_number = int(second_line_second_last)
                    wavelengths.append(file_number)

        # create a list of wavelengths
        wavelengths_text = "\n".join(map(str, wavelengths))
        wavelengths_output.config(state='normal')
        wavelengths_output.delete(1.0, END)
        wavelengths_output.insert(END, wavelengths_text)
        wavelengths_output.config(state='disabled')

    # Define the value you want to find
    value_to_find = int(value_to_find_entry.get())

    # Initialize an empty list to store indices
    indices = []

    # Iterate over the list and find the indices of the value
    for i, value in enumerate(wavelengths):
        if value == value_to_find:
            indices.append(i)

    # Print the list of indices
    indices_text = "\n".join(map(str, indices))
    indices_output.config(state='normal')
    indices_output.delete(1.0, END)
    indices_output.insert(END, indices_text)
    indices_output.config(state='disabled')

# Create a Tkinter root window
root = Tk()
root.title("Data Processing")

# Function to open file dialog and select directory
def select_directory():
    global directory
    directory = filedialog.askdirectory(title="Select Directory")
    directory_label.config(text=directory)

# Label and entry for directory selection
directory_label = Label(root, text="No directory selected")
directory_label.pack()

select_button = Button(root, text="Select Directory", command=select_directory)
select_button.pack()

# Labels and entries for user input
first_scan_label = Label(root, text="First Scan:")
first_scan_label.pack()
first_scan_entry = Entry(root)
first_scan_entry.pack()

last_scan_label = Label(root, text="Last Scan:")
last_scan_label.pack()
last_scan_entry = Entry(root)
last_scan_entry.pack()

channels_label = Label(root, text="Channels (comma-separated):")
channels_label.pack()
channels_entry = Entry(root)
channels_entry.pack()

value_to_find_label = Label(root, text="Value to Find:")
value_to_find_label.pack()
value_to_find_entry = Entry(root)
value_to_find_entry.pack()

# Button to submit user input and process data
submit_button = Button(root, text="Submit", command=process_data)
submit_button.pack()

# Output for displaying wavelengths
wavelengths_output_label = Label(root, text="List of Wavelengths:")
wavelengths_output_label.pack()
wavelengths_output = Text(root, height=10, width=50, state='disabled')
wavelengths_output.pack()

# Output for displaying indices
indices_output_label = Label(root, text="Indices of Value Found:")
indices_output_label.pack()
indices_output = Text(root, height=5, width=50, state='disabled')
indices_output.pack()

root.mainloop()
