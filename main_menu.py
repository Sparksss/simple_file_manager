import tkinter as tk
from FileManager import FileManager

def close_app(event):
    root.quit()

root = tk.Tk()
root.title('File manager')
root.geometry("800x800")

text_widget = tk.Text(root)
file_manager = FileManager(text_widget)
text_widget.pack(expand=True, fill='both')

btn = tk.Button(root, bg="blue", fg="black")
btn['text'] = "Open file"
btn.bind("<Button-1>", file_manager.open_file)
btn.pack()

save_btn = tk.Button(root, bg="green", fg="white")
save_btn['text'] = "Save"
save_btn.bind("<Button-1>", file_manager.save_file)
save_btn.pack()

clean_btn = tk.Button(root, bg="lightblue", fg="black")
clean_btn['text'] = "Clean"
clean_btn.bind("<Button-1>", file_manager.clean_area)
clean_btn.pack()

root.mainloop()