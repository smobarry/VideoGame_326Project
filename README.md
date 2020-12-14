# VideoGame326Project
Code for INST 326 Final Project

* Scott Mobarry
* Chidima Ibezimako
* Salahdin Waji
* Germain Biyao

download and install pandas, tkinter
import csv, videogamessales, pandas as pd, tkinter as tk
from tkinter import ttk

  In the GUI file, there are several methods, but I will go over the ones that are executed in the main method. The main method creates an instance of a class
and calls the method list_of_games() which reads in the csv and loops each line of the csv file and appends only the name of the game into a list. The user_name() method utilizes a tkinter tool called 'entry', which allows the user to input their name. The console method utilizes a tkinter tool called 'optionmenu' and displays an abbreviated naming schema of game console that is pulled from a list. The method user_age() utilizes a tkinter 'entry' tool and allows the user to enter their age (although this feature may or may not be updated to a scrollable listbox, optionmenu or combobox that the user can select their age from instead of typing it). The method game_owned() utilizes the 'combobox' tkinter tool for all the games that are pulled from the csv file into a list for the user to select from. The method gen_lbl() is a generator label that displays a set number of recommendations based on the user inputs. The method record_entries() makes sure data stays up-to-date and extracts data that been previusly entered. The methods btn_add_consoles() and btn.add_titles() is a method for the buttons alone to appends user selections to a list. The method btn_generate() generates recommendations based on the user input and each generation is random. The method switch_settings() will probably be omitted in the near future, but its intended purpose is to activate/enable the generate button once the conditions: choose at least one game and one console to be appended to a list, in order to retrieve a video game suggestion. Lastly, the run_tk() method contains the statement "self.root.mainloop()", which saves me the trouble of having to add it to every method several times over. What is does allow code (or in this case tkinter tools to run infinitely as long as the GUI is not closed.
