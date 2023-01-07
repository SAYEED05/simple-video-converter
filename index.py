import ffmpeg

#Get source file and output filename from the user
input_file = input('Enter the name of the input file: ')

while not input_file:
    print('Input filename is not entered')
    input_file = input('Enter the name of the input file: ')


output_file = input('Enter the name of the output file: ')

while not output_file:
    print('Output filename is not entered')
    input_file = input('Enter the name of the input file: ')


try:
    # Run the conversion
     ffmpeg.input(input_file).output(output_file,acodec='copy',vcodec='copy').run()
except ffmpeg.Error as e:
    # Print an error message
    print(f'\033[0;31m Error: {e}')
else:
    # Print a success message
    print("\033[1;32m Conversion complete!  \n")
