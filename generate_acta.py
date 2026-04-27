import tkinter as tk
from tkinter import filedialog
import docx

def select_input_file():
    root = tk.Tk()  # Create a Tkinter root window
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(title='Select Input Transcript File')
    return file_path


def select_output_file():
    root = tk.Tk()  # Create a Tkinter root window
    root.withdraw()  # Hide the root window
    file_path = filedialog.asksaveasfilename(defaultextension='.docx', title='Save Output DOCX File')
    return file_path


def extract_meeting_info(transcript):
    # Example implementation for extracting information
    # This is where you'll implement your logic for parsing the transcript
    meeting_info = "Extracted Meeting Information..."
    return meeting_info


def generate_docx(meeting_info, output_file):
    doc = docx.Document()
    doc.add_heading('Meeting Information', level=1)
    doc.add_paragraph(meeting_info)
    doc.save(output_file)


def main():
    input_file = select_input_file()
    output_file = select_output_file()
    if input_file:
        with open(input_file, 'r') as file:
            transcript = file.read()
            meeting_info = extract_meeting_info(transcript)
            generate_docx(meeting_info, output_file)

if __name__ == '__main__':
    main()