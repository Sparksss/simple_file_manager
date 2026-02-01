import tkinter as tk
from FileManager import FileManager


RIGHT_CLICK = "<Button-1>"

def close_app(event):
    root.quit()

root = tk.Tk()
root.title('File manager')
root.geometry("800x800")

def toggle_sidebar():
    if sidebar.winfo_viewable():
        sidebar.pack_forget()
    else:
        sidebar.pack(side=tk.LEFT, fill=tk.Y, before=content_frame)

# Create a narrow bar (Activity Bar) to hold the toggle button
activity_bar = tk.Frame(root, bg="#333", width=50)
activity_bar.pack(side=tk.LEFT, fill=tk.Y)

tk.Button(activity_bar, text="≡", command=toggle_sidebar, bg="#333", fg="white", bd=0, font=("Arial", 15)).pack(pady=10)

# Create a sidebar frame for the menu items
sidebar = tk.Frame(root, bg="lightgray", width=200)
sidebar.pack(side=tk.LEFT, fill=tk.Y)

# Create a frame for the main content area
content_frame = tk.Frame(root)
content_frame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

text_widget = tk.Text(content_frame)
file_manager = FileManager(text_widget)
text_widget.pack(expand=True, fill='both')

btn = tk.Button(sidebar, bg="blue", fg="black")
btn['text'] = "Open file"
btn.bind(RIGHT_CLICK, file_manager.open_file)
btn.pack(fill=tk.X, padx=5, pady=5)

save_btn = tk.Button(sidebar, bg="green", fg="white")
save_btn['text'] = "Save"
save_btn.bind(RIGHT_CLICK, file_manager.save_file)
save_btn.pack(fill=tk.X, padx=5, pady=5)

clean_btn = tk.Button(sidebar, bg="lightblue", fg="black")
clean_btn['text'] = "Clean"
clean_btn.bind(RIGHT_CLICK, file_manager.clean_area)
clean_btn.pack(fill=tk.X, padx=5, pady=5)

m = tk.Menubutton(sidebar, text="File", relief=tk.RAISED)

cm = tk.Menu(m, tearoff=0)
m['menu'] = cm
cm.add_command(label="Open", command=lambda: file_manager.open_file(None))
cm.add_command(label="Save", command=lambda: file_manager.save_file(None))
cm.add_command(label="Delete", command=lambda: file_manager.delete_file(None))
cm.add_separator()
cm.add_command(label="Exit", command=root.quit)
m.pack(anchor='nw', fill=tk.X, padx=5, pady=5)

root.mainloop()