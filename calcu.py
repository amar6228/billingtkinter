from tkinter import *

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_Input.set(operator)

def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""

def btnClear():
    global operator
    operator = ""
    text_Input.set("")

root=Tk()
root.geometry("450x300+100+50")

#root.wm_iconbitmap("calculator.ico")
root.title("Simple Calculator")

text_Input = StringVar()
operator = ""

f1=Frame(root,bg='green',bd=6,relief=RIDGE)
f1.pack(side=TOP)


#############################################Calculator###############################################################################
txtDisplay=Entry(f1,width=45,bg='white',bd=4,font=('arial',12,'bold'),justify=RIGHT,textvariable=text_Input)
txtDisplay.grid(row=0,column=0,columnspan=4,pady=1)
txtDisplay.insert(0,"0")

###########################################CALCULATOR BUTTONS################################################################################
btn7=Button(f1,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='7',
                        bg='light blue',command=lambda:btnClick(7)).grid(row=2,column=0)
btn8=Button(f1,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='8',
                        bg='light blue',command=lambda:btnClick(8)).grid(row=2,column=1)
btn9=Button(f1,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='9',
                        bg='light blue',command=lambda:btnClick(9)).grid(row=2,column=2)
btnAdd=Button(f1,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='+',
                        bg='light blue',command=lambda:btnClick('+')).grid(row=2,column=3)
###########################################CALCULATOR BUTTONS################################################################################
btn4=Button(f1,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='4',
                        bg='light blue',command=lambda:btnClick(4)).grid(row=3,column=0)
btn5=Button(f1,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='5',
                        bg='light blue',command=lambda:btnClick(5)).grid(row=3,column=1)
btn6=Button(f1,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='6',
                        bg='light blue',command=lambda:btnClick(6)).grid(row=3,column=2)
btnSub=Button(f1,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='-',
                        bg='light blue',command=lambda:btnClick('-')).grid(row=3,column=3)
###########################################CALCULATOR BUTTONS################################################################################
btn1=Button(f1,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='1',
                        bg='light blue',command=lambda:btnClick(1)).grid(row=4,column=0)
btn2=Button(f1,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='2',
                        bg='light blue',command=lambda:btnClick(2)).grid(row=4,column=1)
btn3=Button(f1,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='3',
                        bg='light blue',command=lambda:btnClick(3)).grid(row=4,column=2)
btnMulti=Button(f1,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='*',
                        bg='light blue',command=lambda:btnClick('*')).grid(row=4,column=3)
###########################################CALCULATOR BUTTONS################################################################################
btn0=Button(f1,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='0',
                        bg='light blue',command=lambda:btnClick(0)).grid(row=5,column=0)
btnClear=Button(f1,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='C',
                        bg='light blue',command=btnClear).grid(row=5,column=1)
btnEqual=Button(f1,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='=',
                        bg='light blue',command=btnEquals).grid(row=5,column=2)
btnDiv=Button(f1,padx=16,pady=1,bd=7,fg='black',font=('arial',16,'bold'),width=4,text='/',
                        bg='light blue',command=lambda:btnClick('/')).grid(row=5,column=3)

root.mainloop()