from cell import Cell,win
from functions import *
from graphics import *
from ops_files import *
import time


env = []
tab = []
border = []
first_gen_size = 300

info()
set_borders(border,res)
set_env(env)

is_file_based(env, first_gen_size, tab)
is_automated(win, env, border)










