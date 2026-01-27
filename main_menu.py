import tkinter as tk
from tkinter import filedialog


def open_file_dialog(event):
    file_path = filedialog.askopenfilename(filetypes=[("Text files","*.txt")])
    print(f"Open a file with name: {file_path}")
    if file_path:
        print(f"Selected file: {file_path}")
        try:
            with open(file_path, 'r') as f:
                content = f.read()
                text_widget.delete('1.0', tk.END)
                text_widget.insert(tk.END, content)
        except Exception as e:
            print(f"Error reading file: {e}")



def clean_area(event):
    text_widget.delete('1.0', tk.END)

def close_app(event):
    root.quit()

root = tk.Tk()
root.title('File manager')
root.geometry("800x800")

btn = tk.Button(root, bg="blue", fg="black")
btn['text'] = "Open file"
btn.bind("<Button-1>", open_file_dialog)
btn.pack()

clean_btn = tk.Button(root, bg="lightblue", fg="black")
clean_btn['text'] = "Clean"
clean_btn.bind("<Button-1>", clean_area)
clean_btn.pack()

text_widget = tk.Text(root)
text_widget.pack(expand=True, fill='both')


root.mainloop()