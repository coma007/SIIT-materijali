import tkinter as tk
from tkinter import filedialog
import tkinter.font as tkFont
import os
import sys
import time
from PIL import Image, ImageTk  # pip install --upgrade Pillow

from board import Board
from search import *
from state import *


def load_board_from_file(filename=None):
    if filename is None:
        filename = filedialog.askopenfilename(defaultextension='.brd',
                                                filetypes=(('board files', '*.brd'), ('All files', '*.*')),
                                                initialdir="./boards")
    board.load_from_file(filename)
    return filename


def save_board_to_file():
    filename = filedialog.asksaveasfilename(defaultextension='.brd',
                                              filetypes=(('board files', '*.brd'), ('All files', '*.*')))
    board.save_to_file(filename)


def load_board(from_file=None):      # filename passed when reopening (resetting) same file
    load_board_from_file(from_file)
    display_board()


def clear():
    board.clear()
    display_board()


def reset():
    for row in range(rows):
        for col in range(cols):
            delete_texts(row, col)
    display_board()


def key(event):
    k = event.keysym.lower()
    row, col, new_row, new_col = board.move_player_keyboard(k)
    if board.find_position('r') != (None, None):
        update_board(row, col)
        update_board(new_row, new_col)


def switch_cell(event, row=None, col=None):
    if row is None and col is None:
        cx = event.x
        cy = event.y
        col = cx // cell_size  # column
        row = cy // cell_size  # row
    board.switch_cell(row, col)
    update_board(row, col)


def update_board(row, col):
    data = board.data
    text = board.text
    delete_elems(row, col)
    elem = data[row][col]
    d, i = elem, elem
    if ',' in elem:
        s = elem.split(',')
        d = s[0]
        i = s[1]

    if d in board_to_colors:
        draw_rectangle(row, col, board_to_colors[d])
    if i in board_to_icons:
        icon = icons[board_to_icons[i]]
        draw_icon(row, col, icon)

    if len(text[row][col]) > 0:
        draw_text(row, col, text[row][col])
    else:
        delete_texts(row, col)


def get_cell_rectangle(row, col):
    return col * cell_size, row * cell_size, (col + 1) * cell_size, (row + 1) * cell_size


def draw_rectangle(row, col, color, width=1):
    rect = get_cell_rectangle(row, col)
    elem_id = canvas.create_rectangle(rect, width=width, fill=color, outline='gray')
    save_elem_id(elem_id, row, col)


def draw_text(row, col, text):
    rect = get_cell_rectangle(row, col)
    l = tk.Label(canvas, text=text, background='white')
    l.bind('<Button-1>', lambda event: switch_cell(event, row, col))
    elem_id = canvas.create_window(rect[0] + cell_size/2, rect[1] + cell_size/2, height=cell_size/3, window=l)
    save_elem_id(elem_id, row, col)
    save_text_id(elem_id, row, col)


def draw_icon(row, col, icon):
    rect = get_cell_rectangle(row, col)
    elem_id = canvas.create_image(rect[0]+2, rect[1]+2, image=icon, anchor=tk.NW)
    canvas.icons[elem_id] = icon
    save_elem_id(elem_id, row, col)


def save_elem_id(elem_id, row, col):
    if len(grid_elem_ids[row][col]) == 0:
        grid_elem_ids[row][col] = []
    grid_elem_ids[row][col].append(elem_id)


def save_text_id(elem_id, row, col):
    if len(grid_text_ids[row][col]) == 0:
        grid_text_ids[row][col] = []
    grid_text_ids[row][col].append(elem_id)


def delete_elems(row, col):
    if 0 <= row < rows and 0 <= col < cols:
        for elem_id in grid_elem_ids[row][col]:
            canvas.delete(elem_id)
            if elem_id in canvas.icons:
                del canvas.icons[elem_id]
        grid_elem_ids[row][col] = []


def delete_texts(row, col):
    if 0 <= row < rows and 0 <= col < cols:
        for elem_id in grid_text_ids[row][col]:
            canvas.delete(elem_id)
            if elem_id in canvas.icons:
                del canvas.icons[elem_id]
        grid_text_ids[row][col] = []
        board.text[row][col] = ''


def display_board():
    canvas.delete(tk.ALL)
    for row in range(len(board.data)):
        for col in range(len(board.data[0])):
            update_board(row, col)


def make_menu(win):
    top = tk.Menu(win)  # win=top-level window
    win.config(menu=top)  # set its menu option
    file_menu = tk.Menu(top)
    file_menu.add_command(label='Open...', command=load_board, underline=0)
    file_menu.add_command(label='Save...', command=lambda: save_board_to_file(), underline=0)
    file_menu.add_command(label='Quit', command=sys.exit, underline=0)
    top.add_cascade(label='File', menu=file_menu, underline=0)
    edit = tk.Menu(top, tearoff=False)
    edit.add_command(label='Clear', command=clear, underline=0)
    edit.add_separator()
    top.add_cascade(label='Edit', menu=edit, underline=0)

processed = None
path = None

