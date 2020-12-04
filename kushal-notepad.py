from tkinter import *
from tkinter .messagebox import showinfo
from tkinter .filedialog import askopenfilename,asksaveasfilename
import os
root=Tk()
def undo_edit():
    Textarea.event_generate('<<Undo>>')
def cut_edit():
    Textarea.event_generate('<<Cut>>')
def copy_edit():
    Textarea.event_generate('<<Copy>>')
def paste_edit():
    Textarea.event_generate('<<Paste>>')
'''def delete_edit():
    pass'''
'''def select_edit():
    Textarea.event_generate('<<Sel>>')'''
def select_edit(event=None):
    Textarea.tag_add('sel', '1.0', 'end')
    return "break"
def new_file():
    global fil
    root.title('Untitled - Notepad')
    fil=None
    Textarea.delete(1.0,END)
def open_file():
    global fil
    fil=askopenfilename(defaultextension='.txt',
                         filetypes=[('All Files','*.*'),('Text Documents',
                                                '*.txt')])
    if fil=='':
        fil = None
    else:
        root.title(os.path.basename(fil)+'- Notepad')
        Textarea.delete(1.0,END)
        f=open(fil,'r')
        Textarea.insert(1.0,f.read())
        f.close()

def save_file():
    global fil
    if fil==None:
        fil=asksaveasfilename(initialfile='Untitled.txt',
                               defaultextension='.txt',
                               filetypes=[('All Files', '*.*'), ('Text Documents',
                                                                 '*.txt')]
                               )
        if fil=='':
            fil=None
        else:
            f=open(fil,'w')
            f.write(Textarea.get(1.0,END))
            f.close()
            root.title(os.path.basename(fil)+ '- Notepad')
            print('file saved')
    else:
        f = open(fil,'w')
        f.write(Textarea.get(1.0, END))
        f.close()
def about_help():
    showinfo('Notepad','Done by kaushal')
root.geometry('900x550')
root.config(background='black')
root.title('Untitled- Notepad')
#for textArea
Textarea=Text(root)
fil=None
Textarea.pack(expand=True,fill=BOTH)
menubar = Menu(root)
root.config(menu=menubar)
#scrollbar
Scroll=Scrollbar(Textarea)
Scroll.pack(side=RIGHT,fill=Y)
Scroll.config(command=Textarea.yview)
Textarea.config(yscrollcommand=Scroll.set)
#file sub-menu
file=Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=file)
file.add_command(label='New',command=new_file)
file.add_separator()
file.add_command(label='Open',command=open_file)
file.add_separator()
file.add_command(label='Save',command=save_file)
file.add_separator()
file.add_command(label='Exit',command=root.quit)
#edit sub-menu
edit=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Edit',menu=edit)
edit.add_command(label='Undo',command=undo_edit)
edit.add_separator()
edit.add_command(label='Cut',command=cut_edit)
edit.add_separator()
edit.add_command(label='Copy',command=copy_edit)
edit.add_separator()
edit.add_command(label='Paste',command=paste_edit)
edit.add_separator()
'''edit.add_command(label='Delete',command=delete_edit)
edit.add_separator()'''
edit.add_command(label='Select All',command=select_edit)
#help sub-menu
help=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=help)
help.add_command(label='About notepad',command=about_help)
root.mainloop()