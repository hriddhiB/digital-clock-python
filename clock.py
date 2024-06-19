import tkinter# Import the tkinter library
import time  # Import the time library

# Function to update the time
def update_time():
    current_time = time.strftime("%H:%M:%S %p")  # Get the current time in hours:minutes:seconds format
    clock_label.config(text=current_time)  # Update the label text with the current time
    clock_label.after(1000, update_time)  # Call this function again after 1000 milliseconds (1 second)

# Create the main window
root = tkinter.Tk()  # Create the main application window
root.title("Digital Clock")
root.geometry("400x400") #dimensions of the clock
root.config(bg="black")

# Create a label to display the time
clock_label = tkinter.Label(root, font=("Retro Gaming", 30 ), bg="black", fg = "white")  # Create a label with specific font size, colour
clock_label.pack(expand=True)  # Position the label in the window

# Initialize the clock by calling the update_time function
update_time()

# Start the main event loop
root.mainloop()
