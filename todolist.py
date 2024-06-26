import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime

class TodoListApp:
    def init(self, root):
        self.root = root
        self.root.title("Todo List App")

        self.tasks = []

        self.task_entry = tk.Entry(self.root, width=50)
        self.task_entry.pack(pady=20)

        self.add_button = tk.Button(self.root, text="Ajouter une tâche", command=self.add_task)
        self.add_button.pack()

        self.task_list = tk.Listbox(self.root, width=50)
        self.task_list.pack(pady=20)

        self.remove_button = tk.Button(self.root, text="Supprimer une tâche", command=self.remove_task)
        self.remove_button.pack()

        self.menu_bar = tk.Menu(self.root)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Nouveau", command=self.new_todo_list)
        self.file_menu.add_command(label="Ouvrir", command=self.open_todo_list)
        self.file_menu.add_command(label="Enregistrer", command=self.save_todo_list)
        self.file_menu.add_command(label="Enregistrer sous", command=self.save_as_todo_list)
        self.menu_bar.add_cascade(label="Fichier", menu=self.file_menu)

        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Toutes", command=self.show_all_tasks)
        self.edit_menu.add_command(label="En cours", command=self.show_in_progress_tasks)
        self.edit_menu.add_command(label="Terminées", command=self.show_completed_tasks)
        self.edit_menu.add_command(label="Effacer", command=self.clear_todo_list)
        self.menu_bar.add_cascade(label="Édition", menu=self.edit_menu)

        self.detail_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.detail_menu.add_command(label="À propos", command=self.show_about_info)
        self.menu_bar.add_cascade(label="Détail", menu=self.detail_menu)

        self.root.config(menu=self.menu_bar)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            new_task = {
                "Titre": task,
                "Créé_le": datetime.now().strftime("%d/%m/%Y %H:%M"),
                "Tâche": task,
                "Priorité": 1,
                "Terminée": False,
                "Date_terminée": ""
            }
            self.tasks.append(new_task)
            self.update_task_list()

    def remove_task(self):
        selected_task_index = self.task_list.curselection()
        if selected_task_index:
            task_index = int(selected_task_index[0])
            del self.tasks[task_index]
            self.update_task_list()

    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            task_text = task["Tâche"]
            if task["Terminée"]:
                task_text = f"{task_text}"
            self.task_list.insert(tk.END, task_text)

    def new_todo_list(self):
        if len(self.tasks) > 0:
            response = messagebox.askyesnocancel("Enregistrer les modifications", "Voulez-vous enregistrer la liste de tâches actuelle ?")
            if response is None:
                return
            elif response:
                self.save_todo_list()
        
        self.tasks = []
        self.update_task_list()

