**PDF to Speech Converter**

This is a simple Python GUI application that converts the text content of a PDF file to speech using the Voice RSS API. The application uses the `tkinter` library for the graphical user interface, `pyttsx3` for text-to-speech synthesis, `PyPDF2` for PDF file processing, and `requests` for making API calls.

**Features**

- Select a PDF file using the GUI.
- Extract text content from each page of the PDF.
- Convert text to speech using either the local text-to-speech engine (`pyttsx3`) or the Voice RSS API.
- Save the generated audio to a temporary file (`temp_audio.mp3`).

**Prerequisites**

- Python 3.x
- Install required libraries using: `pip install pyttsx3 PyPDF2 requests python-dotenv`

