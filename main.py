from tkinter import Tk, Button, Label
import tkinter.messagebox as messagebox
from tkinter.ttk import Combobox
from tkinter.filedialog import asksaveasfilename, askopenfile
from gtts import gTTS
from gtts.tokenizer import Tokenizer,tokenizer_cases,symbols
from gtts.lang import tts_langs
import pdfplumber

file_path = None
file_lang = None

def convert_to_mp3(file_path, file_lang, save_path):
    try:
        with pdfplumber.open(file_path) as pdf:
            text = [page.extract_text() for page in pdf.pages]
        text = ''.join(text)

        symbols.ALL_PUNC = symbols.ALL_PUNC[:-1] + '–'
        punc_config = Tokenizer([
            tokenizer_cases.legacy_all_punctuation
        ]).run(
        tokenizer_func = punc_config).save(gTTS(text, lang=file_lang,ve_path))
        return True
    except:
        messagebox.showinfo('Error', 'Something went wrong')
        return False


def confirm():
    answer = messagebox.askyesno(title='Confirm', message=f"Convert {file_path} to MP3?")
    if answer:
        return True
    return False


def set_file_path():
    global file_path
    file_path = askopenfile(title="Select file", filetypes=[('PDF files', '*.pdf')]).name
    label.config(text=f'File loaded: {file_path}', fg='green')


def set_file_lang():
    global file_lang
    user_lang = dropdown_list.get()
    available_langs = list(tts_langs().items())
    for lang in available_langs:
        if lang[1] == user_lang:
            file_lang = lang[0]


def delete_file():
    global file_path
    file_path = None
    label.config(text='Any file was not loaded', fg='red')


def delete_lang():
    global file_lang
    file_lang = None


def main():
    set_file_lang()

    if file_path and file_lang:
        save_path = asksaveasfilename(defaultextension=".mp3", filetypes=[("mp3", "*.mp3")])
        if save_path and confirm():
            if convert_to_mp3(file_path, file_lang, save_path):
                messagebox.showinfo('Result', 'Success')
        else:
            delete_lang()
            messagebox.showinfo('Message', 'Saving process was interrupted')

    else:
        messagebox.showerror('Error', 'PDF file or file language were not selected')


root = Tk()
root.title('PDF to MP3 compiler')
root.minsize(width=400, height=200)

select_button = Button(text='Select PDF file', command=set_file_path)
select_button.pack()

delete_file_button = Button(text='Delete loaded file', command=delete_file)
delete_file_button.pack()

label = Label(root, text='Any file was not loaded', font=("Helvetica", 10), fg='red')
label.pack()

dropdown_list = Combobox(root, values=list(tts_langs().values()))
dropdown_list.current(11)
dropdown_list.pack()

compile_button = Button(text='Compile file to mp3', command=main)
compile_button.pack()

exit_button = Button(text='Stop code', command=root.destroy)
exit_button.pack()

if __name__ == '__main__':
    root.mainloop()
