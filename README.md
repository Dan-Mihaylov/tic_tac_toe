# Simple Tic Tac Toe Game
First Python Project To Practice Basic Python Knowledge And Learn Tkinter GUI and Pillow




 The Main Page of the Tic Tac Toe game gives you the options to start a Single game, Multiplayer game or Quit the game. The Play against the computer logic is not developed yet.
 The widgets that have been used for the whole game are, Labelframe, Label, Menu, Button, Entry, Messagebox, Toplevel, PhotoImage. The widgets have been displayed using a combination of the pack() and grid() methods.
 
 Main Page Image:

![main_page](https://user-images.githubusercontent.com/123562461/215777726-75c2af89-27ed-470e-9b14-2110a6914355.png)

The dropdown Menubar gives you the options to go back to the Main Menu or Quit the game constantly

![dropdown_menubar](https://user-images.githubusercontent.com/123562461/215779891-5d5cff4f-e5c1-4c2d-8dbc-a8eee058a91e.png)

When selecting Single Game, the game automatically starts, and a grid system with the available options to play is displayed. X always starts the game. You play alone, and now that I think about it, I will remove against PC and create the Single Player logic to automatically play against it, rather than by yourself.


![Single_player](https://user-images.githubusercontent.com/123562461/215780150-1cfe0da8-6f45-4b0a-a3c3-d43b80170d3a.png)

When selecting a box that is already takken, a popup widget appears and asks you to select a window that hasn't already been selected.

![pop_up_message](https://user-images.githubusercontent.com/123562461/215781477-5de3b487-c693-487f-ba91-82bad068fbb3.png)

In the event of a win a new Toplevel window appears with a gif animation of fireworks to congratulate the winner.
Then you are given the options to go To Main Menu, or Start Again.

![winner_animation](https://user-images.githubusercontent.com/123562461/215781664-51cd84ce-29e1-425d-9771-d4b13896eb4a.png)

In the event of a draw a new Toplevel window appears to state that it is a draw and again gives you the options to go Main Menu or New Game.

![draw_window](https://user-images.githubusercontent.com/123562461/215782495-78833915-6fa6-49ff-ab9a-37845b3a425c.png)


When selecting Multiplayer in the Main Menu, you are given the options to get player one and player two names. This names are used when displaying the winner, and in the future there will be stars implemented into the game.


![multiplayer option](https://user-images.githubusercontent.com/123562461/215782976-cfa1bba9-08c2-41da-beea-d32b8be90bf7.png)

Overall the creating the game has helped me understand basic funtionality of Tkinter library and practice simple Python List and Dictionary functions.

### Added a Zip file so you can test the game in the [Demo](https://github.com/Dan-Mihaylov/tic_tac_toe/tree/main/demo) directory 

