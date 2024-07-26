import tkinter as tk

def on_enter(event):
    widget = event.widget
    index = widget.index('active')
    print(f"Mouse is over: {widget.get(index)}, Position: {index}")

root = tk.Tk()

listbox = tk.Listbox(root)
listbox.pack()

items = ["Item 1", "Item 2", "Item 3", "Item 4"]
for item in items:
    listbox.insert(tk.END, item)

listbox.bind('<Motion>', on_enter)

root.mainloop()
