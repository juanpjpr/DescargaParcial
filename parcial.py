from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import ntpath




def root_path():
    # Infer the root path from the run file in the project root (e.g. manage.py)
    fn = getattr(sys.modules['__main__'], '__file__')
    root_path = os.path.abspath(os.path.dirname(fn))
    return root_path

path=root_path()
src=root_path()+"\_d.bat"
cofg= "notepad "+root_path()+"\_d.bat"

def agregar():
    dir = filedialog.askopenfilename(
        initialdir=path, title="Select file", filetypes=(("all files", "*.*"), ("DBF", "*.DBF")))
    print(dir)

    if ".DBF" in dir:
        iBox.insert(END, path_leaf(dir))
    if ".PAR" in dir:
        iBox.insert(END, path_leaf(dir))
    if ".class" in dir:
        fBox.insert(END, path_leaf(dir))
    
    crearArchivo()

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def delete():
    if iBox.curselection():
        iBox.delete(iBox.curselection())
    if fBox.curselection():
        fBox.delete(fBox.curselection())

    crearArchivo()


def ejecutarBat():
    os.startfile(src)

def config():
     os.system(cofg)

def crearArchivo():
    arch = open("d.dld", "w")
    arch.write("setdrive.i\n")
    print(iBox.size())
    
    for i in range(iBox.size()):
        arch.write('-i'+iBox.get(i)+'\n')

    arch.write("setdrive.f\n")

    for f in range(fBox.size()):
        arch.write('-i'+fBox.get(f)+'\n')

    arch.close()


def descargar():
    ejecutarBat()


window = Tk()
window.geometry('250x550')
window.title('Parcial')


I = Label(window, text='I:')
I.pack()


iBox = Listbox(window)
iBox.pack()


F = Label(window, text='F:')
F.pack()

fBox = Listbox(window)
fBox.pack()


# BOTONES
add = Button(window, text="Agregar", pady=8, width=20, command=agregar)
add.pack()
minus = Button(window, text="Eliminar", pady=8, width=20, command=delete)
minus.pack()
cfg = Button(window, text="Config", pady=8, width=20, command=config)
cfg.pack()
down = Button(window, text="Descargar", pady=8, width=20, command=descargar)
down.pack()


window.mainloop()
