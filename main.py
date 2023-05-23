import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import Shifrovanie


def save_position(event):

   with open("okno.txt", "w") as f:
       f.write(str(main_window.winfo_x())+' '+ str(main_window.winfo_y()))


def load_position():
    try:
        with open("okno.txt", "r") as f:
            t = f.read().split()
            position = int(t[0]),int(t[1])
            main_window.geometry("+%d+%d" % position)
    except FileNotFoundError:
        pass



def new_file():
    text_fild.delete('1.0',tk.END)


def open_file():
    file = tk.filedialog.askopenfilename(title='Выбор файла',filetypes=(('Текстовые документы (*.txt)','.txt'),
                                                                        ('Все файлы','*.*')))

    if file:
        text_fild.delete('1.0',tk.END)
        text = open(file,encoding='utf-8').read()
        text = Shifrovanie.CodeText(text,17,19)
        text_fild.insert('1.0',text)



def save_file():

    file = tk.filedialog.asksaveasfilename(filetypes=(('Текстовые документы (*.txt)', '.txt'),
                                                                         ('Все файлы', '*.*')))


    f = open(file,'w',encoding='utf-8')
    text = text_fild.get('1.0',tk.END)
    text = Shifrovanie.CodeText(text,17,19)
    f.write(text)
    f.close()


def exit_bloknot():
    exit = tk.messagebox.askokcancel('Выход','Вы точно хотите выйти?')
    if exit:
        main_window.destroy()

def about():
    '''Программа для прозрачного шифрования
    (с)Sidorov M.M, Russia,2023'''
    about_programm = tk.Toplevel()
    about_programm.geometry('400x200')
    about_programm.title('О программе')
    label_about = tk.Label(about_programm,text=about.__doc__).place(x=100,y=50)
    btn = tk.Button(about_programm,text='Закрыть',command=about_programm.destroy).place(x = 200, y = 90)
    about_programm.resizable(False, False)
    about_programm.focus()
    about_programm.grab_set()

def spravka_show():
    '''
    Приложение с графическим интерфейсом «Блокнот AmTCD» (файл приложения: AmTCD).
    Позволяет: создавать /открывать / сохранять зашифрованный тестовый файл,
    предусмотрены ввод и сохранение личного ключа, вывод не модальной формы
    «Справка» , вывод модальной формы
    «О программе».
    '''

    global fVisible

    def cmClose():
        global fVisible
        fVisible = False
        main_window.destroy()

    if fVisible: return 0
    fVisible = True
    spravka = tk.Toplevel()
    spravka.resizable(False,False)
    spravka.title("Справка")
    spravka.geometry("525x150")
    label_spravka = tk.Label(spravka, text=spravka_show.__doc__,justify='left').pack()
    btn = tk.Button(spravka, text='Закрыть', command=spravka.destroy).place(x=200, y=90)
    spravka.protocol('WM_DELETE_WINDOW', cmClose)


def copy():
    main_window.clipboard_clear()
    main_window.clipboard_append(string=text_fild.get('1.0',tk.END))

def paste():
    text_fild.insert(1.0,str(main_window.clipboard_get()))

def parametrs():

    def change_theme():
        if buff1.get() == 'Светлая':
            text_fild['bg'] = 'white'
            text_fild['fg'] = 'black'
            text_fild['insertbackground'] = 'black'
        elif buff1.get() == 'Темная':
            text_fild['bg'] = 'black'
            text_fild['fg'] = 'white'
            text_fild['insertbackground'] = 'white'


    parametr_window = tk.Toplevel()
    parametr_window.geometry('400x200')
    parametr_window.title('Параметры')
    label_1 = tk.Label(parametr_window, text='Выберите тему').place(x=0, y=10)
    themes = ['Светлая','Темная']
    buff1 = tk.StringVar(value='x')

    for i in range(len(themes)):
        tk.Radiobutton(parametr_window,text=themes[i], value=themes[i], variable=buff1).place(x=5, y = 30 * (i + 1))
    change_button = tk.Button(parametr_window,text='Выбрать тему', command= change_theme).place(x = 5, y = 90)

main_window = tk.Tk()
main_window.geometry("720x560")
load_position()
main_window.title('Текстовый редактор')
main_window.iconbitmap("znachok.ico")
main_window.attributes("")
menu_main = tk.Menu(main_window)
main_window.config(menu = menu_main)

f_text = tk.Frame(main_window)
f_text.pack(expand=1,fill=tk.BOTH)

text_fild = tk.Text(f_text,
                    padx=10,
                    pady=10,
                    wrap=tk.WORD,
                    spacing3=10
                    )
text_fild.pack(expand=1,fill=tk.BOTH,side=tk.LEFT)



#Файл
menu_file = tk.Menu(tearoff=False)
menu_main.add_cascade(label='Файл',menu=menu_file)
menu_file.add_command(label = 'Новый',command=new_file)
menu_file.add_command(label = 'Открыть',command=open_file)
menu_file.add_command(label = 'Сохранить как',command=save_file)
menu_file.add_separator()
menu_file.add_command(label='Выход',command=exit_bloknot)

#Правка
menu_pravka = tk.Menu(tearoff=False)
menu_main.add_cascade(label='Правка',menu=menu_pravka)
menu_pravka.add_command(label = 'Копировать',command=copy)
menu_pravka.add_command(label = 'Вставить',command=paste)
menu_pravka.add_separator()
menu_pravka.add_command(label='Параметры',command=parametrs)

#Справка
menu_spravka = tk.Menu(tearoff=False)
menu_main.add_cascade(label='Справка',menu=menu_spravka)
menu_spravka.add_command(label = 'Содержание',command=spravka_show)
menu_spravka.add_separator()
menu_spravka.add_command(label='О программе',command=about)

main_window.bind('<Destroy>',save_position)

fVisible = False


main_window.mainloop()
