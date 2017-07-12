from Tkinter import *

def calculator():
    result_Var.set()

root=Tk()
root.title('calculator !')
info=Label(root,text='hello world !',width=50)
info.grid(row=0,column=0,columnspan=2)
start_info=Label(root, text='date start:',width=20)
start_info.grid(row=1,column=0)
start_var=StringVar()
start_var.set()
start_Entry=Entry(root,width=30,textvariable=start_var)
start_Entry.grid(row=1,column=1)
end_info=Label(root, text='date end:',width=20)
end_info.grid(row=2,column=0)
end_var=StringVar()
end_var.set('2017.06.05')
end_Entry=Entry(root,width=30,textvariable=end_var)
end_Entry.grid(row=2,column=1)

submit_button=Button(text='count days',command=countit,width=50)
submit_button.grid(row=3,column=0,columnspan=2)
res_info=Label(root,text='total days',width=20)
res_info.grid(row=4,column=0)
result_Var=StringVar()
result_Entry=Entry(root,width=20,textvariable=result_Var,state='disabled')
result_Entry.grid(row=4,column=1)
result_Var2=StringVar()
result_Entry1=Entry(root,width=50,textvariable=result_Var2,state='disabled')
result_Entry1.grid(row=5,column=0,columnspan=2)

root.mainloop()