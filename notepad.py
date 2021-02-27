from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
import webbrowser
import pyautogui



class NotePad:
    root = Tk()
    root.withdraw()

    def __init__(self):
        self.master = Toplevel(NotePad.root)
        self.mini_note()

    def mini_note(self):

        self.master.title('Untitled - Psarris\' Notepad')
        self.master.resizable(True, True)
        NotePad.root.iconbitmap('images__2_o5_2.ico')
        self.master.iconbitmap('images__2_o5_2.ico')
        self.master.geometry("650x550")
        self.master.option_add('*tearOff', False)
        self.master.configure(background='#FFFFFF')

        # frame_menu = ttk.Frame(self.master)
        menu = Menu(self.master)
        self.master.config(menu=menu)

        self.master.bind('<Control-n>', lambda e: self.new())
        self.master.bind('<Control-Shift-KeyPress-N>', lambda e: self.new_window())
        self.master.bind('<Control-p>', lambda e: self.open_file())
        self.master.bind('<Control-s>', lambda e: self.save_file())
        # self.master.bind('<Control-z>', lambda e: self.undo())
        self.master.bind('<Control-c>', lambda e: self.copy())
        self.master.bind('<Control-x>', lambda e: self.cut())
        # self.master.bind('<KeyPress-Delete>', lambda e: self.add_undo())
        self.master.bind('<Control-Shift-KeyPress-S>', lambda e: self.save_as_file())

        file = Menu(menu)
        menu.add_cascade(menu=file, label='File')
        file.add_command(label='New', command=self.new, accelerator="Ctrl N")
        file.add_command(label='New window', command=self.new_window, accelerator="Ctrl Shift N")

        file.add_command(label='Open', command=self.open_file, accelerator="Ctrl P")
        file.add_command(label='Save', command=self.save_file, accelerator="Ctrl S")
        file.add_command(label='Save as', command=self.save_as_file, accelerator="Ctrl Shift S")
        file.add_separator()
        file.add_command(label='Exit', command=self.exit_notepad)

        edit = Menu(menu)
        menu.add_cascade(menu=edit, label='Edit')
        # edit.add_command(label='Undo', command="", accelerator="Ctrl Z")
        # edit.add_separator()
        edit.add_command(label='Cut', command=self.cut, accelerator="Ctrl X")
        edit.add_command(label='Copy', command=self.copy, accelerator="Ctrl C")
        edit.add_command(label='Paste', command=self.paste, accelerator="Ctrl V")
        edit.add_separator()
        edit.add_command(label='Select all', command=self.select_all, accelerator="Ctrl A")

        format_ = Menu(menu)
        menu.add_cascade(menu=format_, label='Format')
        theme = Menu(format_)
        format_.add_cascade(menu=theme, label='Theme')
        theme.add_command(label='Dark', command=self.bg_dark)
        theme.add_command(label='Light', command=self.bg_light)
        format_.add_command(label='Font', command=self.import_)

        view = Menu(menu)
        menu.add_cascade(menu=view, label='View')
        zoom = Menu(view)
        view.add_cascade(menu=zoom, label='Zoom')
        zoom.add_command(label='Zoom in', command=self.zoom_in)
        zoom.add_command(label='Zoom out', command=self.zoom_out)

        help_ = Menu(menu)
        menu.add_cascade(menu=help_, label='Help')
        help_.add_command(label='Send Feedback', command=self.redirect)
        help_.add_separator()
        help_.add_command(label='About', command=self.redirect)

        frame_text = ttk.Frame(self.master)
        frame_text.pack(fill=BOTH, expand=True)
        self.text = Text(frame_text)
        self.scrollbar = ttk.Scrollbar(self.text, orient=VERTICAL, command=self.text.yview)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.text.config(yscrollcommand=self.scrollbar.set, font=('Arial', 10, 'normal'))
        self.text.pack(fill=BOTH, expand=True, pady=1)
        self.dirr = ''
        self.initial = ''
        self.ini = 10

        # footer
        label_frame = ttk.Frame(frame_text)
        label_frame.pack(anchor='e')
        self.line_count = ttk.Label(label_frame, text="Ln - 1, Col - 0", width=20)
        self.line_count.grid(row=0, column=0)
        word_count = ttk.Label(label_frame, text="100%", width=10)
        word_count.grid(row=0, column=1)
        self.crlf = ttk.Label(label_frame, text="WINDOWS (CRLF)", width=20)
        self.crlf.grid(row=0, column=2)
        encoding = ttk.Label(label_frame, text="UTF-8", width=10)
        encoding.grid(row=0, column=3)
        space = ttk.Label(label_frame, text="", width=10)
        space.grid(row=0, column=4)

        self.update_label()
        self.for_name = ''
        self.check_title()



        self.master.protocol("WM_DELETE_WINDOW", self.exit_notepad)

        NotePad.root.mainloop()

        # expendable

    # font box begins here
    def import_(self):
        font = Tk()
        self.parent = font

        self.parent.geometry('410x350')
        self.parent.title('Psarris\' Fonts')
        self.parent.iconbitmap(r'')
        self.parent.resizable(False, False)

        # variables
        self.sizee = 10
        self.stylee = 'normal'
        self.fontt = 'Arial'

        # font labels
        font_main = ttk.Label(self.parent, text='Fonts:')
        font_main.place(x=21, y=25)

        font_style = ttk.Label(self.parent, text='Style:')
        font_style.place(x=176, y=25)

        font_size = ttk.Label(self.parent, text='Size:')
        font_size.place(x=334, y=25)

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
        self.list_size.insert(1, '10')
        self.list_size.insert(2, '11')
        for i in range(12, 29):
            if i % 2 == 0:
                p = str(i)
                q = p
                self.list_size.insert(END, q)
        self.list_size.insert(END, '36')
        self.list_size.insert(END, '48')
        self.list_size.insert(END, '72')

        self.list_size.select_set(1)

        self.list_scroll2.place(x=375, y=46, anchor='n', height=116)
        self.list_size.yview_moveto('0.11')
        self.list_size.place(x=333, y=44, width=53, height=120)

        """
        add font to each inserted item
        """

        # sample label
        frames = ttk.Frame(self.parent, width=260, height=80, border=5, relief=SOLID)
        frames.place(x=255, y=190, anchor='n')

        frame = ttk.Frame(frames, width=250, height=66, border=5)
        frame.place(y=35, relx=0.5, rely=0.5, anchor='s')

        sample_label = ttk.Label(self.parent, text='Sample!')
        sample_label.place(x=170, y=191, anchor='center', height=20)

        self.sample_label1 = ttk.Label(frame, text='AaBbCc')
        self.sample_label1.place(relx=0.5, rely=0.5, anchor='center')

        # ok n cancel button (2)
        ok_button = ttk.Button(self.parent, text='ok', command=self.ok_)
        ok_button.place(x=220, y=300)
        cancel_button = ttk.Button(self.parent, text='cancel', command=self.cancel_)
        cancel_button.place(x=300, y=300)

        # bindings
        self.list_main.bind('<<ListboxSelect>>', lambda e: self.change_font())
        self.list_style.bind('<<ListboxSelect>>', lambda e: self.change_style())
        self.list_size.bind('<<ListboxSelect>>', lambda e: self.change_size())
        self.parent.bind('<Return>', lambda a: self.ok_())

        self.parent.protocol("WM_DELETE_WINDOW", self.cancel_)

        self.parent.mainloop()

        # function

    def change_font(self):
        x = self.list_main.curselection()
        self.fontt = self.list_main.get(x)
        self.text.config(font=(self.fontt, self.sizee, self.stylee))
        self.sample_label1.config(font=(self.fontt, self.sizee, self.stylee))
        # self.entry_main.delete(0, END)
        # if self.fontt == 'Arial (default)':
        #     self.entry_main.insert(0, 'Arial')
        # else:
        #     self.entry_main.insert(0, self.fontt)
        # self.entry_main.config(font=(self.fontt, 10))

    def change_style(self):
        x = self.list_style.curselection()
        self.stylee = self.list_style.get(x)
        self.text.config(font=(self.fontt, self.sizee, self.stylee))
        self.sample_label1.config(font=(self.fontt, self.sizee, self.stylee))

    def change_size(self):
        x = self.list_size.curselection()
        self.sizee = self.list_size.get(x)
        self.text.config(font=(self.fontt, self.sizee, self.stylee))
        self.sample_label1.config(font=(self.fontt, self.sizee, self.stylee))

    def cancel_(self):
        try:
            self.text.config(font=(self.default, self.default_, self.default__))
        except AttributeError:
            self.text.config(font=('Arial', 10, 'normal'))
        self.parent.destroy()

    def ok_(self):
        self.default = self.fontt
        self.default_ = self.sizee
        self.default__ = self.stylee
        self.parent.destroy()

    # main notepad begins here
    def bg_dark(self):
        self.text.config(background='black', foreground='white', insertbackground='white')

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
                if save_message == 'yes':
                    self.save_as_file()
                elif save_message == 'no':
                    pass
                else:
                    return None

    def save_as_file(self):
        save_file = filedialog.asksaveasfile(title='Save as file', mode='w', defaultextension='.txt',
                                             filetypes=(("All Files", "*.*"), ("Text Files", "*.txt"),))
        text_file = self.text.get(1.0, 'end-1c')
        saved_text_file = save_file.name
        file = open(saved_text_file, 'w')
        saved = file.write(text_file)
        self.initial = saved_text_file
        self.for_name = self.initial
        real_name = self.initial.split('/')
        name = real_name[len(real_name) - 1]
        names = name.split('.')[0]
        self.master.title(names + ' - Psarris\' Notepad')
        self.check_title()
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
            self.for_name = self.initial
            f = open(self.initial)
            texxt = f.read()
            self.text.delete(1.0, END)
            self.text.insert(1.0 + 1, texxt)
        else:
            self.e = open(self.dirr)
            if self.e.read() != self.text.get(1.0, 'end-1c'):
                save_message = messagebox.askyesnocancel(title="Notepad",
                                                         message='Do you want to save changes to this file?', icon='warning')
                if save_message == 'yes':
                    self.save_file()
                    self.dirr = ""
                elif save_message == 'no':
                    self.dirr = ""
                else:
                    return None
                file = filedialog.askopenfile()
                self.initial = file.name
                self.dirr = self.initial
                self.for_name = self.initial
                f = open(self.initial)
                texxt = f.read()
                self.text.delete(1.0, END)
                self.text.insert(1.0 + 1, texxt)
            else:
                self.dirr = ''
                file = filedialog.askopenfile()
                self.initial = file.name
                self.dirr = self.initial
                self.for_name = self.initial
                f = open(self.initial)
                texxt = f.read()
                self.text.delete(1.0, END)
                self.text.insert(1.0 + 1, texxt)
        real_name = self.initial.split('/')
        name = real_name[len(real_name)-1]
        names = name.split('.')[0]
        self.master.title(names + ' - Psarris\' Notepad')
        self.check_title()
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
                                                         message='Do you want to save this file?')
                if save_message == 'yes':
                    self.save_as_file()
                elif save_message == 'no':
                    pass
                else:
                    return None
        else:
            e = open(self.initial)
            if e.read() != self.text.get(1.0, 'end-1c'):
                save_message = messagebox.askyesnocancel(title="Notepad",
                                                         message='Do you want to save changes to this file?')
                if save_message == 'yes':
                    self.save_as_file()
                elif save_message == 'no':
                    pass
                else:
                    return None
            else:
                pass

    def exit_empty(self):
        try:
            if self.initial == '':
                if self.text.get(0.0, 'end-1c') == '':
                    pass
                if self.text.get(0.0, 'end-1c') != '':
                    save_message = messagebox.askyesnocancel(title="Notepad",
                                                             message='Do you want to save this file?')
                    if save_message == 'yes':
                        self.save_as_file()
                    elif save_message == 'no':
                        pass
                    else:
                        return None
            else:
                e = open(self.initial)
                if e.read() != self.text.get(1.0, 'end-1c'):
                    save_message = messagebox.askyesnocancel(title="Notepad",
                                                             message='Do you want to save changes to this file? :)')
                    if save_message == 'yes':
                        self.save_as_file()
                    elif save_message == 'no':
                        pass
                    else:
                        return None
                else:
                    pass
        except FileNotFoundError:
            save_message = messagebox.askyesnocancel(title="Notepad",
                                                     message='This file doesnt exist, do you \n want to save it? :)')
            if save_message == 'yes':
                self.save_as_file()
            elif save_message == 'no':
                pass
            else:
                return None

    def exit_notepad(self):
        self.exit_empty()
        self.master.destroy()

    def new_window(self):
        NotePad()

    # def add_undo(self):
    #     notes = []
    #     note = self.text.get(1.0, 'end-1c')
    #     if " " in note:
    #         for i in note.split(" "):
    #             notes.append(i)
    #     self.noted = notes[-1]
    #     self.index = self.text.index(tk.INSERT)
    #     print(self.index)
    #     print(self.noted)
    #
    # def undo(self):
    #     self.text.insert(float(self.index), self.noted)
    #     plus = float(len(self.noted))
    #     plus = float(self.index) + plus
    #     print(plus)
    #     # self.text.tag_add(SEL, self.index, str(plus))

    def cut(self):
        try:
            e = self.text.selection_get()
            self.index = self.text.index(tk.INSERT)

            # for clipboard
            self.master.clipboard_clear()
            self.master.clipboard_append(e)
            self.master.update()

            # in case of undo
            t = self.text.get(0.0, 'end-1c')
            self.text.delete(0.0, 'end-1c')
            p = t.replace(e, "")

            self.copy_string = e
            self.text.insert(END, p)
        except Exception as e:
            print(e)

    def copy(self):
        try:
            self.copy_string = self.text.selection_get()

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

    def select_all(self):
        pyautogui.hotkey('ctrl', 'a')

    def redirect(self):
        webbrowser.open('www.github.com/lord-psarris/tkinter_notepad/')

    def zoom_in(self):
        try:
            if 10 <= self.fontt <= 96:
                ini = self.sizee
                ini += 4
                self.sizee = ini
                self.text.config(font=(self.fontt, self.sizee, self.stylee))
            else:
                pass
        except AttributeError:
            self.ini += 4
            self.text.config(font=('Arial', self.ini, 'normal'))

    def zoom_out(self):
        try:
            if self.fontt >= 14 and self.fontt <= 96:
                ini = self.sizee
                ini -= 4
                self.sizee = ini
                self.text.config(font=(self.fontt, self.sizee, self.stylee))
                print('1')
            else:
                print('2')
                pass
        except AttributeError:
            if self.ini >= 14 and self.ini <= 96:
                self.ini -= 4
                print('3')
                self.text.config(font=('Arial', self.ini, 'normal'))
            else:
                print('4')
                pass

    def update_label(self):
        lines = int(self.text.index(tk.INSERT).split('.')[0])
        columns = int(self.text.index(tk.INSERT).split('.')[1])
        self.line_count.config(text=f"Ln - {lines}, Col - {columns}")
        self.line_count.after(100, self.update_label)

    def check_title(self):
        try:
            file = open(self.for_name, 'r')
            real_name = self.for_name.split('/')
            name = real_name[len(real_name) - 1]
            names = name.split('.')[0]
            file = file.read()
            while self.text.get(0.0, 'end-1c') != file:
                self.master.title('*' + names + ' - Psarris\' Notepad')
            self.crlf.after(500, self.check_title)
        except (FileNotFoundError, AttributeError):
            print('error')
            pass



if __name__ == "__main__":
    NotePad()
