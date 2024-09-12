import tkinter as tk
from tkinter import ttk


def add_task():
    new_task: str = task_entry.get()
    if new_task:
        active_listbox.insert(tk.END, new_task)
        task_entry.delete(0, tk.END)


def completed_task():
    active_task: tuple[int] = active_listbox.curselection()
    if active_task:
        completed_listbox.insert(tk.END, active_listbox.get(active_task[0]))
        active_listbox.delete(active_task[0])


def bin_task():
    selected_active: tuple[int] = active_listbox.curselection()
    selected_completed: tuple[int] = completed_listbox.curselection()
    if selected_active:
        bin_listbox.insert(tk.END, active_listbox.get(selected_active[0]))
        active_listbox.delete(selected_active[0])
    elif selected_completed:
        bin_listbox.insert(tk.END, completed_listbox.get(selected_completed[0]))
        completed_listbox.delete(selected_completed[0])


def clean_bin():
    bin_listbox.delete(0, tk.END)


# Задание стилей для виджетов
def apply_style():
    style = ttk.Style()

    style.theme_use('clam')
    style.theme_settings('clam', settings={
       'TFrame': {
            'configure': {
                'background': '#325050'
                }
             },
       'TButton': {
           'configure': {
                'borderwidth': '3',
                'relief': 'ridge',
                'font': ('Arial', 11),
                },
            'map': {
                'background': [('!active', '#333333'), ('active', '#404040')],
                'foreground': [('!active', '#A0A0A0'), ('active', '#FFFFFF')],
                }
            },
       'TLabel': {
            'configure': {
                'background': '#327070',
                'foreground': '#FFFFFF',
                'font': ('Arial', 12, 'bold')
                }
            },
       'TEntry': {
            'configure': {
                'background': '#333333',
                'fieldbackground': '#333333',
                'foreground': '#FFFFFF',
                'borderwidth': '3',
                'relief': 'flat'
            }
        }
    })


root: tk = tk.Tk()
root.geometry('960x355')
root.title('Отслеживание задач v 1.1')

apply_style()

frame: ttk = ttk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Добавление виджетов
active_label: ttk = ttk.Label(frame, text='Активные задачи')
active_label.place(x=88, y=10)

completed_label: ttk = ttk.Label(frame, text='Выполненные задачи')
completed_label.place(x=389, y=10)

bin_label: ttk = ttk.Label(frame, text='Корзина')
bin_label.place(x=764, y=10)

active_listbox: tk = tk.Listbox(frame, bg='#303535', fg='#FFFFFF', borderwidth='3', relief='flat', font=('Arial', 12, 'bold'))
active_listbox.place(x=10, y=40, width=300, height=200)

completed_listbox: tk = tk.Listbox(frame, bg='#303535', fg='#FFFFFF', borderwidth='3', relief='flat', font=('Arial', 12, 'bold'))
completed_listbox.place(x=330, y=40, width=300, height=200)

bin_listbox: tk = tk.Listbox(frame, bg='#303535', fg='#FFFFFF', borderwidth='3', relief='flat', font=('Arial', 12, 'bold'))
bin_listbox.place(x=650, y=40, width=300, height=200)

task_font: tuple[str, int] = ('Arial', 11)  # через стили в settings={} не работало не смог понять почему

task_entry = ttk.Entry(frame, font=task_font)
task_entry.place(x=170, y=260, width=410, height=35)

add_button: ttk = ttk.Button(frame, text='Добавить задачу ', command=add_task)
add_button.place(x=10, y=260, width=150, height=35)

completed_button: ttk = ttk.Button(frame, text='Задача выполнена', command=completed_task)
completed_button.place(x=10, y=305, width=150, height=35)

bin_button: ttk = ttk.Button(frame, text='Переместить в корзину', command=bin_task)
bin_button.place(x=170, y=305, width=200, height=35)

clean_button: ttk = ttk.Button(frame, text='Очистить корзину', command=clean_bin)
clean_button.place(x=380, y=305, width=200, height=35)

root.mainloop()