### PDF-to-MP3 Converter

The **PDF-to-MP3 Converter** is a desktop application designed to convert PDF documents into MP3 audio files with text-to-speech narration. This project leverages the power of `Tkinter` for the user interface and `gTTS` (Google Text-to-Speech) for generating audio from text extracted from PDFs.

#### Features

- **User-Friendly Interface:** Built using `Tkinter`, the application offers a simple and intuitive GUI for easy navigation and operation.
- **PDF to Audio Conversion:** Extracts text from PDF documents and converts it into speech using `gTTS`.
- **Multiple Languages:** Supports a variety of languages for text-to-speech conversion.
- **Error Handling:** Includes error handling to inform users if something goes wrong during the conversion process.
- **File Management:** Allows users to select PDF files, choose the output language, and save the resulting MP3 file.

#### Technologies Used

- **Frontend:** Tkinter (Python)
- **Text Extraction:** pdfplumber (Python)
- **Text-to-Speech:** gTTS (Google Text-to-Speech)
- **File Dialogs:** tkinter.filedialog

#### How to Use

1. **Open the Application:** Launch the converter application by running the Python script.
2. **Select PDF:** Click on the "Select PDF file" button to choose the PDF file you want to convert.
3. **Choose Language:** Select the desired language from the dropdown list.
4. **Convert:** Click the "Compile file to mp3" button to start the conversion process.
5. **Save Output:** Specify the location and name for the output MP3 file.
6. **Success:** If the conversion is successful, a success message will be displayed.

#### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/pdf-to-mp3-converter.git
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python main.py
   ```
#### Screenshot
![PDF_converter](https://github.com/user-attachments/assets/df02d48c-6f8c-4c13-abb3-7933a03fe045)
