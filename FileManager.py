import tkinter
from tkinter import filedialog
from tkinter import messagebox

class FileManager:

    TEXT_FILE_TYPES = "Text files"
    TEXT_EXTENTION = ".txt"


    def __init__(self, text_widget):
        self.text_widget = text_widget
        self.current_file_path = None

    def create_file(self, event=None):
        file_path = filedialog.asksaveasfilename(defaultextension=self.TEXT_EXTENTION, filetypes=[(self.TEXT_FILE_TYPES, "*.txt")])

        if file_path:
            try:
                with open(file_path, 'w') as f:
                    f.write("")
                messagebox.showinfo("Success",f"Created file: {file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not create file: {file_path} {e}")


    def open_file(self, event=None):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            self.current_file_path = file_path
            print(f"Selected file: {file_path}")
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                    self.text_widget.delete('1.0',tkinter.END)
                    self.text_widget.insert(tkinter.END, content)
            except Exception as e:
                    messagebox.showerror("Error", f"Couldn't read file: {e}")

    def save_file(self, event = None):
        if not self.current_file_path:
            self.current_file_path = filedialog.asksaveasfilename(defaultextension=self.TEXT_EXTENTION,
                                                             filetypes=[(self.TEXT_FILE_TYPES, "*.txt")])

        if self.current_file_path:
            try:
                content = self.text_widget.get("1.0", "end-1c")
                with open(self.current_file_path, 'w') as f:
                    f.write(content)
                messagebox.showinfo("Success",f"Saved file: {self.current_file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Could save file: {self.current_file_path} {e}")

    def clean_area(self, event=None):
        self.text_widget.delete('1.0', tkinter.END)
