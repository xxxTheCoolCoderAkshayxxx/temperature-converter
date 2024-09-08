from tkinter import *
import tkinter.font as f
root = Tk()
root.title("Tempurature converter")
root.geometry("350x250")

def conversion():
    celsius=celsiusBox.get()
    if(celsius.replace('.','',1).isdigit()):
        errorMessage.grid_forget()
        fahrenheit= (float(celsius)*9/5)+32
        answerLabel.config(text="Temp in fahrenheit: "+str(fahrenheit))
    else:
        errorMessage.grid(row=1,column=1)

head = Label(root,text="Celsius -> Fahrenheit",font=f.Font(size=20),fg="grey")
head.pack()

#creating frame
frame=Frame(root)
frame.pack(pady=20)

label1 = Label(frame,text="Enter the temp in celsius: ",font=f.Font(size=10),fg="black")
label1.grid(row=0,column=0)

celsiusBox = Entry(frame)
celsiusBox.grid(row=0,column=1)

errorMessage = Label(frame,text="Please enter the valid input",font=f.Font(size=8),fg="red")

answerLabel = Label(frame,font=f.Font(size=12))
answerLabel.grid(row=2,column=0,columnspan=2,pady=10)

convert = Button(frame,text="Convert",width=30,fg="black",bg="light green",bd=0,padx=20,pady=10,command=conversion)
convert.grid(row=3,column=0,columnspan=2,pady=10)

root.mainloop()

