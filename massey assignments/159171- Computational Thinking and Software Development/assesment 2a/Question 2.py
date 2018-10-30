import random
import os.path

print("Curtis Preston")
print("16453897")
print()
print()

running = True
favourites=[]
loaded=False;
movies_list = []
last = ""

def closed():
    global loaded
    loaded = False


def need_load():
    print("you need to load the movie file first")
    x=input("press enter to go back")


def load():
    global movies_list
    global loaded
    file_name=input("enter the name of the file you want to open")
    if os.path.isfile(file_name):
        file = open(file_name, "r")  # open the file
        movies_list = file.readlines()  # load each line into a list
        file.close()  # close the file
    else:
        file = open("movies.txt", "r")  # open the file
        movies_list = file.readlines()  # load each line into a list
        file.close()

    movies_list = [movie.strip() for movie in movies_list]

    loaded=True
    print("loaded file")
    x=input("press enter to continue")
    return


def rand():
    global last
    x=random.choice(movies_list)
    print(x)
    last = x
    inp = input("""b - do you want to go back
r - do you want to see another random: R
f - do you want to add this to your favourites
command: """)
    if (inp == "r"):
        rand()
    elif(inp=='f'):
        keep()
        inp = input("""B - go back
R - see another random movie
command: """)
        if (inp == "r"):
            rand()
        elif (inp == 'b'):
            last = x
            return
    elif(inp=='b'):
        last = x
        return


def search():
    global movies_list
    global last
    func=input("what do you want to search for")
    for x in range(0,len(movies_list)):
        if func in movies_list[x]:
            print(movies_list[x])
            last = movies_list[x]
            print()
    i = input("""
    B - back 
    S - search again
    
    command:""")
    if i =="b":
        return
    elif i=='s':
        search()


def start_with():
    global last
    global movies_list
    result = []
    x = input("what does it begin with")
    for y in range(0,len(movies_list)):
        z = movies_list[y][0:len(x)]
        if(x == z):
            print(movies_list[y])
            result.append(movies_list[y])
            last=movies_list[y]
    num = len(result)
    if(num>0):
        x = input("press enter to go back")
        return
    else:
        print("sorry there are no movies starting with :"+x)
        x=input("press enter to go back")
        return



def keep():
    global favourites
    global last
    if not(last==""):
        favourites.append(last)
        print("adding "+last+" to your favourites list")
    else:
        print("not much point in that")
    x=input("press enter to continue")
    last = ""
    return

def fav_display():
    global favourites
    if(len(favourites)>0):
        for x in range(0,len(favourites)):
            print(str(x+1)+": "+favourites[x])
    else:
        print("there is nothing in your favourites")
    x=input("press enter to go back")


def fav_clear():
    global favourites
    favourites.clear()
    print("favourites cleared")
    x = input("press enter to go back")

def main():
    global loaded
    global last
    while running == True:
        print("""
*** Movie Title Explorer ***
l – load file of movie titles
r – random movie
s – search
sw – starts with
k – keep - save the last displayed movie title to your favourites
f – favourites display
c – clear favourites
q – quit
    """)
        x=input("command: ")

        if loaded:

            if(x=="r"):
                rand()

            if(x=="s"):
                search()

            if(x=="q"):
                closed();

            if(x=='k'):
                keep()

            if(x=='f'):
                fav_display()

            if(x=='c'):
                fav_clear()

            if(x=='sw'):
                start_with()
        else:
            if(x == 'l'):
                load()
            else:
                need_load()

main()