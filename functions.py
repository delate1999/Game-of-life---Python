from random import randint
from cell import Cell
from graphics import *
from ops_files import *

# variable which defines resolution of the graphics window #
# counted in small squares #
res = 50

# creating grid consisting of cells #
# at the beginning all cells are 'dead' #
# cell has size 10 pixels #

def set_env(env):
    for x in range(res):
        for y in range(res):
            env.append(Cell(x*10 + 5, y*10 + 5,'dead',0))

#randomly chose index of one cell, all cells are different#
def rand_cell(tab):
    i = randint(0,res*res)
    if i not in tab:
        tab.append(i)
    else:
        rand_cell(tab)

# setting alive cells which were chosed in rand_cell() #
def set_alive(tab,env):
    for i in tab:
        env[i].state = 'alive'

# function which clears graphic window #
def clear(win):
    for item in win.items[:]:
        item.undraw()

# function which creates borders of graphic window #
# borders are allways black, because they consist of permamently dead cells #
# it makes counting neighbours easier #
def set_borders(border,res):
    for i in range(0, res):
        border.append(i)

    for i in range(res*res - 51, res*res):
        border.append(i)

    for i in range(0, res*res - 51, res):
        border.append(i)

    for i in range(res-1, res*res -1, res):
        border.append(i)

# function which counts how many neighbours cell has #
def check_mates(env,i):
    if env[i + 1].state == 'alive':
        env[i].mates += 1
    if env[i - 1].state == 'alive':
        env[i].mates += 1
    if env[i + res].state == 'alive':
        env[i].mates += 1
    if env[i + res + 1].state == 'alive':
        env[i].mates += 1
    if env[i + res - 1].state == 'alive':
        env[i].mates += 1
    if env[i - res - 1].state == 'alive':
        env[i].mates += 1
    if env[i - res + 1].state == 'alive':
        env[i].mates += 1
    if env[i - res].state == 'alive':
        env[i].mates += 1

# function which runs the Game of Life in automated mode #
# user cannot control the speed, he can only save by pressing 's' #
def automat(win,env,res,border):
    while win.checkKey() is not 's':
        clear(win)
        for i in range(0, len(env)):
            env[i].draw_cell()
        update(1)

        for i in range(res, len(env) - (res + 1)):

            for q in border:
                env[q].state = 'dead'

            check_mates(env, i)

            if env[i].state == 'alive':
                if env[i].mates == 2 or env[i].mates == 3:
                    env[i].state = 'alive'
                else:
                    env[i].state = 'dead'

            if env[i].state == 'dead':
                if env[i].mates == 3:
                    env[i].state = 'alive'

            env[i].mates = 0
    save(env)

# function which runs Game in manual mode, in which user #
# can control the speed, virtually he changes frames by pressing key (let's say 'space') #
# and saves by pressing 's' #
def manual(win,env,res,border):
    while win.getKey() is not 's':
        clear(win)
        for i in range(0, len(env)):
            env[i].draw_cell()

        for i in range(res, len(env) - (res + 1)):

            for q in border:
                env[q].state = 'dead'

            check_mates(env, i)

            if env[i].state == 'alive':
                if env[i].mates == 2 or env[i].mates == 3:
                    env[i].state = 'alive'
                else:
                    env[i].state = 'dead'

            if env[i].state == 'dead':
                if env[i].mates == 3:
                    env[i].state = 'alive'

            env[i].mates = 0
    save(env)

# function which asks the user if he wants to run Game in automated mode #
# if yes, then it is started with 3s delay, so he can switch to graphic window #
def is_automated(win, env, border):
    print("Czy chcesz samemu kontrolowac klatki ? 1/0 ")
    switch = input()
    if switch == 0:
        time.sleep(2)
        automat(win, env, res, border)
    if switch == 1:
        manual(win, env, res, border)

# function which asks the user if he wants to read the state of game #
#  from the file called state.csv #
def is_file_based(env, first_gen_size, tab):
    print("Czy chcesz wczytac stan poprzedniej sesji ? 1/0")
    switch = input()
    if switch == 1:
        read(env)
    if switch == 0:
        for q in range(first_gen_size):
            rand_cell(tab)
        set_alive(tab, env)

# function which prints to the console basic instructions #
def info():
    print('To jest "Gra w Zycie" wedlug klasycznych zasad')
    print('Program ma mozliwosc wczytywania danych z pliku')
    print('Ma rowniez dwa mozliwe tryby dzialania:')
    print('- Automatyczny w ktorym uzytkownik nie kontroluje klatek')
    print('- Manualny w ktorym uzytkownik sam, naciskajac spacje zmienia klatki')
    print('W obydwoch trybach istnieje mozliwosc zapisu do pliku')
    print('Instrukcja : ')
    print("'1' - Tak")
    print("'0' - Nie")
    print("'space' - natepna klatka animacji w trybie manualnym")
    print("'s' - zapis stanu i automatyczne wyjscie z programu")
    print("***************************************************************************************")






