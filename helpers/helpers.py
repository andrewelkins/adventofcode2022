import os


def get_filename(day):
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, day + '/input.txt')
    return filename


def parse_input(filename):
    with open(filename) as file:
        input_list = file.read().splitlines()
    return input_list

def create_folder_structure():
    for i in range(1, 26):
        if i < 10:
            day = '0' + str(i)
        else:
            day = str(i)
        
        if not os.path.exists(day):
            os.mkdir(day)

        os.popen("cp -n template/puzzle.py {}/puzzle.py".format(str(day))) 

            
def check_input_exists(day):
    if not os.path.exists(day + '/input.txt'):
        FileNotFoundError('Input file not found for day ' + day)