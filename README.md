# VideoGame326Project

Code for INST 326 Final Project

* Scott Mobarry
* Chidima Ibezimako
* Salahdin Waji
* Germain Biyao

# Prerequisites

Download https://www.kaggle.com/rush4ratio/video-game-sales-with-ratings and install pandas, tkinter.

# Suggester

In the Video Game Suggester Program (videogamessales.py), we use video game sales data to provide a suggestion for video games that a user might want to buy. We start with data collected from the user that could be indicitive or restraining of what games they might want to use next. In addition we load a datafile of many video games and their associated platform, genre, and rating. This datafile is a csv file from Kaggle intended for machine learning experimentation. The user data is collected via our GUI and will be discussed in a subsequent section.

The csv file ('Video_Games_Sales_as_at_22_Dec_2016.csv') was loaded into a Pandas DataFrame. There are sixteen columns in the dataset in which we only used four of the columns for this project. 

## More Like This

The titles of the games are used to find genres that are available in the database that the user would like. So we want to suggest games in these genres. Note we did not ask the user about genres because each database has a different set of genre names.

## Filter

Also we cannot suggest games that the user cannot use. Two of the DataFrame columns were used to restrict the data. In particular we asked the user for their prefered platform, and their age. The age was used to compute which ESRB ratings were allowed to be suggested to the user. Our algorithm takes the Pandas DataFrame and filters down to those games that meet these requirements. 

The video game suggestor will filter rows by this criteria:
 
     1. Only keep genres of games the user likes
     2. Only keep platforms the user wants
     3. Only keep the ratings the user can buy due to their age restrictions
     4. Don't keep the titles the user gave they already like

## Sample

At this point we have a subset of games in the dataset that could be suggested. Currently the program random samples a specified number of titles. 

# GUI

  In the GUI file, there are several methods, but I will go over the ones that are executed in the main method. The main method creates an instance of a class
and calls the method list_of_games() which reads in the csv and loops each line of the csv file and appends only the name of the game into a list. The user_name() method utilizes a tkinter tool called 'entry', which allows the user to input their name. The console method utilizes a tkinter tool called 'optionmenu' and displays an abbreviated naming schema of game console that is pulled from a list. The method user_age() utilizes a tkinter 'entry' tool and allows the user to enter their age (although this feature may or may not be updated to a scrollable listbox, optionmenu or combobox that the user can select their age from instead of typing it). The method game_owned() utilizes the 'combobox' tkinter tool for all the games that are pulled from the csv file into a list for the user to select from. The method gen_lbl() is a generator label that displays a set number of recommendations based on the user inputs. The method record_entries() makes sure data stays up-to-date and extracts data that been previusly entered. The methods btn_add_consoles() and btn.add_titles() is a method for the buttons alone to appends user selections to a list. The method btn_generate() generates recommendations based on the user input and each generation is random. The method switch_settings() will probably be omitted in the near future, but its intended purpose is to activate/enable the generate button once the conditions: choose at least one game and one console to be appended to a list, in order to retrieve a video game suggestion. Lastly, the run_tk() method contains the statement "self.root.mainloop()", which saves me the trouble of having to add it to every method several times over. What is does allow code (or in this case tkinter tools to run infinitely as long as the GUI is not closed.
