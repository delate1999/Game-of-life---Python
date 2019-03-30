import csv

# function which creates or overwrites file called 'state.csv' #
# which contains index, and state of every cell #
def save(env):
    with open('state.csv', 'w') as file:

        csv_writer = csv.writer(file)

        for i in range(0,len(env)):
            line = [i, env[i].state]
            csv_writer.writerow(line)

# function which reads state of the previous game #
# only state of the latest game can be loaded ! #
def read(env):
    with open('state.csv', 'r') as file:

        csv_reader = csv.reader(file)

        for row in csv_reader:
            env[int(row[0])].state = row[1]