search_class_map = {
    "BFS": BreadthFirstSearch,
    "DFS": DepthFirstSearch,
    "IDFS": IterativeDepthFirstSearch,
    "GS": GreedySearch,
    "A*": AStarSearch 
}

def get_search_class():
    return search_class_map[search_class_text.get()]

# funkcija koja se poziva na dugme SEARCH
def do_search():
    global processed, path
    reset()
    # koju strategiju pretrage koristiti
    search_class = get_search_class()
    search = search_class(board)
    print(board.find_all_positions('b'))
    # kog "agenta" koristiti
    initial_state = RobotState

    # pokreni pretragu, meri vreme izvrsavanja
    start = time.perf_counter()
    path, processed, states = search.search(initial_state)
    end = time.perf_counter()

    print('-'*15, 'DONE', '-'*15)
    print('Time: {0} ms'.format(end - start))
    print('Processed nodes: {0}'.format(len(processed)))
    print('States left: {0}'.format(len(states)))
    if path is None:
        # nije bilo resenja
        print('-'*15, 'NO SOLUTION', '-'*15)
    else:
        # ako je bilo resenja, iscrtaj ga
        for idx, p in enumerate(path):
            text = board.text[p[0]][p[1]]
            if len(text) == 0:
                text += str(idx)
            else:
                text += ',' + str(idx)
            board.text[p[0]][p[1]] = text
            update_board(p[0], p[1])


# funkcija za debagovanje, u eksperimentalnoj fazi :)
def move_icon(from_position, to_position, has_box=None):
    f = board.data[from_position[0]][from_position[1]]
    t = board.data[to_position[0]][to_position[1]]
    if ',' in f:
        s = f.split(',')
        f = s[0]
        if has_box:
            t = 'b,' + s[1]
        else:
            t += ',' + s[1]
    else:
        t += ',' + f
        f = '.'
    board.data[from_position[0]][from_position[1]] = f
    update_board(from_position[0], from_position[1])
    board.data[to_position[0]][to_position[1]] = t
    update_board(to_position[0], to_position[1])
    root.update()


def debug():
    global processed
    reset()
    position = board.find_position('r')
    for idx, p in enumerate(processed):
        move_icon(position, p.position, hasattr(p, 'has_box') and p.has_box)
        position = p.position
        time.sleep(0.2)

#  main program #
rows = 20  # broj redova table
cols = 20  # broj kolona table
cell_size = 40  # velicina celije

board = Board(rows=rows, cols=cols)

grid_elem_ids = [[[]] * cols for _ in range(rows)]
grid_text_ids = [[[]] * cols for _ in range(rows)]

# mapiranje sadrzaja table na boju celije
board_to_colors = {
    '.': 'white',
    'w': 'gray',
    'g': 'orangered',
    'b': 'blue',
    'y': 'yellow'
    }
# mapiranje sadrzaja table na ikonicu
board_to_icons = {
    'r': 'robot.png',
    'f': 'fire.png'
}


root = tk.Tk()
root.title('ORI - Pretrage')
make_menu(root)  # make window menu
ui = tk.Frame(root, bg='white')  # main UI
ui2 = tk.Frame(root, bg='white')

# define the user interaction widgets
canvas = tk.Canvas(root, width=cols * cell_size + 1, height=rows * cell_size + 1,
                   highlightthickness=0, bd=0, bg='white')

# load icons
canvas.icons = dict()
icons = dict()
for f in os.listdir('icons'):
    icon = Image.open(os.path.join('icons', f))
    icon = icon.resize((cell_size - 2, cell_size - 2), Image.ANTIALIAS)  # resize icon to fit cell
    icon = ImageTk.PhotoImage(icon)
    icons[f] = icon

search_class_text = tk.StringVar(ui)
search_class_text.set("BFS")

# create buttons
search_option = tk.OptionMenu(ui, search_class_text, *search_class_map.keys())
start_button = tk.Button(ui, text='SEARCH', width=10, command=do_search)
restart_button = tk.Button(ui, text='RESET', width=10, command=reset)
clear_button = tk.Button(ui, text='CLEAR ALL', width=10, command=clear)
debug_button = tk.Button(ui, text='DEBUG', width=10, command=debug)
stat_report = tk.Label(root, text='      ', bg='white', justify=tk.LEFT, relief=tk.GROOVE,
                       font=tkFont.Font(weight='bold'))

# add buttons to UI
search_option.grid(row=0, column=0, padx=10, pady=10)
start_button.grid(row=1, column=0, padx=10, pady=10)
clear_button.grid(row=2, column=0, padx=10, pady=10)
clear_button.grid(row=3, column=0, padx=10, pady=10)
restart_button.grid(row=4, column=0, padx=10, pady=10)
debug_button.grid(row=5, column=0, padx=10, pady=10)

# put everything on the screen
display_board()
canvas.bind('<Button-1>', switch_cell)  # bind left mouse click event to function switch_cell
root.bind('<Key>', key)  # bind keyboard event to function key
ui.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.BOTH)
canvas.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH)
ui2.pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH, anchor=tk.W)
stat_report.pack(side=tk.RIGHT, expand=tk.NO, fill=tk.NONE)

# load default board
load_board('boards/zadatak1.brd')

root.mainloop()
