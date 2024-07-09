import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog, colorchooser
import json
from datetime import datetime


class TodolistApp:
    #initialisation de la fenêtre principale
    def __init__(self, root):
        self.root = root
        self.root.title("To do List App")
        self.tasks = []
        self.current_file = None

        # Creation des menus
        self.create_menus()

        # Cadre de la liste des tâches
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=1)
        
        #listbox pour afficher les tâches
        self.task_listbox = tk.Listbox(self.frame, selectmode=tk.SINGLE)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        #barre déroullante(scollbar)
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Creation de boutons pour gérer les tâches
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(fill=tk.X)
        
        #bouton pour ajouter une tâche
        self.add_button = tk.Button(self.button_frame, text="Ajouter Tâche", command=self.ajouter_tache)
        self.add_button.pack(side=tk.LEFT)
        
        #bouton pour modifier une tâche
        self.edit_button = tk.Button(self.button_frame, text="Modifier Tâche", command=self.editer_tache)
        self.edit_button.pack(side=tk.LEFT)

        #bouton pour supprimer une tâche
        self.delete_button = tk.Button(self.button_frame, text="Supprimer Tâche", command=self.supp_tache)
        self.delete_button.pack(side=tk.LEFT)
        
        #bouton pour marquer une tâche comme terminée
        self.complete_button = tk.Button(self.button_frame, text="Marquer Comme Terminée", command=self.completer_tache)
        self.complete_button.pack(side=tk.LEFT)

    def create_menus(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        #creation du menu fichier

        fichier_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Fichier", menu=fichier_menu)
        fichier_menu.add_command(label="Nouveau", command=self.nouveau_fichier)
        fichier_menu.add_command(label="Ouvrir", command=self.ouvrir_fichier)
        fichier_menu.add_command(label="Enregistrer", command=self.enregistrer)
        fichier_menu.add_command(label="Enregistrer sous", command=self.enregistrer_sous)
        fichier_menu.add_command(label="Configuration", command=self.configurer)
        
        #creation du menu edition
        edition_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Édition", menu=edition_menu)
        edition_menu.add_command(label="Toutes les tâches", command=self.toutes)
        edition_menu.add_command(label="Tâches en cours", command=self.en_cours)
        edition_menu.add_command(label="Tâches terminées", command=self.terminees)
        edition_menu.add_command(label="Effacer", command=self.effacer)
        
        #creation du menu details
        details_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Détails", menu=details_menu)
        details_menu.add_command(label="À propos", command=self.infos)
       
#fonctions
    def nouveau_fichier(self):
        if self.tasks and messagebox.askyesno("Nouveau fichier",
                                              "Voulez-vous enregistrer la liste actuelle avant d'en créer une nouvelle?"):
            self.enregistrer()
        self.tasks = []
        self.current_file = None
        self.task_listbox.delete(0, tk.END)

    def ouvrir_fichier(self):
        file_path = filedialog.askopenfilename(defaultextension=".json",
                                               filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
        if file_path:
            try:
                with open(file_path, 'r') as file:
                    data = json.load(file)
                    self.tasks = data["tasks"]
                    self.current_file = file_path
                    self.update_tache()
            except Exception as e:
                messagebox.showerror("Erreur", f"Impossible d'ouvrir le fichier: {e}")

    def enregistrer(self):
        if not self.current_file:
            self.enregistrer_sous()
        else:
            self.enregistrer_alt(self.current_file)

    def enregistrer_sous(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".json",
                                                 filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
        if file_path:
            self.enregistrer_alt(file_path)

    def enregistrer_alt(self, file_path):
        try:
            with open(file_path, 'w') as file:
                data = {
                    "title": " To do list App",
                    "tasks": self.tasks
                }
                json.dump(data, file, indent=4)
            self.current_file = file_path
        except Exception as e:
            messagebox.showerror("Erreur", f"Impossible de sauvegarder le fichier: {e}")

    def configurer(self):
        color = colorchooser.askcolor(title="Choisir une couleur")
        if color:
            self.task_listbox.config(bg=color[1])

    def toutes(self):
        self.update_tache()

    def en_cours(self):
        self.update_tache(show_in_progress=True)

    def terminees(self):
        self.update_tache(show_completed=True)

    def effacer(self):
        if messagebox.askyesno("Effacer", "Voulez-vous vraiment effacer toutes les tâches?"):
            self.tasks = []
            self.task_listbox.delete(0, tk.END)

    def infos(self):
        messagebox.showinfo("À propos",
                            "TO DO LIST APP\nVersion 1.0.0\nDéveloppeurs: ADJOVI Naomie et NZOUDJA Billie\nAnnée d'édition: 2024\nDépot GitHub: https://github.com/Naomie-adj/1GUI")

    def ajouter_tache(self):
        task_text = simpledialog.askstring("Ajouter Tâche", "Description de la tâche:")
        if task_text:
            priority = simpledialog.askinteger("Ajouter Tâche", "Priorité (1-7):", minvalue=1, maxvalue=7)
            if priority:
                new_task = {
                    "task": task_text,
                    "create_at": datetime.now().strftime("%d/%m/%Y %H:%M"),
                    "priority": priority,
                    "Done": False,
                    "ended_date": None
                }
                self.tasks.append(new_task)
                self.update_tache()
            else:
                messagebox.showerror("Erreur", "Veuillez entrer une priorité valide entre 1 et 7.")
        else:
            messagebox.showerror("Erreur", "La description de la tâche ne peut pas être vide.")

    def editer_tache(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            task = self.tasks[index]
            new_task_text = simpledialog.askstring("Modifier Tâche", "Description de la tâche:",
                                                   initialvalue=task["task"])
            if new_task_text:
                new_priority = simpledialog.askinteger("Modifier Tâche", "Priorité (1-7):",
                                                       initialvalue=task["priority"], minvalue=1, maxvalue=7)
                if new_priority:
                    task["task"] = new_task_text
                    task["priority"] = new_priority
                    self.update_tache()
                else:
                    messagebox.showerror("Erreur", "Veuillez entrer une priorité valide entre 1 et 7.")
            else:
                messagebox.showerror("Erreur", "La description de la tâche ne peut pas être vide.")
        else:
            messagebox.showerror("Erreur", "Veuillez sélectionner une tâche à modifier.")

    def supp_tache(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            if messagebox.askyesno("Supprimer Tâche", "Voulez-vous vraiment supprimer cette tâche?"):
                del self.tasks[index]
                self.update_tache()
        else:
            messagebox.showerror("Erreur", "Veuillez sélectionner une tâche à supprimer.")

    def completer_tache(self):
        selected_task_index = self.task_listbox.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            task = self.tasks[index]
            task["Done"] = True
            task["ended_date"] = datetime.now().strftime("%d/%m/%Y %H:%M")
            self.update_tache()
        else:
            messagebox.showerror("Erreur", "Veuillez sélectionner une tâche à marquer comme terminée.")

    def update_tache(self, show_in_progress=False, show_completed=False):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            if show_in_progress and task["Done"]:
                continue
            if show_completed and not task["Done"]:
                continue
            task_str = task["task"]
            if task["Done"]:
                task_str += f" - Accomplit le {task['ended_date']}"
            self.task_listbox.insert(tk.END, task_str)


if __name__ == "__main__":
    root = tk.Tk()
    app = TodolistApp(root)
    root.mainloop()
