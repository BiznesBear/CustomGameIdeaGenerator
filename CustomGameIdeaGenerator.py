from data import *
import random,sys
import tkinter as tk
from tkinter import filedialog,simpledialog,messagebox
types_amount = 1
themes_amount = 1
goals_amount = 1

type = ""
theme = ""
dimension = ""
goal = ""
result = ""


background_color = False
text_color = False

def ResetAll():
    global background_color,types_amount, themes_amount, goals_amount,text_color
    background_color = False
    text_color = True
    types_amount = 1
    themes_amount = 1
    goals_amount = 1

def toggle_background():
    global background_color
    background_color = not background_color

def toggle_text():
    global text_color
    text_color = not text_color

def random_color(min:int,max:int,full_color:bool):
    # Generuj losowy kolor w formacie '#RRGGBB' (szesnastkowy)
    if not full_color:
        colour = random.randint(min, max)
        return f"#{colour:02X}{colour:02X}{colour:02X}"
    else:
        return f"#{random.randint(10, 222):02X}{random.randint(10, 222):02X}{random.randint(10, 222):02X}"
    #return f"#{random.randint(23, 212):02X}{random.randint(23, 212):02X}{random.randint(23, 212):02X}"
    

        

def update_variable(var_name, var_value):
    global types_amount, themes_amount, goals_amount
    if var_name == "Types":
        types_amount = var_value
    elif var_name == "Themes":
        themes_amount = var_value
    elif var_name == "Goals":
        goals_amount = var_value

def show_variables():
    global types_amount, themes_amount, goals_amount
    message = f"Types={types_amount}, Themes={themes_amount}, Goals={goals_amount}"
    messagebox.showinfo("Current settings", message)

def update_var1():
    new_var_value = simpledialog.askinteger("Settings", "New game types amount in:", initialvalue=types_amount)
    if new_var_value is not None:
        update_variable("Types", new_var_value)

def update_var2():
    new_var_value = simpledialog.askinteger("Settings", "New game themes amount in:", initialvalue=themes_amount)
    if new_var_value is not None:
        update_variable("Themes", new_var_value)

def update_var3():
    new_var_value = simpledialog.askinteger("Settings", "New game goals amount in:", initialvalue=goals_amount)
    if new_var_value is not None:
        update_variable("Goals", new_var_value)

def delete_selected_item(event):
    selected_item_index = ideasList.curselection()
    if selected_item_index:
        ideasList.delete(selected_item_index)

def Clear():
    ideasList.delete(0, tk.END)

def Save():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"),("All", "*")],initialfile="ideas.txt")
    if file_path:
        with open(file_path, "w") as file:
            for item in ideasList.get(0, tk.END):
                file.write(item + "\n")


def Generate50():
    for i in range(0,50):
        GenerateIdea()

def Generate20():
    for i in range(0,20):
        GenerateIdea()

def Generate5():
    for i in range(0,5):
        GenerateIdea()

def GenerateIdea():
    dimension = random.choice(game_dimension)
    type= random.choices(game_types,k=types_amount)
    theme = random.choices(game_themes,k=themes_amount) 
    goal = random.choices(game_goals,k=goals_amount)

    type_str = ', '.join(type)
    theme_str = ', '.join(theme)
    goal_str = ' and '.join(goal)

    result = (f"{dimension} {type_str} game about {theme_str} were the goal is {goal_str}")
    #print(result)
    ideasList.insert(tk.END,result)
    if not text_color:
        ideasList.itemconfig(tk.END,{'fg': random_color(50,140,True)})
    else:
        ideasList.itemconfig(tk.END,{'fg': random_color(0,0,False)})
    if not background_color:
        ideasList.itemconfig(tk.END,{'bg': random_color(255,255,False)})
    else:
        ideasList.itemconfig(tk.END,{'bg': random_color(30,222,True)})
    root.update()    

    
root = tk.Tk()
root.geometry("900x600")
root.title("Custom Game Idea Generator")
root.iconbitmap(sys.argv[0])

menubar = tk.Menu(root,font=11)
root.config(menu=menubar)
list_menu = tk.Menu(menubar, tearoff=0)
file_menu = tk.Menu(menubar, tearoff=0)

file_menu.add_command(label="Clear", command=Clear)
file_menu.add_command(label="Save", command=Save)

settings_menu = tk.Menu(menubar, tearoff=0)

# Dodawanie opcji do menu "List"
list_menu.add_command(label="Generate", command=GenerateIdea)
list_menu.add_command(label="Generate 5", command=Generate5)
list_menu.add_command(label="Generate 20", command=Generate20)
list_menu.add_command(label="Generate 50", command=Generate50)

menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="List", menu=list_menu)
menubar.add_cascade(label="Settings", menu=settings_menu)


scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

ideasList = tk.Listbox(root,yscrollcommand=scrollbar.set,font=9)
ideasList.pack(side="top",fill=tk.BOTH, expand=True)
ideasList.bind("<Delete>", delete_selected_item)

scrollbar.config(command=ideasList.yview)

settings_menu.add_command(label="Set game types in", command=update_var1)
settings_menu.add_command(label="Set game themes in", command=update_var2)
settings_menu.add_command(label="Set game goals in", command=update_var3)
settings_menu.add_separator()
settings_menu.add_command(label="Show current setting", command=show_variables)
settings_menu.add_command(label="Toggle text color", command=toggle_text)
settings_menu.add_command(label="Toggle background color", command=toggle_background)
settings_menu.add_command(label="Reset all", command=ResetAll)

root.mainloop()
