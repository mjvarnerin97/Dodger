#Dodger!.py

#Name: Michael Varnerin
#Date: 21 July 2021

#Import Necessary Libraries
import tkinter as tk
from tkinter import ttk
from tkinter import *
from random import *
import time
import statistics

class Dodger():
    '''
    Welcome to Dodger! This is a game made by Michael Varnerin for CSI 31.

    In this game, you will control a circular character and try to dodge fast-falling objects. If one of the objects hits you, it's Game Over!

    I hope you enjoy this game!
    '''
    coords = [0,0]
    def __init__(self):
        '''
        This is the constructor that creates the character customizer window.
        '''
        self.char_window = tk.Tk()
        self.char_window.title("Welcome to Dodger!")
        self.char_window_canvas = tk.Canvas(width = 200, height = 200)
        self.create_char_widgets()
        
    def create_char_widgets(self):
        '''
        This method provides the framing for the GUI that the user will interact with.

        This is where the user can read how to play Dodger!, in addition to choosing the color character they wish to play as.
        '''
        self.char_window['padx'] = 5
        self.char_window['pady'] = 5

        self.instruction_frame = ttk.LabelFrame(self.char_window, text = 'How to Play:', relief = tk.RIDGE)
        self.instruction_frame.pack()

        instruction_label = ttk.Label(self.instruction_frame, text = "Welcome to Dodger! In this game, your goal is to survive as long as possible while dodging randomly falling objects.\n\nHow to Play:\n  1. Choose your character's color using the customizer below.\n  2. When you are ready, click the 'Start Game' button to begin playing!\n  3. To move your character, move your mouse while holding down the left-click button. YOUR CHARACTER WILL NOT MOVE UNLESS YOU ARE HOLDING DOWN THE LEFT-CLICK BUTTON!\n  4. Survive for as long as possible!\n\n Good Luck, and I hope you enjoy playing this game!")
        instruction_label.grid(row = 1, columnspan = 2)

        self.main_frame = ttk.LabelFrame(self.char_window, text = 'Character Customizer', relief = tk.RIDGE)
        self.main_frame.pack()

        character_label = ttk.Label(self.main_frame, text = "What color would you like your character to be?  \n(Red, Blue, Green, Pink, Yellow, Purple, or Orange) ")
        character_label.grid(row = 2, column = 1)

        self.character_color_entry = ttk.Entry(self.main_frame, width = 50)
        self.character_color_entry.grid(row = 2, column = 2)

        button_color = ttk.Button(self.main_frame, text = "Preview Character", command = self.character_builder)
        button_color.grid(row = 3, column = 2)

        self.startGame_frame = ttk.Frame(self.char_window, relief = tk.RIDGE)
        self.startGame_frame.pack()

    def character_builder(self):
        '''
        This method creates the character object in addition to showing a preview of the character of choice to the user prior to the game starting.
        '''
        self.char_window_canvas.delete('all')
        self.color_choice = self.character_color_entry.get()
        self.color_choice = self.color_choice.lower()
        if self.color_choice in ['red', 'blue', 'green', 'pink', 'yellow', 'purple', 'orange']:
            self.char_window_canvas.create_text(100,50, text = "This will be your character:", font = 'Helvetica 11 bold')
            self.char_window_canvas.create_oval(75, 75, 125, 125, fill = self.color_choice)
            button_game_start = ttk.Button(self.startGame_frame, text = "            Start Game!            ", command = self.game)
            button_game_start.grid(row = 1, columnspan = 4)
        else:
            self.char_window_canvas.create_text(100,100, text = "Please enter a valid color.", fill = 'red', font = 'Helvetica 12 bold')
            button_game_start = ttk.Button(self.startGame_frame, text = "Please Enter a Valid Color")
            button_game_start.grid(row = 1, columnspan = 4)
        self.char_window_canvas.pack()

        def draw(self):
            '''
            This nested method draws the character on the screen.
            '''
            information = (self.tx, self.ty, self.tx-(0.5*self.base), self.ty+self.height, self.tx+(0.5*self.base), self.ty+self.height)
            canvas.create_polygon(information, fill = self.color)

    def game(self):
        '''
        This method removes the character builder window and then opens up the actual game window for Dodger!.

        The character is drawn against a black background, and methods are called within this function to activate the falling spikes, allow for the character to move, in addition to providing a 'Quit Game'
        button that the user can click at any time to exit the program.
        '''
        self.char_window.destroy()
        self.game_window = tk.Tk()
        self.game_window.title("Dodger!")
        self.game_window_canvas = tk.Canvas(width = 600, height = 800, bg = 'black')
        x1 = 275
        x2 = 325
        y1 = 675
        y2 = 725
        self.character = self.game_window_canvas.create_oval(x1, y1, x2, y2, fill = self.color_choice)
        self.coords = [statistics.mean((x1, x2)), statistics.mean((y1, y2))]
        self.create_game_widgets()
        self.spikes()

    def movement(self, event):
        '''
        This method draws the character at a given point in the xy coordinate plane based on the user's mouse movements.

        Additionally, in order to detect collision, this method contains a conditional statement that will check if the character's x and y coordinates match those of the falling spikes. If so,
        a Game Over is triggered.
        '''
        self.event = event
        self.coords = [self.event.x, self.event.y]
        self.drawCharacter(self.event.x, self.event.y)

    def drawObstacles(self):
        '''
        This method draws the spikes and causes them to fall from the top of the screen to the bottom of the screen.
        '''
        self.rand_x = randrange(30,570)
        spike = self.game_window_canvas.create_oval(self.rand_x,-20,self.rand_x+40, 50 ,fill = 'grey')
        self.timeDelay = .001
        for i in range(83):
            self.i = i
            time.sleep(self.timeDelay)
            self.game_window_canvas.move(spike, 0,10)
            self.game_window_canvas.update()
            self.spike_x_coord = self.rand_x
            self.spike_y_coord = 50 + 10*self.i
            if self.spike_y_coord - 25 <= self.coords[1] <= self.spike_y_coord + 25 and self.spike_x_coord - 25 <= self.coords[0] <= self.spike_x_coord + 25:
                self.game_over()


    def spikes(self):
        '''
        This method invokes the drawObstacles method in a while loop so that spikes continually fall until a Game Over occurs, or the player quits the game.
        '''
        while self.character:
            self.drawObstacles()

    def drawCharacter(self, x, y):
        '''
        This method draws the character at a given point in the xy coordinate plane
        '''
        if 25 <= x <= 575 and 25 <= y <= 775:
            self.game_window_canvas.coords(self.character, x-25, y-25, x+25, y+25)

    def create_game_widgets(self):
        '''
        This method contains widgets that bind the character's movements to the self.movement method, in addition to providing the user
        with a Quit Game button.
        '''
        self.game_window['padx'] = 1
        self.game_window['pady'] = 1

        self.game_command_frame = ttk.LabelFrame(self.game_window, relief = tk.RIDGE)
        self.game_command_frame.pack()
        
        self.game_window_canvas.pack()   

        self.game_window_canvas.bind('<B1-Motion>', self.movement)
        quit_button = ttk.Button(self.game_command_frame, text = "Quit Game", command = self.quit_game)
        quit_button.grid(row = 1, columnspan = 3)

    def quit_game(self):
        '''
        This method destroys the game window, thereby ending the program.
        '''
        self.game_window.destroy()

    def play_again(self):
        '''
        This method destroys the game over window, and restarts the program.
        '''
        self.game_over_window.destroy()
        Dodger()

    def game_over(self):
        '''
        This method creates a game over screen, with a Play Again button that will restart the program
        if the user wishes to play again.
        '''
        self.game_window.destroy()
        self.game_over_window = tk.Tk()
        self.game_over_window.title("Game Over")
        self.game_over_window_canvas = tk.Canvas(width = 400, height = 200, bg = 'white')
        self.game_over_window_canvas.create_text(200, 100, text = "Game Over!", fill = 'red', font = 'Helvetica 28 bold')
        play_again_button = Button(self.game_over_window, text = 'Play Again', width = 10, height = 2, bd = '10', command = self.play_again)
        play_again_button.place(x = 155, y = 140)
        self.game_over_window_canvas.pack()

# Create the entire GUI program
program = Dodger()

# Start the GUI event loop
program.char_window.mainloop()
program.game_window.mainloop()
program.game_over_window.mainloop()
