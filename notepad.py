from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk


class NotePad():
    root = Tk()
    root.withdraw()

    def __init__(self):
        self.fontt = NotePad.fontt

        self.master = Toplevel(NotePad.root)
        self.miniNote()

    def miniNote(self):

        self.master.title('Untitled - Psarris\' Notepad')
        self.master.resizable(True, True)
        self.master.iconbitmap(r'images__2_o5_2.ico')
        self.master.geometry("650x550")
        self.master.option_add('*tearOff', False)
        self.master.configure(background='#FFFFFF')

        self.frame_menu = ttk.Frame(self.master)
        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)

        self.master.bind('<Control-n>', lambda e: self.new())
        self.master.bind('<Control-Shift-KeyPress-N>', lambda e: self.new_window())
        self.master.bind('<Control-p>', lambda e: self.open_file())
        self.master.bind('<Control-s>', lambda e: self.save_file())
        self.master.bind('<Control-z>', lambda e: self.undo())
        self.master.bind('<KeyPress-Delete>', lambda e: self.add_undo())
        self.master.bind('<Control-Shift-KeyPress-S>', lambda e: self.save_as_file())

        self.file = Menu(self.menu)
        self.menu.add_cascade(menu=self.file, label='File')
        self.file.add_command(label='New', command=self.new, accelerator="Ctrl N")
        self.file.add_command(label='New window', command=self.new_window, accelerator="Ctrl Shift N")

        self.file.add_command(label='Open', command=self.open_file, accelerator="Ctrl P")
        self.file.add_command(label='Save', command=self.save_file, accelerator="Ctrl S")
        self.file.add_command(label='Save as', command=self.save_as_file, accelerator="Ctrl Shift S")
        self.file.add_separator()
        self.file.add_command(label='Exit', command=self.exit_notepad)

        self.edit = Menu(self.menu)
        self.menu.add_cascade(menu=self.edit, label='Edit')
        self.edit.add_command(label='Undo', command="", accelerator="Ctrl Z")
        self.edit.add_separator()
        self.edit.add_command(label='Cut', command=self.cut, accelerator="Ctrl X")
        self.edit.add_command(label='Copy', command=self.copy, accelerator="Ctrl C")
        self.edit.add_command(label='Paste', command=self.paste, accelerator="Ctrl V")
        self.edit.add_separator()
        self.edit.add_command(label='Select all', command=self.select_all, accelerator="Ctrl A")

        self.format = Menu(self.menu)
        self.menu.add_cascade(menu=self.format, label='Format')
        self.theme = Menu(self.format)
        self.format.add_cascade(menu=self.theme, label='Theme')
        self.theme.add_command(label='Dark', command=self.bg_dark)
        self.theme.add_command(label='Light', command=self.bg_light)
        self.format.add_command(label='Font', command=self.impot)

        self.view = Menu(self.menu)
        self.menu.add_cascade(menu=self.view, label='View')
        self.zoom = Menu(self.view)
        self.view.add_cascade(menu=self.zoom, label='Zoom')
        self.zoom.add_command(label='Zoom in', command="")
        self.zoom.add_command(label='Zoom out', command="")

        self.help = Menu(self.menu)
        self.menu.add_cascade(menu=self.help, label='Help')
        self.help.add_command(label='Help', command="")
        self.help.add_command(label='Send Feedback', command="")
        self.help.add_separator()
        self.help.add_command(label='About', command="")

        self.frame_text = ttk.Frame(self.master)
        self.frame_text.pack(fill=BOTH, expand=True)
        self.text = Text(self.frame_text)
        self.scrollbar = ttk.Scrollbar(self.text, orient=VERTICAL, command=self.text.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.text.config(yscrollcommand=self.scrollbar.set, font=(self.fontt, NotePad.sizee, NotePad.stylee))
        self.text.pack(fill=BOTH, expand=True, pady=1)
        self.dirr = ''
        self.initial = ''
        text = self.text

        """footer - five panes, 1 - , 2 - linecount, wordcount,3- %, 4 - windows crlf, 5 - encoding """
        # footer
        label = ttk.Label(self.frame_text, text="label ddd", width="50")
        label.pack()
        label1 = ttk.Label(self.frame_text, text="label ddd", width="50")
        label1.pack()
        label2 = ttk.Label(self.frame_text, text="label ddd", width="50")
        label2.pack()

        self.master.protocol("WM_DELETE_WINDOW", self.exit_notepad)

        NotePad.root.mainloop()

    def impot(self):
        FontBox()

    def bg_dark(self):
        # self.text.config(background='black', foreground='white', insertbackground='white')
        print(FontBox)

    def bg_light(self):
        self.text.config(background='white', foreground='black', insertbackground='black')

    def empty_string(self):
        if self.initial == '':
            if self.text.get(0.0, 'end-1c') == '':
                pass
            if self.text.get(0.0, 'end-1c') != '':
                print('afa!!!')
                save_message = messagebox.askyesnocancel(title="Notepad",
                                                         message='Do you want to save this file? :)')
                if save_message == True:
                    self.save_as_file()
                if save_message == False:
                    pass

    def save_as_file(self):
        save_file = filedialog.asksaveasfile(title='Save as file', mode='w', defaultextension='.txt',
                                             filetypes=(("All Files", "*.*"), ("Text Files", "*.txt"),))
        text_file = self.text.get(1.0, 'end-1c')
        saved_text_file = save_file.name
        file = open(saved_text_file, 'w')
        saved = file.write(text_file)
        self.initial = saved_text_file
        self.master.title(self.initial + '-Psarris\' Notepad')
        file.close()

    def save_file(self):
        try:
            file = open(self.initial, 'w')
            written = self.text.get(0.0, 'end-1c')
            filen = file.write(written)
            file.close()
        except NameError and FileNotFoundError:
            print('no file')
            self.save_as_file()

    def open_file(self):
        self.empty_string()
        if self.dirr == "":
            file = filedialog.askopenfile(title='open file',
                                          filetypes=(("All Files", "*.*"), ("Text Files", "*.txt"),))
            self.initial = file.name
            self.dirr = self.initial
            f = open(self.initial)
            texxt = f.read()
            self.text.delete(1.0, END)
            self.text.insert(1.0 + 1, texxt)
        else:
            self.e = open(self.dirr)
            if self.e.read() != self.text.get(1.0, 'end-1c'):
                save_message = messagebox.askyesnocancel(title="Notepad",
                                                         message='Do you want to save changes to this file?')
                if save_message:
                    self.save_file()
                    self.dirr = ""
                elif not save_message:
                    pass
                    self.dirr = ""
                print("hello")
                file = filedialog.askopenfile()
                self.initial = file.name
                self.dirr = self.initial
                f = open(self.initial)
                texxt = f.read()
                self.text.delete(1.0, END)
                self.text.insert(1.0 + 1, texxt)
            else:
                print('it works')
                self.dirr = ''
                file = filedialog.askopenfile()
                self.initial = file.name
                self.dirr = self.initial
                f = open(self.initial)
                texxt = f.read()
                self.text.delete(1.0, END)
                self.text.insert(1.0 + 1, texxt)
        self.master.title(self.initial + '-Psarris\' Notepad')
        file.close()

    def new(self):
        self.empty_string_new()
        self.text.delete(1.0, END)
        self.initial = ''
        self.dirr = ''
        self.master.title('Untitled - Psarris\' Notepad')
        print(self.initial)

    def empty_string_new(self):
        if self.initial == '':
            if self.text.get(0.0, 'end-1c') == '':
                pass
            if self.text.get(0.0, 'end-1c') != '':
                save_message = messagebox.askyesnocancel(title="Notepad",
                                                         message='Do you want to save this file? :)')
                if save_message:
                    self.save_as_file()
                if not save_message:
                    pass
        else:
            e = open(self.initial)
            if (e.read() != self.text.get(1.0, 'end-1c')):
                save_message = messagebox.askyesnocancel(title="Notepad",
                                                         message='Do you want to save changes to this file? :)')
                if save_message:
                    self.save_as_file()
                if not save_message:
                    pass
            else:
                pass

    def exit_empty(self):
        try:
            if self.initial == '':
                if self.text.get(0.0, 'end-1c') == '':
                    pass
                if self.text.get(0.0, 'end-1c') != '':
                    save_message = messagebox.askyesnocancel(title="Notepad",
                                                             message='Do you want to save this file? :)')
                    if save_message:
                        self.save_as_file()
                        pass
                    if not save_message:
                        pass
            else:
                e = open(self.initial)
                if e.read() != self.text.get(1.0, 'end-1c'):
                    save_message = messagebox.askyesnocancel(title="Notepad",
                                                             message='Do you want to save changes to this file? :)')
                    if save_message:
                        self.save_as_file()
                    if not save_message:
                        pass
                else:
                    pass
        except FileNotFoundError:
            save_message = messagebox.askyesnocancel(title="Notepad",
                                                     message='This file doesnt exist, do you \n want to save it? :)')
            if save_message:
                self.save_as_file()
            if not save_message:
                pass

    def exit_notepad(self):
        self.exit_empty()
        self.master.destroy()

    def new_window(self):
        NotePad()

    def add_undo(self):
        notes = []
        note = self.text.get(1.0, 'end-1c')
        for i in note.split(" "):
            notes.append(i)
        self.noted = notes[-1]
        print(self.noted)

    def undo(self):
        self.text.insert(END, self.noted)

    def cut(self):
        try:
            e = self.text.selection_get()
            index = self.text.index(tk.INSERT)

            # for clipboard
            self.master.clipboard_clear()
            self.master.clipboard_append(e)
            self.master.update()

            # in case of undo
            t = self.text.get(1.0, 'end-1c')
            p = t.replace(e, "")
            self.copy_string = p
            self.cut_list = [p, index]
            self.text.delete(1.0, 'end-1c')
            self.text.insert(END, p)
        except Exception as e:
            print(e)

    def copy(self):
        try:
            self.copy_string = self.text.selection_get()
            print(self.copy_string)
            print(self.text.index(tk.INSERT))

            # for clipboard
            self.master.clipboard_clear()
            self.master.clipboard_append(self.copy_string)
            self.master.update()
        except Exception as e:
            print(e)

    def paste(self):
        p = self.copy_string
        place = self.text.index(tk.INSERT)
        self.text.insert(place, p)

    def all(self):
        pass

    def select_all(self):
        self.text.tag_add(SEL, "1.0", END)
        self.text.mark_set(INSERT, "1.0")
        self.text.see(INSERT)


class FontBox(object):
    NotePad.fontt = 'Baskerville Old Face'
    NotePad.stylee = 'normal'
    NotePad.sizee = 10

    def __init__(self):
        font = Tk()
        self.parent = font

        self.parent.geometry('410x350')
        self.parent.title('Psarris\' Fonts')
        self.parent.iconbitmap(r'')
        self.parent.resizable(False, False)

        # variables
        self.sizee = 12
        self.stylee = 'normal'
        self.fontt = 'Arial'

        # font labels
        self.font_main = ttk.Label(self.parent, text='Fonts:')
        self.font_main.place(x=20, y=10)

        self.font_style = ttk.Label(self.parent, text='Style:')
        self.font_style.place(x=174, y=10)

        self.font_size = ttk.Label(self.parent, text='Size:')
        self.font_size.place(x=333, y=10)

        # entry boxes
        # entry box1
        self.entry_main = ttk.Entry(self.parent)
        self.entry_main.insert(0, self.fontt)
        self.entry_main.config(font=(self.fontt, 10))
        self.entry_main.place(x=21, y=25, width=148)

        # entry box2
        self.entry_style = ttk.Entry(self.parent)
        self.entry_style.insert(0, self.stylee)
        self.entry_style.config(font=(self.fontt, 10, self.stylee))
        self.entry_style.place(x=176, y=25, width=148)

        # entry box3
        self.entry_size = ttk.Entry(self.parent)
        self.entry_size.insert(0, 12)
        self.entry_size.config(font=('Arial', 8))
        self.entry_size.place(x=334, y=25, width=51)

        # listboxes (3)
        # .. listbox1
        self.list_main = Listbox(self.parent, height=6, exportselection=False, relief=SOLID)
        self.list_scroll = ttk.Scrollbar(self.parent, orient=VERTICAL, command=self.list_main.yview)
        self.list_main.config(yscrollcommand=self.list_scroll.set)

        self.list_main.insert(1, 'Algerian')
        self.list_main.insert(2, 'Arial (default)')
        self.list_main.insert(END, 'Arial Rounded MT', 'Arial Unicode MS')
        self.list_main.insert(END, 'Baskerville Old Face')
        self.list_main.insert(END, 'Brittanic')
        self.list_main.insert(END, 'Calibri')
        self.list_main.insert(END, 'Cooper')
        self.list_main.insert(END, 'Franklin Gothic')
        self.list_main.insert(END, 'Georgia')
        self.list_main.select_set(1)

        self.list_scroll.place(x=159, y=46, anchor='n', height=116)
        self.list_main.yview_moveto('0.11')
        self.list_main.place(x=20, y=44, height=120, width=150)

        # .. listbox2
        self.list_style = Listbox(self.parent, height=6, width=15, exportselection=False, relief=SOLID)
        self.list_scroll1 = ttk.Scrollbar(self.parent, orient=VERTICAL, command=self.list_style.yview)

        self.list_style.config(yscrollcommand=self.list_scroll1.set)
        self.list_style.insert(1, 'normal')
        self.list_style.insert(2, 'bold')
        self.list_style.insert(4, 'italic')
        self.list_style.insert(5, 'bold italic')

        self.list_style.select_set(0)

        self.list_scroll1.place(x=314, y=46, anchor='n', height=116)
        self.list_style.place(x=175, y=44, width=150, height=120)

        # .. listbox3
        self.list_size = Listbox(self.parent, height=6, width=9, relief=SOLID, exportselection=False)
        self.list_scroll2 = ttk.Scrollbar(self.parent, orient=VERTICAL, command=self.list_size.yview)
        self.list_size.config(yscrollcommand=self.list_scroll2.set)
        # 8, 11, 12- 28, 36, 48, 72
        self.list_size.insert(1, '8')
        self.list_size.insert(2, '11')
        for i in range(12, 29):
            if (i % 2 == 0):
                p = str(i)
                q = p
                self.list_size.insert(END, q)
        self.list_size.insert(END, '36')
        self.list_size.insert(END, '48')
        self.list_size.insert(END, '72')

        self.list_size.select_set(2)

        self.list_scroll2.place(x=375, y=46, anchor='n', height=116)
        self.list_size.yview_moveto('0.11')
        self.list_size.place(x=333, y=44, width=53, height=120)

        """
        add font to each inserted item
        """

        # sample label
        self.frames = ttk.Frame(self.parent, width=260, height=80, border=5, relief=SOLID)
        self.frames.place(x=255, y=190, anchor='n')

        self.frame = ttk.Frame(self.frames, width=250, height=66, border=5)
        self.frame.place(y=35, relx=0.5, rely=0.5, anchor='s')

        self.sample_label = ttk.Label(self.parent, text='Sample!')
        self.sample_label.place(x=170, y=191, anchor='center', height=20)

        self.sample_label1 = ttk.Label(self.frame, text='AaBbCc')
        self.sample_label1.place(relx=0.5, rely=0.5, anchor='center')

        # ok n cancel button (2)
        self.ok_button = ttk.Button(self.parent, text='ok', command=self.ok_)
        self.ok_button.place(x=220, y=300)
        self.cancel_button = ttk.Button(self.parent, text='cancel', command=self.cancel_)
        self.cancel_button.place(x=300, y=300)

        # bindings
        self.list_main.bind('<<ListboxSelect>>', lambda e: self.changeFont())
        self.list_style.bind('<<ListboxSelect>>', lambda e: self.changeStyle())
        self.list_size.bind('<<ListboxSelect>>', lambda e: self.changeSize())
        self.parent.bind('<Return>', lambda a: self.cancel_())

        self.parent.mainloop()

    # function
    def changeFont(self):
        x = self.list_main.curselection()
        self.fontt = self.list_main.get(x)
        self.sample_label1.config(font=(self.fontt, self.sizee, self.stylee))
        self.entry_main.delete(0, END)
        if self.fontt == 'Arial (default)':
            self.entry_main.insert(0, 'Arial')
        else:
            self.entry_main.insert(0, self.fontt)
        self.entry_main.config(font=(self.fontt, 10))

    def changeStyle(self):
        x = self.list_style.curselection()
        self.stylee = self.list_style.get(x)
        self.sample_label1.config(font=(self.fontt, self.sizee, self.stylee))
        self.entry_style.delete(0, END)
        self.entry_style.insert(0, self.stylee)
        self.entry_style.config(font=(self.fontt, 10, self.stylee))

    def changeSize(self):
        x = self.list_size.curselection()
        self.sizee = self.list_size.get(x)
        self.sample_label1.config(font=(self.fontt, self.sizee, self.stylee))
        self.entry_size.delete(0, END)
        self.entry_size.insert(0, self.sizee)
        self.entry_size.config(font=('Arial', 8))

    def cancel_(self):
        self.parent.destroy()

    def ok_(self):
        self.parent.destroy()


if __name__ == "__main__":
    NotePad()
