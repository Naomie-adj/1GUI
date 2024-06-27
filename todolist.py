 1GUI
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox, simpledialog
from tkinter.colorchooser import askcolor
import tkinter as tk
from tkinter import messagebox, Text
 
# configuration de l'interface principale de l'application  
root = tk.Tk()
root.title("TO DO LIST APP")
#geometry("XxY+0+0")
root.geometry("700x600+100+50")

# configuration de la fenêtre de texte
text_area = tk.Text()
text_area.pack(expand=True,fill='both')
 
# fonctions permettant de manipuler l'application
# fonctions du menu fichier
 
def nouveau_fichier():
    if len(text_area.get('1.0',tk.END)) > 1:
        result = messagebox.askyesno("Enregistrer,voulez-vous enregistrer ce fichier?")
        if result :
            enregistrer_fichier()
    text_area.delete(1.0, tk.END)
 
def ouvrir_fichier():
    filepath = filedialog.askopenfilename(filetypes=[("fichier texte","*txt"),("tous les fichiers","*.*")])
    if not filepath :
        return
    text_area.delete(1.0, tk.END)
    with open(filepath,'r') as input_file:
        Text = input_file.read()
        text_area.insert(tk.END,text_area)
 
def enregistrer_fichier ():
    filepath = filedialog.askopenfilename(defaultextension="txt", filetypes=[("Fichier texte", "txt"),("Tous les fichiers","*.*")])
    if not filepath:
        return
    with open(filepath, 'W') as output_file:
        text = text_area.get(1.0, tk.END)
        output_file.write(text)
 
def enregistrer_sous_fichier():
    filepath = filedialog.asksaveasfilename(defaultextension="txt", filetypes=[("Fichiers texte", "*txt*")("tous les fichiers","*.*")])
    if not filepath:
        return
    with open(filepath,'w') as output_file:
        text = text_area.get(1.0,tk.END)
        output_file.write(text)
 # fonctions du menu configuration
def configuration_menu ():
    messagebox.showinfo("a propos:",''' fhbvnjcksxdchxnnjkjdcbf ncd,nk jcf''')
   
 # fonctions du menu edition
 
 # fonctions du menu details
def A_propos():
     messagebox.showinfo("A propos de TO DO LIST APP",'''
                         
                         
                version 1.1.1
                dévéloppeurs: ADJOVI Naomie
                              NZOUDJA Billie
                de ECOLE_IT Developpers Group
                Année d'édition : 2024
                Dépot Github                  
                                    ''')
def aide():
    messagebox.showinfo("Guide d'utilisation", '''''
                       
               bonjour   
                       
                       
                        ''''')      
 
 
     
 
# creation des menus
#menu fichier
 
To_do_list_app = tk.Menu(root)
 
fichier_menu = tk.Menu(To_do_list_app , tearoff=0)
To_do_list_app.add_cascade(label="Fichier" , menu=fichier_menu)
fichier_menu.add_command(label="Nouveau", command=nouveau_fichier)
fichier_menu.add_command(label="Ouvrir", command=ouvrir_fichier)
fichier_menu.add_command(label="Enregistrer", command=enregistrer_fichier)
fichier_menu.add_command(label="Enregistrer Sous" , command=enregistrer_sous_fichier)
fichier_menu.add_command(label="Configuration" , command=configuration_menu , )
fichier_menu.add_command(label="Quitter", command=root.quit)
 
 
 
 
#menu editions:
 
edition_menu = tk.Menu(To_do_list_app , tearoff=0)
To_do_list_app.add_cascade(label="Edition" , menu=edition_menu)
edition_menu.add_command(label="Toutes les tâches",command=A_propos)
edition_menu.add_command(label="Tâches en cours",command=A_propos)
edition_menu.add_command(label="Tâches terminées",command=A_propos)
edition_menu.add_command(label="Effacer",command=A_propos)
 
 
 
 
#menu details
details_menu = tk.Menu(To_do_list_app , tearoff=0)
To_do_list_app.add_cascade(label="Détails" , menu=details_menu)
details_menu.add_command(label="A Propos",command=A_propos)
details_menu.add_command(label="Aide" , command=aide)
 
 
 
 
 
#menu edition
 
 
 
 
 
root.config(menu=To_do_list_app)
 
root.mainloop()          
 
