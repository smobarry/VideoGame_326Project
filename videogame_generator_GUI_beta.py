import argparse
import os
import sys
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import csv
import pandas

class game_Generator:
    
    def __init__(self):
        self.root = tk.Tk()#refers to the window
        self.root.title("Videogame Suggestion Generator")
        self.root.geometry("600x400")
        self.v = tk.IntVar()
        self.games=["GTA, Super Mario"]#list is only here for testing purposes. will be removed/updated later
        #self.root.mainloop()
        
    def run_tk(self):
        self.root.mainloop()
        
    def user_name(self):
        self.name_var = tk.StringVar()
        self.name_var.set("Name")
        
        tk.Label(self.root, 
                text="Enter your name:" 
                ).grid(row=0, column=0)
         
        self.entry_name = tk.Entry(self.root, textvariable = self.name_var, bd =5).grid(row=1, column=0, padx=1)
         
         
    
    def console(self):
        
        self.v.set(1)#Default value i.e. Playstation
        
        tk.Label(self.root, 
                text="Choose a gaming console that you own:" 
                ).grid(row=2, column=0)
        
        self.rbtn_Play = tk.Radiobutton(self.root, 
                    text="PlayStation",
                    #padx = 20, 
                    variable=self.v, 
                    value=1).grid(row=3, column=0)
        
        self.rbtn_Xbox = tk.Radiobutton(self.root, 
                    text="Xbox",
                    #padx = 20, 
                    variable=self.v, 
                    value=2).grid(row=4, column=0)

        #self.root.mainloop()
    
    def list_of_games(self):
        #self.games=["GTA, Super Mario"]
        pass
        
    def user_age(self):
        self.age_var = tk.IntVar()
        self.age_var.set(6)
        
        self.lbl_age = tk.Label(self.root, text="Enter your age").grid(row=5, column=0)
        #lbl_age.grid(row=0, column = 3).pack( side = LEFT)
        #lbl_age.pack(side = LEFT)
        self.entry_age = tk.Entry(self.root, textvariable = self.age_var, bd =5).grid(row=6, column=0, padx=1)
        #entry_age.pack(side = RIGHT)
        #Notes: Cannot use grid and pack in same root/window
        #pass
        
    def game_owned(self):
        self.gameType_var = tk.StringVar()
        self.lbl_game = tk.Label(self.root, text = "Enter the games that you own ").grid(row=7, column=0)
        self.entry_gameType = tk.Entry(self.root, textvariable= self.gameType_var, bd =5).grid(row=8,column=0)
        pass
    
    def gen_lbl(self):
        self.recommend = tk.StringVar()
        self.recommend.set("Recommendations will be displayed here")
        
        label_gen = Label(self.root, textvariable= self.recommend, width = 20 ).grid(row=12, column= 0)
    
    def generate(self):
        #messagebox.showinfo("Testing", "Button Works!") 
       
        
        #try:
            if self.name_var != "Name":
                if self.age_var.get() > 6:
                    messagebox.showinfo("Age", "Age greater than 6!") #just to test code. not final edit
                pass
            messagebox.showinfo("Name", "Name is not name!") #not final edit
            self.recommend.set("tester")#for list or csv file with game recmmendatins
            pass
        
       
        #print("hi")
        #pass
    
    def btn_generate(self):
        

        btn_gen = tk.Button(self.root, text = "Generate", command = self.generate).grid(row=9, column=0)
        
        #pass
    
def main():
    gen = game_Generator()
    gen.user_name()
    gen.console()
    gen.user_age()
    gen.game_owned()
    gen.gen_lbl()
    gen.btn_generate()
    #gen.generate()
    gen.run_tk()
        
if __name__ == "__main__":
    main()
   
