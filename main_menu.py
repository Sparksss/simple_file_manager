import tkinter as tk
from tkinter import filedialog

current_file_path = None

def open_file_dialog(event):
    global current_file_path
    file_path = filedialog.askopenfilename(filetypes=[("Text files","*.txt")])
    print(f"Open a file with name: {file_path}")
    if file_path:
        print(f"Selected file: {file_path}")
        current_file_path = file_path
        try:
            with open(file_path, 'r') as f:
                content = f.read()
                text_widget.delete('1.0', tk.END)
                text_widget.insert(tk.END, content)
        except Exception as e:
            print(f"Error reading file: {e}")


def save_file(event):
    global current_file_path
    if not current_file_path:
        current_file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])

    if current_file_path:
        try:
            content = text_widget.get("1.0", "end-1c")
            with open(current_file_path, 'w') as f:
                f.write(content)
            print(f"Saved file: {current_file_path}")
        except Exception as e:
            print(f"Saved file: {current_file_path}")


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

save_btn = tk.Button(root, bg="green", fg="white")
save_btn['text'] = "Save"
save_btn.bind("<Button-1>", save_file)
save_btn.pack()

clean_btn = tk.Button(root, bg="lightblue", fg="black")
clean_btn['text'] = "Clean"
clean_btn.bind("<Button-1>", clean_area)
clean_btn.pack()

text_widget = tk.Text(root)
text_widget.pack(expand=True, fill='both')


root.mainloop()