from ast import operator
from tkinter import *
import tkinter as tk
import math as m

root=Tk()
root.title("CALCULATOR")    
root.resizable(0,0)


def click(char):
    global operator
    operator+=str(char)
    InputText.set(operator)

def Clearall():
    global operator
    operator=""
    InputText.set("")

def Deleteone():
    global operator
    text=operator[:-1]
    operator=text
    InputText.set(text)

def percent():
    global operator
    temp=str(eval(operator+'/100'))
    operator=temp
    InputText.set(temp)

def square():
    global operator
    if int(operator)>=0:
        temp = str(eval(operator+'**(1/2)'))
        operator = temp
    else:
        temp = "ERROR"
    InputText.set(temp)
    
def sin():
    global operator
    result=str(m.sin(m.radians(int(operator))))
    operator=result
    InputText.set(result)

def cos():
    global operator
    result=str(m.cos(m.radians(int(operator))))
    operator=result
    InputText.set(result)

def tan():
    global operator
    result=str(m.tan(m.radians(int(operator))))
    operator=result
    InputText.set(result)

def cot():
    global operator
    result=str(m.cot(m.radians(int(operator))))
    operator=result
    InputText.set(result)

def equal1():
    global operator
    temp=str(eval(operator))
    InputText.set(temp)
    operator=temp
   

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

def fact_func():
    global operator
    result = str(factorial(int(operator)))
    operator = result
    InputText.set(result)

operator=""
InputText=StringVar()


widget=Entry(root,font=("arial",20,'bold'),textvariable=InputText,bd=10,bg='navajo white').grid(columnspan=5,padx=0,pady=20)


#1
square1=Button(root,font=("arial",20,"bold"),fg="white",bg="PaleVioletRed1",text="\u00B2\u221A",command=square).grid(row=1,column=0,sticky="nsew")
e1=Button(root,font=("arial",20,"bold"),fg="white",bg="PaleVioletRed1",text="e",command=lambda:click(str(m.exp(1)))).grid(row=1,column=1,sticky="nsew")
fact1=Button(root,font=("arial",20,"bold"),fg="white",bg="PaleVioletRed1",text="x!",command=fact_func).grid(row=1,column=2,sticky="nsew")
divbutt=Button(root,font=("arial",20,"bold"),fg="white",bg="PaleVioletRed1",text="div",command=lambda:click('//')).grid(row=1,column=3,sticky="nsew")


#2
sin1=Button(root,font=("arial",20,"bold"),fg="white",bg="PaleVioletRed1",text="sin",command=sin).grid(row=2,column=0,sticky="nsew")
cos1=Button(root,font=("arial",20,"bold"),fg="white",bg="PaleVioletRed1",text="cos",command=cos).grid(row=2,column=1,sticky="nsew")
tan1=Button(root,font=("arial",20,"bold"),fg="white",bg="PaleVioletRed1",text="tan",command=tan).grid(row=2,column=2,sticky="nsew")
cot1=Button(root,font=("arial",20,"bold"),fg="white",bg="PaleVioletRed1",text="cot",command=cot).grid(row=2,column=3,sticky="nsew")


#3
secondpow=Button(root,font=("arial",20,"bold"),fg="white",bg="PaleVioletRed1",text="x\u00B2",command=lambda:click('**2')).grid(row=3,column=0,sticky="nsew")
thirdpow=Button(root,font=("arial",20,"bold"),fg="white",bg="PaleVioletRed1",text="x\u00B3",command=lambda:click('**3')).grid(row=3,column=1,sticky="nsew")
npow=Button(root,font=("arial",20,"bold"),fg="white",bg="PaleVioletRed1",text="x^n",command=lambda:click('**')).grid(row=3,column=2,sticky="nsew")
tens_pow=Button(root,font=("arial",20,"bold"),fg="white",bg="PaleVioletRed1",text="10^x",command=lambda:click('10**')).grid(row=3,column=3,sticky="nsew")


