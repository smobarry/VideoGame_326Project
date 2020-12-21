import argparse
import os
import sys
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import csv
import pandas
import videogamessales

class game_Generator:
    
    def __init__(self):
        self.root = tk.Tk()#refers to the window
        self.root.title("Videogame Suggestion Generator")
        self.root.geometry("1000x400")
        self.v = tk.IntVar()
        #self.consoles =[""]#this needs to be populated first
        #self.titles = [""]#this needs to be populated first
        self.consoles =['XB', 'PS']#for testing purposes
        self.titles=  ['']#for testing purposes
        self.fname = 'Video_Games_Sales_as_at_22_Dec_2016.csv'
        self.df = videogamessales.make_games_clean(self.fname)
        self.gameList=['']
      
        #self.games=["GTA, Super Mario"]#list is only here for testing purposes. will be removed/updated later
        #self.root.mainloop()
        
    def run_tk(self):
        self.root.mainloop()
        
    def user_name(self):
        self.name_var = tk.StringVar()
        #self.name_var.set("Enter your name here")
        
        tk.Label(self.root, 
                text="Enter your name:" 
                ).grid(row=0, column=0)
         
        self.entry_name = tk.Entry(self.root, textvariable = self.name_var, bd =5).grid(row=0, column=1, padx=1)
        
     
    def console(self):
        
        #self.v.set(1)#Default value i.e. Playstation
        
        tk.Label(self.root, 
                text="Owned gaming console:" 
                ).grid(row=1, column=0)
        
        # self.rbtn_Play = tk.Radiobutton(self.root, 
        #             text="PlayStation",
        #             #padx = 20, 
        #             variable=self.v, 
        #             value=1).grid(row=1, column=1)
        
        # self.rbtn_Xbox = tk.Radiobutton(self.root, 
        #             text="Xbox",
        #             #padx = 20,  
        #             variable=self.v, 
        #             value=2).grid(row=1, column=2)
        OPTIONS = [
       "3DS", "DC", "GBA", "GC", "PC",
        "PS", "PS2", "PS3", "PS4", "PSP", "PSV",
        "Wii", "WiiU", "XB", "X360", "XOne"
        ] #list of game consoles
        
        self.gc = StringVar()
        self.gc.set(OPTIONS[0]) # default value

        w = OptionMenu(self.root, self.gc,*OPTIONS).grid(row=1, column=1)
        

        #self.root.mainloop()
    
    def list_of_games(self):
        with open("Video_Games_Sales_as_at_22_Dec_2016.csv") as gameFile:
            self.csv_reader = csv.DictReader(gameFile, delimiter=',')
            for lines in self.csv_reader:
                self.gameList.append(lines['Name'])
               
        return self.gameList
    
       
        
        
    def user_age(self):
        self.age_var = tk.IntVar()
        #self.age_var.set(6)
        
        self.lbl_age = tk.Label(self.root, text="Enter your age").grid(row=2, column=0)
        
        self.entry_age = tk.Entry(self.root, textvariable = self.age_var, bd =5).grid(row=2, column=1, padx=1)
        #entry_age.pack(side = RIGHT)
        #Notes: Cannot use grid and pack in same root/window
        #pass
        
       
        
        
        
    def game_owned(self):
       
        
        self.gameType_var = tk.StringVar()
        self.lbl_game = tk.Label(self.root, text = "Owned games: ").grid(row=3, column=0,padx=5, pady=5)
        
        
        self.combo_games = ttk.Combobox(self.root, textvariable= self.gameType_var , values=self.gameList).grid(row=3,column=1, padx=1, pady=1)
        
        
        #self.entry_gameType = tk.Entry(self.root, textvariable= self.gameType_var, bd =5)
    def gen_lbl(self):
        #self.recommend = tk.StringVar()
        #self.recommend.set("Recommendations will be displayed here")
        
        self.label_gen = Label(self.root, text="Recommendations will be displayed here")
        self.label_gen.grid(row=10, column= 1, padx=5, pady=5)
    
    
    def record_entries(self):
        self.name_input = self.name_var.get()#retieves the value in the name textbox
        self.game_console = self.gc.get()#retrieves console input from the user
        self.game_input = self.gameType_var.get()#retrieves game input from the user
        self.age_input = self.age_var.get()#retrieves age input from the user
        
        #videogamessales.my_age = self.age_input
        
    def add_titles(self):
        #self.record_entries()#just pre-loads entries inputed by user
        try:
            self.record_entries()
            #self.gameType_var.get()
            #self.titles.append(self.game_input)
            #self.titles.append(self.game_input)
        except:
            print("List cannot be empty!")
        finally:
            self.titles.append(self.game_input)
        
        
        #self.recommend.set(self.titles)
    
    
    
    def add_consoles(self):
        self.record_entries()#just pre-loads entries inputed by user
        # if self.game_console == 1:
        #     self.consoles.append("PS")
        # else:
        self.consoles.append(self.game_console)
        #self.recommend.set(self.consoles)
        
    def show_titles_lbl(self):
        self.record_entries()
        #self.games = tk.StringVar()
        #self.games.set("List will be displayed here")
        
        self.lbl_games = Label(self.root, text="\n".join(self.titles)).grid(row=3, column= 4, padx=5, pady=5)
        #self.lbl_games.config(text='')
        #self.lbl_games.config(test=("\n".join(self.gameList)))
        
    
    def btn_add_titles(self):
        btn_gen = tk.Button(self.root, text = "Add Games", command = self.add_titles).grid(row=3, column=2, padx=5, pady=5)
    
    def btn_show_titles(self):
        self.record_entries()
        btn_gen = tk.Button(self.root, text = "Preview List", command = self.show_titles_lbl).grid(row=3, column=3, padx=5, pady=5)
            
    def btn_add_consoles(self):
        btn_gen = tk.Button(self.root, text = "Add Console", command = self.add_consoles).grid(row=1, column=2, padx=5, pady=5)
        
    
    def generate(self):
        self.record_entries()#just pre-loads entries inputed by user
        
        
        #try:
        # if self.name_var != "Name":
        #     if self.age_var.get() > 4:
        #         messagebox.showinfo("Age", "Age is {}".format(self.age_input)) #just to test code. not final edit
        #     pass
        # messagebox.showinfo("Name", "Name is {}".format(self.name_input)) #not final edit
        try:
            self.label_gen.configure(text="{}, we recommend ".format(self.name_input)+
                       str(videogamessales.suggest_games(self.df,self.titles, self.consoles, self.age_input,3))
                       + " to play next")#for list or csv file with game recommendations
            pass
        except AttributeError:
            messagebox.showinfo("Information Needed", "Please make sure all fields are filled")
        finally:
            pass
        
        
        
        
        
        
    def btn_generate(self):

        self.btn_gen = tk.Button(self.root, text = "Generate", command = self.generate, state=NORMAL).grid(row=5, column=1, padx=5, pady=5)
        
        #pass
    
    def switch_settings(self):
        if not self.titles and self.consoles:
            self.btn_gen["state"] = tk.DISABLED
    
    
def main():
    #methods to function the buttons
    gen = game_Generator()
    gen.list_of_games()
    gen.user_name()
    gen.console()
    gen.user_age()
    gen.game_owned()
    
    #methods for labels
    gen.show_titles_lbl()
    gen.gen_lbl()
    
    
    #gen.record_entries()
    
    #methods for buttons
    gen.btn_add_consoles()
    gen.btn_add_titles()
    gen.btn_show_titles()
    gen.btn_generate()
    #gen.switch_settings()
    
    
    gen.run_tk()
        
if __name__ == "__main__":
    main()
   
