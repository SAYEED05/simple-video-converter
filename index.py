import tkinter as tk
from tkinter import filedialog
import ffmpeg
import os

def convert():
    input_files = source_file_entry.get().split(';')

    while not input_files[0]:
        print('Input filename(s) are not entered')
        log_messages.insert(tk.END, 'Input filename(s) are not entered \n')
        return

    for input_file in input_files:
        try:
            # Get the input file's directory and file name without extension
            input_folder = os.path.dirname(input_file)
            file_name = os.path.splitext(os.path.basename(input_file))[0]
            output_file = os.path.join(input_folder, f'{file_name}.mp4')

            # Run the conversion
            ffmpeg.input(input_file).output(output_file, acodec='copy', vcodec='copy').run()
        except Exception as e:
            # Print an error message
            print(f'Error: {e}')
            log_messages.insert(tk.END, f'Error: {e} \n')
        else:
            # Print a success message
            print(f"Conversion of {input_file} complete!")
            log_messages.insert(tk.END, f"Conversion of {input_file} complete! \n")

def browse_files():
    file_paths = filedialog.askopenfilenames()
    if file_paths:
        formatted_paths = ';'.join(file_paths)
        source_file_entry.delete(0, tk.END)  # Clear any existing content
        source_file_entry.insert(tk.END, formatted_paths)

# Create the main window
window = tk.Tk()
window.title('ffmpeg - converter')
window.geometry('600x400')

# Create the label and entry widgets for the file input
source_file_label = tk.Label(window, text='Enter input filenames (separated by ;):')
source_file_entry = tk.Entry(window)

# Create the button widget for the file browser
source_file_location = tk.Button(window, text='Browse', command=browse_files)

# Create the button widget for printing the values
print_button = tk.Button(window, text='Convert', command=convert)

# Log the success and error messages
log_messages = tk.Text(window)

# Place the widgets in the layout
source_file_label.pack()
source_file_entry.pack()
source_file_location.pack()
print_button.pack()
log_messages.pack()

# Run the main loop
window.mainloop()
