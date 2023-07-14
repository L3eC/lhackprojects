import tkinter as tk

window = tk.Tk()
greeting = tk.Label(text="Hello Again, World!")
greeting.grid(row=1,column=1)
txt_test = tk.Text(height=10,relief="sunken")
txt_test.grid(row=2,column=1)
txt_test2 = tk.Text(height=10,relief="sunken")
txt_test.grid(row=3,column=1)
window.mainloop()