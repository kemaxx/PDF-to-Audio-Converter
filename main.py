# Import necessary libraries
from tkinter import *
from tkinter import filedialog
import pyttsx3
import PyPDF2
import requests
from dotenv import load_dotenv
import os

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Load environment variables from a .env file (requires python-dotenv library)
load_dotenv()

# Function to read and convert a PDF to speech
def read_pdf():
    # Ask the user to select a PDF file
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])

    # Open the selected PDF file for reading
    file = open(file_path, "rb")

    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(file)

    # Get the number of pages in the PDF
    no_of_pages = len(pdf_reader.pages)

    # Iterate through each page of the PDF
    for page_num in range(no_of_pages):
        page = pdf_reader.pages[page_num]

        # Extract text content from the page
        text = page.extract_text()

        # Using Python TTS engine (commented out)
        # engin.say(text)
        # engin.runAndWait()

        # Using Voice RSS API to convert text to speech
        params = {
            'key': os.environ.get("API_KEY"),  # Retrieve API key from environment variables
            'hl': "en-us",
            'v': 'Mary',  # Voice name (you can change this)
            'src': text  # Text content to be converted to speech
        }

        # Make a POST request to the Voice RSS API
        response = requests.post("http://api.voicerss.org/", data=params)

        # Save the audio content received from the API to a temporary audio file
        with open("temp_audio.mp3", "ab") as audio_file:
            audio_file.write(response.content)

    # Close the input PDF file
    file.close()

# Create the GUI window
window = Tk()
window.title("My PDF Reader")

# Add a label to the window
Label(window, text="WELCOME TO MY PDF READER").pack()

# Button to trigger PDF reading
Button(window, text="Read PDF", command=read_pdf).pack()

# Button to stop reading (text-to-speech engine)
Button(window, text="Stop Reading", command=engine.stop).pack()

# Start the GUI application and wait for user interactions
window.mainloop()
