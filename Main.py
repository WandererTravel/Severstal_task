import tkinter
from tkinter import *
from tkinter import messagebox, filedialog
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter.font import *
from PIL import Image, ImageTk
import os


class Notepad:
    app = Tk()  # Создание окна
    Width = 400  # Ширина по умолчанию
    Height = 400  # Высота по умолчанию

    # Создаем текстовое поле
    text = Text(app)

    # Создаем полосу прокрутки
    scrollbar = Scrollbar(text)

    my_file = None
    my_image = None

    def new_file(self):  # Функция для создания нового файла
        self.app.title('Заметки  |  Без названия')
        self.my_file = None
        self.text.delete('1.0', END)  # Удаление данных, начиная с первой строки (строки 1.0) и до конца (END)

    def open_file(self):  # Функция для открытия существующего файла
        self.my_file = askopenfilename(defaultextension='.txt',
                                       filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt')])
        if self.my_file == '':
            self.my_file = None
        else:
            self.app.title('Заметки  |  ' + os.path.basename(self.my_file))
            self.text.delete('1.0', END)
            file = open(self.my_file, 'r')
            self.text.insert('1.0', file.read())
            file.close()

    def save_file(self):  # Функция для сохранения файла
        if self.my_file is None:  # Сохранить как новый файл
            self.my_file = asksaveasfilename(initialfile='Без названия.txt', defaultextension='.txt',
                                             filetypes=[('All Files', '*.*'), ('Text Documents', '*.txt'),
                                                        ('Документ Word', '*.docx'), ('Документ Word 97-2003', '*.doc'),
                                                        ('PDF', '*.pdf'), ('Веб-страница', '*.html')])
            if self.my_file == '':
                self.my_file = None
            else:
                file = open(self.my_file, 'w')
                file.write(self.text.get('1.0', END))
                file.close()
                self.app.title('Заметки  |  ' + os.path.basename(self.my_file))
                showinfo('Заметки', 'Файл сохранен')  # Вывод информации об успешном сохранении файла
        else:
            file = open(self.my_file, 'w')
            file.write(self.text.get('1.0', END))
            file.close()
            showinfo('Заметки', 'Файл сохранен')  # Вывод информации об успешном сохранении файла

    def remove_file(self):  # Функция для удаления файла
        os.remove(self.my_file)
        showinfo('Заметки', 'Файл удален')  # Вывод информации об успешном удалении файла из директории

    def arial_txt(self):
        font_example = Font(family='Arial')
        self.text.configure(font=font_example)

    def roman_txt(self):
        font_example = Font(family='Times New Roman')
        self.text.configure(font=font_example)

    def impact_txt(self):
        font_example = Font(family='Impact')
        self.text.configure(font=font_example)

    def bold_txt(self):
        font_example = Font(weight='bold')
        self.text.configure(font=font_example)

    def italic_txt(self):
        font_example = Font(slant='italic')
        self.text.configure(font=font_example)

    def lined_txt(self):
        font_example = Font(underline=True)
        self.text.configure(font=font_example)

    def size_1(self):
        font_example = Font(size=10)
        self.text.configure(font=font_example)

    def size_2(self):
        font_example = Font(size=20)
        self.text.configure(font=font_example)

    def size_3(self):
        font_example = Font(size=30)
        self.text.configure(font=font_example)

    def insert_image(self):
        image_file = filedialog.askopenfilename(filetypes=[('PNG Files', '*.png'), ('JPG Files', '*.jpg'),
                                                           ('JPEG Files', '*.jpeg')])
        image = ImageTk.PhotoImage(file=image_file)
        self.text.image_create(END, image=image)
        self.app.mainloop()

    def about_app(self):  # Функция для пунтка "Справка"
        showinfo('Заметки', 'Программа разработана на языке Python, с использованием библиотеки'
                            ' "tkinter" (Tk (Toolkit) interface), предназначенной для организации'
                            ' диалогов в программе с помощью оконного графического интерфейса.')

    def quit_app(self):  # Функция для выхода из приложения
        self.app.destroy()

    # Меню
    # Изменение цвета верхнего меню, судя по некоторым форумам, не работает на Windows и OSX
    menu_bar = Menu(app, bg='#001235', fg='white')
    file_menu = Menu(menu_bar, bg='#71ABFF', bd=5, fg='black')  # Цвет фона, толщина рамки, цвет шрифта
    edit_menu = Menu(menu_bar, bg='#71ABFF', bd=5, fg='black')
    txt_menu = Menu(edit_menu, bg='#71ABFF', bd=5, fg='black')
    font_menu = Menu(txt_menu, bg='#71ABFF', bd=5, fg='black')
    size_menu = Menu(txt_menu, bg='#71ABFF', bd=5, fg='black')
    insert_menu = Menu(edit_menu, bg='#71ABFF', bd=5, fg='black')
    information_menu = Menu(menu_bar, bg='#71ABFF', bd=5, fg='black')

    def __init__(self, **kwargs):

        # Окно
        self.app.title('Заметки  |  Начало работы')  # Заголовок окна
        if os.path.exists('Greetings.txt'):  # Если приветственный файл существует
            file = open('Greetings.txt', 'r')  # Открыть и прочитать файл с приветствием
        else:  # Если приветственный файл не существует
            file = open('Greetings.txt', 'w+')  # Создать приветственный файл
            file.write('Добро пожаловать!')
            file.close()
            file = open('Greetings.txt', 'r')  # Открыть и прочитать файл с приветствием
        self.text.insert('1.0', file.read())
        file.close()  # Закрыть файл

        try:
            self.Width = kwargs['width']  # Ширина окна
        except KeyError:
            pass

        try:
            self.Height = kwargs['height']  # Высота окна
        except KeyError:
            pass

        # Центрируем окно по ширине и высоте экрана
        screen_width = self.app.winfo_screenwidth()
        screen_height = self.app.winfo_screenheight()
        x = (screen_width / 2) - (self.Width / 2)  # Находим координату по вертикали
        y = (screen_height / 2) - (self.Height / 2)  # Находим координату по горизонтали

        # Определяем размеры и местоположение (параметры: ширина и высота окна, затем координаты на экране)
        self.app.geometry('%dx%d+%d+%d' % (self.Width, self.Height, x, y))

        # Делаем текстовую область подстраивающейся под окно
        self.app.grid_rowconfigure(0, weight=1)
        self.app.grid_columnconfigure(0, weight=1)

        # Конфигурация текстового поля: цвет фона, толщина рамки, цвет шрифта, цвет курсора вставки, перенос по словам
        self.text.configure(bg='#001030', bd=5, fg='white', insertbackground='white', wrap=WORD)

        # При помощи атрибута sticky метода grip растягиваем виджет на весь объем ячейки (по всем сторонам света)
        self.text.grid(sticky='nesw')

        # Упаковываем и автоматизируем скроллбар в правой части окна
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.scrollbar.config(command=self.text.yview)
        self.text.configure(yscrollcommand=self.scrollbar.set)

        # Основное каскадное меню "Файл"
        self.menu_bar.add_cascade(label='Файл', menu=self.file_menu)  # Создание каскадного (выпадающего) меню "Файл"
        self.file_menu.add_command(label='Создать', command=self.new_file)  # Создание пункта "Создать" в меню "Файл"
        self.file_menu.add_command(label='Открыть', command=self.open_file)  # Создание пункта "Открыть"
        self.file_menu.add_command(label='Сохранить', command=self.save_file)  # Создание пункта "Сохранить"
        self.file_menu.add_command(label='Удалить', command=self.remove_file)  # Создание пункта "Удалить"

        # Основное каскадное меню "Изменить"
        self.menu_bar.add_cascade(label='Изменить', menu=self.edit_menu)  # Создание каскадного меню "Изменить"
        self.edit_menu.add_cascade(label='Текст', menu=self.txt_menu)  # Создание каскадного меню "Текст"
        self.txt_menu.add_cascade(label='Шрифт', menu=self.font_menu)  # Создание каскадного меню "Кегль"
        self.font_menu.add_command(label='Arial', command=self.arial_txt)  # Создание пункта Arial
        self.font_menu.add_command(label='Times New Roman', command=self.roman_txt)  # Создание пункта Times New Roman
        self.font_menu.add_command(label='Impact', command=self.impact_txt)  # Создание пункта Impact
        self.txt_menu.add_command(label='Ж', command=self.bold_txt)  # Создание пункта Жирный
        self.txt_menu.add_command(label='К', command=self.italic_txt)  # Создание пункта Курсив
        self.txt_menu.add_command(label='Ч', command=self.lined_txt)  # Создание пункта Подчеркивание
        self.txt_menu.add_cascade(label='Кегль', menu=self.size_menu)  # Создание каскадного меню "Кегль"
        self.size_menu.add_command(label='10', command=self.size_1)  # Создание пункта для изменения размера шрифта
        self.size_menu.add_command(label='20', command=self.size_2)  # Создание пункта для изменения размера шрифта
        self.size_menu.add_command(label='30', command=self.size_3)  # Создание пункта для изменения размера шрифта
        self.edit_menu.add_cascade(label='Вставка', menu=self.insert_menu)  # Создание каскадного меню "Вставка"
        self.insert_menu.add_command(label='Вставить изображение',
                                     command=self.insert_image)  # Создание пункта для вставки изображений

        # Основное каскадное меню "Справка"
        self.menu_bar.add_cascade(label='Справка', menu=self.information_menu)  # Создание каскадного меню "Справка"
        self.information_menu.add_command(label='Справка', command=self.about_app)  # Создание пункта "Справка"
        self.information_menu.add_separator()  # Создание разделителя в меню "Справка"
        self.information_menu.add_command(label='Выход', command=self.quit_app)  # Создание пункта выхода из программы

        self.app.iconbitmap(default='notepad_icon.ico')

        self.app.config(menu=self.menu_bar)

    def run_app(self):  # Функция запуска приложения
        self.app.mainloop()  # Держим окно открытым


notepad = Notepad(width=1000, height=500)  # Задаём необходимый нам размер окна
notepad.run_app()