#4
pi1=Button(root,font=("arial",20,"bold"),fg="white",bg="PaleVioletRed1",text="pi",command=lambda:click(m.pi)).grid(row=4,column=0,sticky="nsew")
add=Button(root,font=("arial",20,"bold"),fg="white",bg="PaleVioletRed1",text="+",command=lambda:click('+')).grid(row=4,column=1,sticky="nsew")
sub=Button(root,font=("arial",20,"bold"),fg="white",bg="PaleVioletRed1",text="-",command=lambda:click('-')).grid(row=4,column=2,sticky="nsew")
mod1=Button(root,font=("arial",20,"bold"),fg="white",bg="PaleVioletRed1",text="mod",command=lambda:click('%')).grid(row=4,column=3,sticky="nsew")


#5
percentage = Button(root, font=("arial",20,"bold"),fg="white",bg="PaleVioletRed1", text='%',command=percent).grid(row=5, column=0, sticky="nsew")
mul=Button(root,font=("arial",20,"bold"),fg="white",bg="PaleVioletRed1",text="*",command=lambda:click('*')).grid(row=5,column=1,sticky="nsew")
div=Button(root,font=("arial",20,"bold"),fg="white",bg="PaleVioletRed1",text="/",command=lambda:click('/')).grid(row=5,column=2,sticky="nsew")
left_par = Button(root, font=("arial",20,"bold"),fg="white",bg="PaleVioletRed1", text='(',command=lambda:click('(')).grid(row=5, column=3, sticky="nsew") 


#6
button_7=Button(root,font=("arial",20,"bold"),fg="white",bg="Lightskyblue1",text="7",command=lambda:click('7')).grid(row=6,column=0,sticky="nsew")
button_8=Button(root,font=("arial",20,"bold"),fg="white",bg="Lightskyblue1",text="8",command=lambda:click('8')).grid(row=6,column=1,sticky="nsew")
button_9=Button(root,font=("arial",20,"bold"),fg="white",bg="Lightskyblue1",text="9",command=lambda:click('9')).grid(row=6,column=2,sticky="nsew")
right_par = Button(root, font=("arial",20,"bold"),fg="white",bg="PaleVioletRed1", text=')',command=lambda:click(')')).grid(row=6, column=3, sticky="nsew") 


#7
button_4=Button(root,font=("arial",20,"bold"),fg="white",bg="Lightskyblue1",text="4",command=lambda:click('4')).grid(row=7,column=0,sticky="nsew")
button_5=Button(root,font=("arial",20,"bold"),fg="white",bg="Lightskyblue1",text="5",command=lambda:click('5')).grid(row=7,column=1,sticky="nsew")
button_6=Button(root,font=("arial",20,"bold"),fg="white",bg="Lightskyblue1",text="6",command=lambda:click('6')).grid(row=7,column=2,sticky="nsew")
deleteone1=Button(root,font=("arial",20,"bold"),fg="white",bg="gray",text="DEL",command=Deleteone).grid(row=7,column=3,sticky="nsew")


#8
button_1=Button(root,font=("arial",20,"bold"),fg="white",bg="Lightskyblue1",text="1",command=lambda:click('1')).grid(row=8,column=0,sticky="nsew")
button_2=Button(root,font=("arial",20,"bold"),fg="white",bg="Lightskyblue1",text="2",command=lambda:click('2')).grid(row=8,column=1,sticky="nsew")
button_3=Button(root,font=("arial",20,"bold"),fg="white",bg="Lightskyblue1",text="3",command=lambda:click('3')).grid(row=8,column=2,sticky="nsew")
deleteall=Button(root,font=("arial",20,"bold"),fg="white",bg="gray",text="AC",command=Clearall).grid(row=8,column=3,sticky="nsew")

#9
button_0=Button(root,font=("arial",20,"bold"),fg="white",bg="Lightskyblue1",text="0",command=lambda:click('0')).grid(row=9,column=0,sticky="nsew")
point=Button(root,font=("arial",20,"bold"),fg="white",bg="Lightskyblue1",text=".",command=lambda:click('.')).grid(row=9,column=1,sticky="nsew")
equal=Button(root,font=("arial",20,"bold"),fg="white",bg="gray",text="=",command=equal1).grid(row=9,columnspan=2,column=2,sticky="nsew")

root.mainloop()


