from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox


root = Tk()
root.title("Tic Tac Toe")
root.overrideredirect(True)
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int(screen_width / 2) - (400 // 2)
y_coordinate = int(screen_height / 2) - (600 // 2)
root.geometry(f"{400}x{600}+{x_coordinate}+{y_coordinate}")
main_menu_frame = LabelFrame(root, width=400, height=600)

# Creating a boolean to see if it is going to display X or O
is_x = True
# Creating variables for the logo image of the game
my_img_label = Label
my_img = Image


# Create the image we are using for the main page.
# It will return a Label widget with the image inside it, just have to display it.
def image(path):
    global my_img_label, my_img, main_menu_frame
    my_img = Image.open(path)
    image_resize = Image.Image.resize(my_img, (50, 50))
    my_img = ImageTk.PhotoImage(image_resize)
    my_img_label = Label(main_menu_frame, image=my_img)
    return my_img_label


player_one_name = ""
player_two_name = ""


def go_to_main_page():
    global winner_window, main_menu_frame, entry_one, entry_two, player_one_name, player_two_name, counter, is_x

    record_positions.clear()
    create_positions()
    game_frame.forget()

    main_menu_frame.forget()
    winner_window = Toplevel.destroy
    counter = 0
    is_x = True

    player_one_name = "X"
    player_two_name = "O"

    root.geometry("450x600")

    # Creating the main menu frame, will give you option to play alone, with pc or with opponent

    main_menu_frame = LabelFrame(root, width=400, height=600, relief=FLAT)
    main_menu_frame.pack(fill=BOTH, expand=True)

    game_logo = image("C:/Users/danie/PycharmProjects/tic_tac_toe/images/Tic.png")
    game_logo.pack(pady=20)

    title = Label(main_menu_frame, text="Select Game Type", font="TimesNewRoman 30", fg="grey", anchor='s', pady=10)
    title.pack(side=TOP, pady=15, anchor="center")

    start_game_button = Button(main_menu_frame, text="Single Game", font="helvetica 10", pady=10, padx=30, width=25,
                               command=start_game)
    start_game_button.pack(pady=10)

    against_pc_button = Button(main_menu_frame, text="Against Pc", font="helvetica 10", pady=10, padx=30, width=25)
    against_pc_button.pack(pady=10)

    multiplayer = Button(main_menu_frame, text="Multiplayer", font="helvetica 10", pady=10, padx=30, width=25,
                         command=multiplayer_game)
    multiplayer.pack(pady=10)

    quit_button = Button(main_menu_frame, text="Quit Game", font="helvetica 10", pady=10, padx=30, width=25,
                         command=root.destroy)
    quit_button.pack(pady=10)


# Creating a menubar  with the options to go to main win or quit

menubar = Menu(root)
root.config(menu=menubar)

options_menu = Menu(menubar, tearoff=0, selectcolor="RED")
menubar.add_cascade(label="File", menu=options_menu)
options_menu.add_command(label="Main Menu", command=go_to_main_page)
options_menu.add_separator()
options_menu.add_command(label="Quit Program", command=root.destroy)

count = 0
anim = None

# Creating a dict to store the played values

record_positions = {}


def create_positions():
    for i in range(1, 10):
        converted_to_string = "b"+str(i)
        record_positions[converted_to_string] = ""


# Check if there is a winner on the grid

winner_window = Toplevel
counter = 0
player = ""         # who is playing, if x wins X if o wins O, if adding name, display the name


def winner_animation():
    global winner_window, player, count

    main_menu_frame.forget()

    winner_window = Toplevel()
    winner_window.geometry("400x700")
    root.eval(f'tk::PlaceWindow {str(winner_window)} center')
    winner_window.overrideredirect(True)

    winner_label = Label(winner_window, text=f"The Winner Is {player}", font="helvetica 26 bold", fg="red")
    winner_label.pack(pady=20)

    file = 'C:/Users/danie/PycharmProjects/tic_tac_toe/images/firework2.gif'
    gif = Image.open(file)

    frames = gif.n_frames

    image_list = [PhotoImage(file=file, format=f"gif -index {i}") for i in range(frames)]

    count = 0
    anim = ""

    def stop_animation():
        global anim

        winner_window.after_cancel(anim)
        winner_window.after(10, winner_window.destroy)
        go_to_main_page()

# Using recursion to continue playing the gif

    def animation(frame_count):
        global anim
        new_image = image_list[frame_count]

        gif_label.configure(image=new_image)
        frame_count += 1
        if frame_count == frames:
            frame_count = 0
        anim = root.after(100, lambda: animation(frame_count))

    gif_label = Label(winner_window, image="")
    gif_label.pack()

    stop = Button(winner_window, text="To Main Menu", command=stop_animation, width=20, height=5)
    stop.pack(pady=10, padx=20, side="left")

# Creating a local function to start a new game, and destroy the current window

    def start_again_button():
        winner_window.destroy()
        start_game()

    start_again_button = Button(winner_window, text="Start Again", command=start_again_button, width=20, height=5)
    start_again_button.pack(pady=10, padx=20, side="right")

    animation(count)  # start the animation straight away


def winner_check():
    global winner_window, player, counter, is_x

    if counter > 4:

        if record_positions["b1"] == "X" and record_positions["b2"] == "X" and record_positions["b3"] == "X"\
            or record_positions["b1"] == "X" and record_positions["b4"] == "X" and record_positions["b7"] == "X"\
                or record_positions["b4"] == "X" and record_positions["b5"] == "X" and record_positions["b6"] == "X"\
                or record_positions["b7"] == "X" and record_positions["b8"] == "X" and record_positions["b9"] == "X"\
                or record_positions["b2"] == "X" and record_positions["b5"] == "X" and record_positions["b8"] == "X"\
                or record_positions["b3"] == "X" and record_positions["b6"] == "X" and record_positions["b9"] == "X"\
                or record_positions["b1"] == "X" and record_positions["b5"] == "X" and record_positions["b9"] == "X"\
                or record_positions["b3"] == "X" and record_positions["b5"] == "X" and record_positions["b7"] == "X":

            player = player_one_name
            counter = 0
            is_x = True
            record_positions.clear()
            create_positions()

            winner_animation()

        elif record_positions["b1"] == "O" and record_positions["b2"] == "O" and record_positions["b3"] == "O" \
            or record_positions["b1"] == "O" and record_positions["b4"] == "O" and record_positions["b7"] == "O" \
                or record_positions["b4"] == "O" and record_positions["b5"] == "O" and record_positions["b6"] == "O" \
                or record_positions["b7"] == "O" and record_positions["b8"] == "O" and record_positions["b9"] == "O" \
                or record_positions["b2"] == "O" and record_positions["b5"] == "O" and record_positions["b8"] == "O" \
                or record_positions["b3"] == "O" and record_positions["b6"] == "O" and record_positions["b9"] == "O" \
                or record_positions["b1"] == "O" and record_positions["b5"] == "O" and record_positions["b9"] == "O" \
                or record_positions["b3"] == "O" and record_positions["b5"] == "O" and record_positions["b7"] == "O":

            player = player_two_name
            counter = 0
            is_x = True
            record_positions.clear()
            create_positions()

            winner_animation()

        elif counter == 9:
            record_positions.clear()
            create_positions()

            winner_window = Toplevel()
            winner_window.geometry("500x200")
            winner_window.overrideredirect(True)
            root.eval(f'tk::PlaceWindow {str(winner_window)} center')

            win_label = Label(winner_window, text="IT IS A DRAW!", font="helvetica 26", fg="red")
            win_label.pack(pady=50)

            def close():
                winner_window.destroy()
                go_to_main_page()

            def new_game():
                winner_window.destroy()
                start_game()

            main_menu_button = Button(winner_window, text="Main Menu", command=close, width=20)
            main_menu_button.pack(side=LEFT, padx=50)

            new_game_button = Button(winner_window, text="New Game", command=new_game, width=20)
            new_game_button.pack(side=RIGHT, padx=50)


# Creating a function to change the clicked button

def clicked(b, button_number):
    global is_x, count, counter
    counter += 1

    if b["text"] == "M" and is_x:
        b["text"] = "X"
        b["fg"] = "#d9d9d9"
        is_x = False
        record_positions[button_number] = "X"
        count += 1
        winner_check()

    elif b["text"] == "M" and not is_x:
        b["text"] = "O"
        b["fg"] = "black"
        is_x = True
        count += 1
        record_positions[button_number] = "O"
        winner_check()

    else:
        messagebox.showerror("Tic Tac Toe", "You Have To Select An Empty Box")


game_frame = LabelFrame(root, width=800, height=800)


def start_game():
    global game_frame, main_menu_frame
    main_menu_frame.after(10, main_menu_frame.forget)
    root.geometry('800x800')

    main_menu_frame.forget()
    # Creating the frame that the game will be played in

    game_frame.pack(fill=BOTH, expand=True)

    # Creating the grid system, which will be expandable

    game_frame.columnconfigure(1, weight=2)
    game_frame.columnconfigure(3, weight=2)
    game_frame.columnconfigure(5, weight=2)
    game_frame.rowconfigure(1, weight=2)
    game_frame.rowconfigure(3, weight=2)
    game_frame.rowconfigure(5, weight=2)

    # will create Buttons for each option you got

    b1 = Button(game_frame, text="M", font="Timesnewroman 30", bg="#404040", activebackground="#808080", fg="#404040",
                activeforeground="#808080", command=lambda: clicked(b1, "b1"))
    b2 = Button(game_frame, text="M", font="Timesnewroman 30", bg="#404040", activebackground="#808080", fg="#404040",
                activeforeground="#808080", command=lambda: clicked(b2, "b2"))
    b3 = Button(game_frame, text="M", font="Timesnewroman 30", bg="#404040", activebackground="#808080", fg="#404040",
                activeforeground="#808080", command=lambda: clicked(b3, "b3"))

    b4 = Button(game_frame, text="M", font="Timesnewroman 30", bg="#404040", activebackground="#808080", fg="#404040",
                activeforeground="#808080", command=lambda: clicked(b4, "b4"))
    b5 = Button(game_frame, text="M", font="Timesnewroman 30", bg="#404040", activebackground="#808080", fg="#404040",
                activeforeground="#808080", command=lambda: clicked(b5, "b5"))
    b6 = Button(game_frame, text="M", font="Timesnewroman 30", bg="#404040", activebackground="#808080", fg="#404040",
                activeforeground="#808080", command=lambda: clicked(b6, "b6"))

    b7 = Button(game_frame, text="M", font="Timesnewroman 30", bg="#404040", activebackground="#808080", fg="#404040",
                activeforeground="#808080", command=lambda: clicked(b7, "b7"))
    b8 = Button(game_frame, text="M", font="Timesnewroman 30", bg="#404040", activebackground="#808080", fg="#404040",
                activeforeground="#808080", command=lambda: clicked(b8, "b8"))
    b9 = Button(game_frame, text="M", font="Timesnewroman 30", bg="#404040", activebackground="#808080", fg="#404040",
                activeforeground="#808080", command=lambda: clicked(b9, "b9"))

    b1.grid(row=1, column=1, sticky=NSEW)
    b2.grid(row=1, column=3, sticky=NSEW)
    b3.grid(row=1, column=5, sticky=NSEW)

    b4.grid(row=3, column=1, sticky=NSEW)
    b5.grid(row=3, column=3, sticky=NSEW)
    b6.grid(row=3, column=5, sticky=NSEW)

    b7.grid(row=5, column=1, sticky=NSEW)
    b8.grid(row=5, column=3, sticky=NSEW)
    b9.grid(row=5, column=5, sticky=NSEW)


entry_one = Entry
entry_two = Entry


def multiplayer_game():
    global winner_window, main_menu_frame, entry_one, entry_two
    winner_window = Toplevel.destroy

    root.geometry("450x600")
    main_menu_frame.forget()
    main_menu_frame = LabelFrame(root, width=400, height=600)
    main_menu_frame.pack(fill=BOTH, expand=True)

    instruction_label = Label(main_menu_frame, text="Insert Players Names", font="TimesNewRoman 30", fg="grey",
                              anchor='center', pady=80)
    instruction_label.pack(anchor="center")

    player_1_label = Label(main_menu_frame, text="Player 1 Name")
    player_1_label.pack(pady=5)

    entry_one = Entry(main_menu_frame)
    entry_one.pack()

    player_2_name = Label(main_menu_frame, text="Player 2 Name")
    player_2_name.pack(pady=5)

    entry_two = Entry(main_menu_frame)
    entry_two.pack()

    get_names_button = Button(main_menu_frame, text="Get Names", command=get_names)
    get_names_button.pack(pady=10)


def get_names():
    global player_one_name, player_two_name

    player_one_name = entry_one.get()
    player_two_name = entry_two.get()
    start_game()


def escape(_):
    main_menu_frame.destroy()
    go_to_main_page()


root.bind('<Escape>', escape)
go_to_main_page()


root.mainloop()
