from queue import Empty
from re import S
import tkinter as tk


window = tk.Tk()
window.title("To Do List")
window.geometry("300x500")
window.config(bg="#8BD3E6")
window.resizable(0, 0)

# Make another file save the to do list, use dictioanry title key

old_lists_list = {}

with open("save.txt", "r") as f:
  saved_list = f.read().split("!@#")
  
  for save in range(1, len(saved_list), 2):

    title = saved_list[save]
    content_list_string = saved_list[save + 1]
    content_list_string = content_list_string.replace("'", "")
    content_list = content_list_string[1:len(content_list_string) - 1].split(", ")
    old_lists_list[title] = content_list


title = "Not named"
current_list = []


def back():
  back_button.grid(column=0, row=0)


def display_list(save=None, title=None):
  empty_old_list_text.grid_remove()
  load_button.grid_remove()
  old_lists.grid_remove()
  back_button.grid_remove()

  entry.delete(0, tk.END)
  entry_title.delete(0, tk.END)
  list.delete(0, tk.END)

  if save is not None:
    entry_title.insert(tk.END, title)
    for item in save:
      list.insert(tk.END, item)
      current_list.append(item)

  hide_options()
  back()
  entry_title.grid(row=1, column=0, columnspan=5)
  list.grid(row=2, column=0, columnspan=5)
  entry.grid(row=3, column=0, columnspan=5)
  submit_button.grid(row=4, column=0, columnspan=5)
  empty_new_list_text.grid(row=5)
  delete_button.grid(row=8, column=0, columnspan=2)
  save_button.grid(row=8, column=2, columnspan=2)



def old_lists_display():

  old_lists.delete(0, tk.END)


  with open("save.txt", "r") as f:
    saved_list = f.read().split("!@#")
    
    for save in range(1, len(saved_list), 2):

      title = saved_list[save]
      content_list_string = saved_list[save + 1]
      content_list_string = content_list_string.replace("'", "")
      content_list = content_list_string[1:len(content_list_string) - 1].split(", ")
      old_lists_list[title] = content_list

  hide_options()
  back()
  old_lists.grid(row=1, column=0, columnspan=5)
  empty_old_list_text.grid(row=2, column=0)
  load_button.grid(row=3, column=0, columnspan=5)
  
  for title in old_lists_list.keys():
    old_lists.insert(tk.END, title)


def save():
  global title
  

  with open("save.txt", "r") as f:  # Put this reused code in a func
    saved_list = f.read().split("!@#")
    
    for save in range(1, len(saved_list), 2):

      title = saved_list[save]
      content_list_string = saved_list[save + 1]
      content_list_string = content_list_string.replace("'", "")
      content_list = content_list_string[1:len(content_list_string) - 1].split(", ")
      old_lists_list[title] = content_list

  title = entry_title.get()

  print(current_list)
  print(title)


  if title in old_lists_list.keys():
    print(old_lists_list[title])
    if old_lists_list[title] == current_list:
      return None


  with open("save.txt", "a+") as f:
    print(f.read())
    print(title)
    f.write("!@#" + title + "!@#" + str(current_list))




def load():
  title_load = old_lists.get(tk.ANCHOR)
  save_load = old_lists_list[title_load]
  display_list(save_load, title_load)



def delete():
  item = list.get(tk.ANCHOR)
  print("Item deleted: " + item)
  list.delete(tk.ANCHOR)

  with open("save.txt", "r+") as f:
    original = f.read()
    new = original.replace("\'" + item + "\', ", "")

    if (original == new):
      new = original.replace("\'" + item + "\'", "")

    f.seek(0)
    f.write(new)
    f.truncate()
    print(original)
    print(new)
  
    


def insert():
  value = entry.get()
  current_list.append(str(len(current_list) + 1) + ")" + value)
  list.insert(tk.END, str(len(current_list)) + ") " + value)
  entry.delete(0, tk.END)


def hide_options():
  new_list_button.grid_remove()
  list_button.grid_remove()
  empty_1.grid_remove()
  empty_2.grid_remove()


def show_options():
  current_list.clear()
  empty_old_list_text.grid_remove()
  load_button.grid_remove()
  old_lists.grid_remove()
  back_button.grid_remove()
  empty_1.grid(row=0, column=0)
  new_list_button.grid(row=1, column=1)
  empty_2.grid(row=2, column=0)
  list_button.grid(row=3, column=1)
  empty_new_list_text.grid_remove()
  list.grid_remove()
  entry_title.grid_remove()
  entry.grid_remove()
  delete_button.grid_remove()
  submit_button.grid_remove()
  save_button.grid_remove()
  back_button.grid_remove()


old_lists = tk.Listbox(width=49, height=24)
load_button = tk.Button(command=lambda: load(), text="Load", width=20, height=2)
empty_old_list_text = tk.Label(bg="#8BD3E6", height=0)

empty_new_list_text = tk.Label(bg="#8BD3E6", height=2)
list = tk.Listbox(width=49, height=20)
entry_title = tk.Entry(text="Enter Title", width=25)
entry = tk.Entry(text="Enter Value", width=25)

delete_button = tk.Button(command=delete, text="Delete", width=15)
submit_button = tk.Button(command=insert, text="Submit", width=15)
save_button  = tk.Button(command=save, text="Save", width=20)
back_button = tk.Button(command=show_options, text="< Back", height=1, width=8)

empty_1 = tk.Label(bg = "#8BD3E6", height=6, width=4)
empty_1.grid(row=0, column=0)

new_list_button = tk.Button(command = lambda: display_list(), text="New List", width=30, height=5)
new_list_button.grid(row=1, column=1)

empty_2 = tk.Label(bg = "#8BD3E6", height=6, width=4)
empty_2.grid(row=2, column=0)


list_button = tk.Button(command = old_lists_display, text="Lists", width=30, height=5)
list_button.grid(row=3, column=1)


window.mainloop()