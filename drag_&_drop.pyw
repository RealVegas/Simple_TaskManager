# Полная версия drag and drop
# Позволяет как изменять положение элементов внутри одного Listbox'а,
# так и перемещать их между Listbox'ами

import tkinter as tk


def on_drag_start(event):
    widget = event.widget
    widget.start_index = widget.nearest(event.y)
    widget.drag_data = widget.get(widget.start_index)

    # Создаем временную метку для визуализации перемещения
    widget.drag_label = tk.Label(root, text=widget.drag_data, bg="lightgrey")
    widget.drag_label.place(x=event.x_root - root.winfo_rootx(), y=event.y_root - root.winfo_rooty())


def on_drag_motion(event):
    widget = event.widget
    if hasattr(widget, 'drag_label'):
        widget.drag_label.place(x=event.x_root - root.winfo_rootx(), y=event.y_root - root.winfo_rooty())


def on_drag_release(event):
    widget = event.widget
    widget.drag_label.destroy()

    # Получаем целевой Listbox
    target_widget = event.widget.winfo_containing(event.x_root, event.y_root)
    # Получаем индекс целевого положения
    target_index = widget.nearest(event.y)

    if widget.start_index != target_index and target_widget == widget:
        element = widget.get(widget.start_index)
        widget.delete(widget.start_index)
        widget.insert(target_index, element)

    elif isinstance(target_widget, tk.Listbox) and target_widget != widget:
        widget.delete(widget.start_index)

        # Вставляем элемент в целевой Listbox
        target_widget.insert(tk.END, widget.drag_data)


root = tk.Tk()

listbox1 = tk.Listbox(root)
listbox1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

listbox2 = tk.Listbox(root)
listbox2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Заполнение Listbox для демонстрации
for item in ["Элемент 1", "Элемент 2", "Элемент 3", "Элемент 4", "Элемент 5"]:
    listbox1.insert(tk.END, item)

for item in ["Элемент 6", "Элемент 7", "Элемент 8", "Элемент 9", "Элемент 10"]:
    listbox2.insert(tk.END, item)

# Привязка событий к обоим Listbox
for listbox in [listbox1, listbox2]:
    listbox.bind('<Button-1>', on_drag_start)
    listbox.bind('<B1-Motion>', on_drag_motion)
    listbox.bind('<ButtonRelease-1>', on_drag_release)

root.mainloop()