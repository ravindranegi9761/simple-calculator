from tkinter import*
first_num=second_num=operator=None

ravi=Tk()
ravi.title("calculator by ravi")
ravi.configure(bg="black")


def click(digit):
    current=text_label["text"]
    new=current+str(digit)
    text_label.config(text=new)

def clear():
    text_label.config(text="")

def get_oprator(op):
    global first_num,operator
    first_num=int(text_label["text"])
    operator=op
    text_label.config(text="")

def get_result():
    global first_num,second_num,operator
    second_num=int(text_label["text"])
    if operator=="+":
        text_label.config(text=str(first_num+second_num))
    elif operator=="-":
        text_label.config(text=str(first_num-second_num))
    elif operator=="*":
        text_label.config(text=str(first_num*second_num))
    else:
        if second_num==0:
             text_label.config(text="error")
        else:
            text_label.config(text=str(first_num/second_num))



text_label=Label(ravi,text="",font=("arial",40,"bold"),bg="black",fg="white")
text_label.grid(row=0,column=1,columnspan=5,sticky="w")


button_1=Button(ravi,text="1",width=8,height=4,font=("arial",20,"bold"),bg="lightgreen",fg="white",command=lambda:click(1))
button_1.grid(row=3,column=1)
button_2=Button(ravi,text="2",width=8,height=4,font=("arial",20,"bold"),bg="lightgreen",fg="white",command=lambda:click(2))
button_2.grid(row=3,column=2)
button_3=Button(ravi,text="3",width=8,height=4,font=("arial",20,"bold"),bg="lightgreen",fg="white",command=lambda:click(3))
button_3.grid(row=3,column=3)
button_4=Button(ravi,text="4",width=8,height=4,font=("arial",20,"bold"),bg="lightgreen",fg="white",command=lambda:click(4))
button_4.grid(row=2,column=1)
button_5=Button(ravi,text="5",width=8,height=4,font=("arial",20,"bold"),bg="lightgreen",fg="white",command=lambda:click(5))
button_5.grid(row=2,column=2)
button_6=Button(ravi,text="6",width=8,height=4,font=("arial",20,"bold"),bg="lightgreen",fg="white",command=lambda:click(6))
button_6.grid(row=2,column=3)
button_7=Button(ravi,text="7",width=8,height=4,font=("arial",20,"bold"),bg="lightgreen",fg="white",command=lambda:click(7))
button_7.grid(row=1,column=1)
button_8=Button(ravi,text="8",width=8,height=4,font=("arial",20,"bold"),bg="lightgreen",fg="white",command=lambda:click(8))
button_8.grid(row=1,column=2)
button_9=Button(ravi,text="9",width=8,height=4,font=("arial",20,"bold"),bg="lightgreen",fg="white",command=lambda:click(9))
button_9.grid(row=1,column=3)
button_0=Button(ravi,text="0",width=8,height=4,font=("arial",20,"bold"),bg="lightgreen",fg="white",command=lambda:click(0))
button_0.grid(row=4,column=1)
clear_button=Button(ravi,text="C",width=8,height=4,font=("arial",20,"bold"),bg="lightgreen",fg="white",command=lambda:clear())
clear_button.grid(row=4,column=2)
equal=Button(ravi,text="=",width=8,height=4,font=("arial",20,"bold"),bg="lightgreen",fg="white",command=lambda:get_result())
equal.grid(row=4,column=3)
plus=Button(ravi,text="+",width=8,height=4,font=("arial",20,"bold"),bg="lightgreen",fg="white",command=lambda: get_oprator("+"))
plus.grid(row=1,column=4)
sub=Button(ravi,text="-",width=8,height=4,font=("arial",20,"bold"),bg="lightgreen",fg="white",command=lambda: get_oprator("-"))
sub.grid(row=2,column=4)
multi=Button(ravi,text="*",width=8,height=4,font=("arial",20,"bold"),bg="lightgreen",fg="white",command=lambda: get_oprator("*"))
multi.grid(row=3,column=4)
div=Button(ravi,text="/",width=8,height=4,font=("arial",20,"bold"),bg="lightgreen",fg="white",command=lambda: get_oprator("/"))
div.grid(row=4,column=4)








ravi.mainloop()
