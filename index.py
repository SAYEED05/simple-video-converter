import tkinter as tk
from tkinter import filedialog
import ffmpeg

def convert():
    input_file = source_file_entry.get()

    while not input_file:
        print('Input filename is not entered \n')
        log_messages.insert(tk.END,'Input filename is not entered \n')
    output_file =output_file_entry.get()

    while not output_file:
        print('Output filename is not entered')
        log_messages.insert(tk.END,'Output filename is not entered \n')


    try:
        # Run the conversion
        ffmpeg.input(input_file).output(output_file,acodec='copy',vcodec='copy').run()
    except ffmpeg.Error as e:
        # Print an error message
        print(f'\033[0;31m Error: {e}')
        log_messages.insert(tk.END,f'\033[0;31m Error: {e} \n')
    else:
        # Print a success message
        print("\033[1;32m Conversion complete!  \n")
        log_messages.insert(tk.END,"\033[1;32m Conversion complete!  \n")

# Create the main window
window = tk.Tk()
window.title('ffmpeg - converter')
window.geometry('400x400')

# Create the label and entry widgets for the file input
source_file_label = tk.Label(window, text='Select a file:')
source_file_entry = tk.Entry(window)
# Create the button widget for the file browser
source_file_location = tk.Button(window, text='Browse', command=lambda: source_file_entry.insert(0, filedialog.askopenfilename()))

# Create the label and entry widgets for the second input
output_file_label = tk.Label(window, text='Enter Output Filename with format (Eg:output.mp4):')
output_file_entry = tk.Entry(window)

# Create the button widget for printing the values
print_button = tk.Button(window, text='Convert', command=convert)

# Log the success and error messages
log_messages = tk.Text(window)

# Place the widgets in the layout
source_file_label.pack()
source_file_entry.pack()
source_file_location.pack()
output_file_label.pack()
output_file_entry.pack()
print_button.pack()
log_messages.pack()

# Run the main loop
window.mainloop()




