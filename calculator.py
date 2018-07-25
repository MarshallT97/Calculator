from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import math

class calculator(Frame):
    def __init__(self):
        super().__init__()
        self.equation = StringVar()
        self.equation.set('0')
        self.blank = True
        self.operator = False
        self.oper_sign = ''
        self.signs = ['.','/','+','x','-','^']
        self.initUI()

    def initUI(self):
        self.master.title("Calculator")
        style = Style()
        style.theme_use('clam')
        self.centerWindow()

        zero = Button(self,text='0',command=self.zeroText)
        zero.grid(row=6,column=1)
        one = Button(self,text='1',command=self.oneText)
        one.grid(row=5,column=0)
        two = Button(self,text='2',command=self.twoText)
        two.grid(row=5,column=1)
        three = Button(self,text='3',command=self.threeText)
        three.grid(row=5,column=2)
        four = Button(self,text='4',command=self.fourText)
        four.grid(row=4,column=0)
        five = Button(self,text='5',command=self.fiveText)
        five.grid(row=4,column=1)
        six = Button(self,text='6',command=self.sixText)
        six.grid(row=4,column=2)
        seven = Button(self,text='7',command=self.sevenText)
        seven.grid(row=3,column=0)
        eight = Button(self,text='8',command=self.eightText)
        eight.grid(row=3,column=1)
        nine = Button(self,text='9',command=self.nineText)
        nine.grid(row=3,column=2)

        equalsign = Button(self,text='=',command=self.equal)
        equalsign.grid(row=6,column=3)
        add = Button(self,text='+',command=self.plusSign)
        add.grid(row=5,column=3)
        minus = Button(self,text='-',command=self.minusSign)
        minus.grid(row=4,column=3)
        multi = Button(self,text='X',command=self.multiplicationSign)
        multi.grid(row=3,column=3)
        div = Button(self,text='÷',command=self.divisonSign)
        div.grid(row=2,column=3)
        dec = Button(self,text='.',command=self.decimalSign)
        dec.grid(row=6,column=2)
        sign = Button(self,text='(-)',command=self.minusSign)
        sign.grid(row=6,column=0)
        back = Button(self,text=u'\u232B',command=self.backspace)
        back.grid(row=2,column=2)
        cls = Button(self,text='C',command=self.clear)
        cls.grid(row=2,column=1)
        exp = Button(self,text='^',command=self.powerSign)
        exp.grid(row=2,column=0)

        display = Entry(self,width=51,textvariable=self.equation,foreground='#000000',state='disable')
        display.grid(row=0,column=0,rowspan=2,columnspan=4)

        self.pack(fill=BOTH,expand=1)

    def centerWindow(self):
        width = 415
        height = 206
        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()
        x = (sw - width) / 2
        y = (sh - height) / 2
        self.master.geometry('{}x{}+{}+{}'.format(width,height,int(x),int(y)))

    def zeroText(self):
        if self.blank:
            self.blank = False
        else:
            self.equation.set('{}0'.format(self.equation.get()))
    def oneText(self):
        if self.blank:
            self.blank = False
            self.equation.set('1')
        else:
            self.equation.set('{}1'.format(self.equation.get()))
    def twoText(self):
        if self.blank:
            self.blank = False
            self.equation.set('2')
        else:
            self.equation.set('{}2'.format(self.equation.get()))
    def threeText(self):
        if self.blank:
            self.blank = False
            self.equation.set('3')
        else:
            self.equation.set('{}3'.format(self.equation.get()))
    def fourText(self):
        if self.blank:
            self.blank = False
            self.equation.set('4')
        else:
            self.equation.set('{}4'.format(self.equation.get()))
    def fiveText(self):
        if self.blank:
            self.blank = False
            self.equation.set('5')
        else:
            self.equation.set('{}5'.format(self.equation.get()))
    def sixText(self):
        if self.blank:
            self.blank = False
            self.equation.set('6')
        else:
            self.equation.set('{}6'.format(self.equation.get()))
    def sevenText(self):
        if self.blank:
            self.blank = False
            self.equation.set('7')
        else:
            self.equation.set('{}7'.format(self.equation.get()))
    def eightText(self):
        if self.blank:
            self.blank = False
            self.equation.set('8')
        else:
            self.equation.set('{}8'.format(self.equation.get()))
    def nineText(self):
        if self.blank:
            self.blank = False
            self.equation.set('9')
        else:
            self.equation.set('{}9'.format(self.equation.get()))

    def decimalSign(self):
        if self.equation.get().count('.') != 2:
            if self.equation.get().count('.') == 0:
                self.blank = False
                self.equation.set('{}.'.format(self.equation.get()))
            elif self.equation.get().count('.') == 1 and self.operator:
                self.blank = False
                self.equation.set('{}.'.format(self.equation.get()))
    def powerSign(self):
        if '^' not in self.equation.get() and not self.operator:
            self.operator = True
            self.oper_sign = '^'
            self.blank = False
            self.equation.set('{}^'.format(self.equation.get()))
    def minusSign(self):
        temp = self.equation.get()
        if temp == '0':
            self.blank = False
            self.equation.set('-')
        elif temp.count('-') != 2 and self.oper_sign != '^':
            if self.oper_sign == '' and temp[-1] != '.' and temp[-1] != '-':
                self.operator = True
                self.oper_sign = '-'
                self.equation.set('{}-'.format(self.equation.get()))
            elif temp[-1] == self.oper_sign:
                self.equation.set('{}-'.format(self.equation.get()))
    def plusSign(self):
        if '+' not in self.equation.get() and not self.operator:
            self.operator = True
            self.oper_sign = '+'
            self.blank = False
            self.equation.set('{}+'.format(self.equation.get()))
    def multiplicationSign(self):
        if 'x' not in self.equation.get() and not self.operator:
            self.operator = True
            self.blank = False
            self.oper_sign = 'x'
            self.equation.set('{}x'.format(self.equation.get()))
    def divisonSign(self):
        if '/' not in self.equation.get() and not self.operator:
            self.operator = True
            self.blank = False
            self.oper_sign = '/'
            self.equation.set('{}/'.format(self.equation.get()))

    def clear(self):
        self.blank = True
        self.operator = False
        self.oper_sign = ''
        self.equation.set('0')
    def backspace(self):
        temp = self.equation.get()
        if len(temp) == 1:
            self.blank = True
            self.equation.set('0')
        else:
            if temp[-1] in self.signs:
                self.operator = False
                self.oper_sign = ''
                self.equation.set(temp[:-1])
            else:
                self.equation.set(temp[:-1])
    def equal(self):
        if self.oper_sign == '':
            return
        tokens = self.equation.get().split(self.oper_sign)
        if tokens[1] == '':
            return
        if self.equation.get()[0] == '-' and self.oper_sign == '-':
            tokens[0] = '-{}'.format(tokens[0])
        tokens[0] = float(tokens[0])
        tokens[1] = float(tokens[1])

        if self.oper_sign == '+':
            self.operator = False
            self.oper_sign = ''
            self.equation.set(self.add(tokens))
        elif self.oper_sign == '-':
            self.operator = False
            self.oper_sign = ''
            self.equation.set(self.substraction(tokens))
        elif self.oper_sign == 'x':
            self.operator = False
            self.oper_sign = ''
            self.equation.set(self.mulitply(tokens))
        elif self.oper_sign == '/':
            self.operator = False
            self.oper_sign = ''
            if tokens[1] == 0:
                self.equation.set("Error: Dividing by zero")
            else:
                self.equation.set(self.divide(tokens))
        elif self.oper_sign == '^':
            self.blank = True
            self.operator = False
            self.oper_sign = ''
            self.equation.set(self.power(tokens))

    def add(self,equ):
        return equ[0] + equ[1]
    def mulitply(self,equ):
        return equ[0] * equ[1]
    def divide(self,equ):
        return equ[0] / equ[1]
    def power(self,equ):
        return pow(equ[0],equ[1])
    def substraction(self,equ):
        return equ[0] - equ[1]



def main():
    root = Tk()
    main = calculator()
    root.iconbitmap("calculator_icon.ico")
    root.resizable(0,0)
    root.mainloop()

if __name__ == '__main__':
    main()
