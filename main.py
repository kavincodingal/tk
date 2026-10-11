import tkinter as tk
s=tk.Tk()
s.title("my app")
s.geometry("400x200")
def submit():
    name=e.get()
    print("your name is ",name)

l1=tk.Label(s,text="enter your name",font=("Arial",15),bg="lightblue",fg="white")
l1.pack(pady=10)
e=tk.Entry(s,width=30,font=("Arial",12))
e.pack(pady=10)
b=tk.Button(s,text="submit",command=submit)
b.pack(pady=10)

s.mainloop()