import tkinter as tk
from tkinter import messagebox, filedialog
def show_selected():
    try:
        selection = listbox.get(listbox.curselection())
        messagebox.showinfo("Selection", f"You selected: {selection}")
    except tk.TclError:
        messagebox.showwarning("Warning", "Please select an item first!")

def open_file():
    file_path = filedialog.askopenfilename(title="Select a File", 
                                          filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        listbox.insert(tk.END, f"File: {file_path}")
root = tk.Tk()
root.title("Tkinter Widget Demo")
root.geometry("400x300")
menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Open File", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=file_menu)
root.config(menu=menubar)
mbtn = tk.Menubutton(root, text="Actions", relief=tk.RAISED)
mbtn.grid()
mbtn.menu = tk.Menu(mbtn, tearoff=0)
mbtn["menu"] = mbtn.menu
mbtn.menu.add_command(label="Show Selection", command=show_selected)
mbtn.pack(pady=5)
frame = tk.Frame(root)
frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
for i in range(1, 51):
    listbox.insert(tk.END, f"Item Number {i}")
root.mainloop()
