import random


print("Curtis Preston")
print("16453897")
print()
print()

last = 0

stories = [
    ['With bloody hands, I say good-bye.', 'Frank Miller'],
    ['TIME MACHINE REACHES FUTURE!!! ... nobody there ...', 'Harry Harrison'],
    ['The baby\'s blood type? Human, mostly.', 'Orson Scott Card'],
    ['For sale: baby shoes, never worn.', 'Ernest Hemingway'],
    ['Corpse parts missing. Doctor buys yacht.', 'Margaret Atwood'],
    ['We kissed. She melted. Mop please!', 'James Patrick Kelly'],
    ['Starlet sex scandal. Giant squid involved.', 'Margaret Atwood'],
    ['Will this do (lazy writer asked)?', 'Ken McLeod'],
    ["I'm sorry, but there's not enough air in here for everyone. I’ll tell them you were a hero.", 'J. Matthew Zoss'],
    [
        'Waking Up To Silence: Deafening silence. I strain my ears, praying there might be someone else still alive. The only noise I hear are the voices in my head',
        'Mike Jackson'],
    [
        "Not In My Job Description: Make sure it's done by the end of the day Jones.\nBut, sir, it's not in my ....\nJust do it, and remember, no blood.",
        'Mike Jackson'],
    [
        'Empty Baggage: The trunk arrived two days later. He lifted the lid and froze, it was empty. No arms, no legs, no head, nothing. Where was she?',
        'Mike Jackson'],
    [
        'Forgot My Own Name: The hospital said it was concussion.\nMight be permanent memory loss.\nCan\'t even remember my own name - which is handy considering who I am.',
        'Mike Jackson']
]

fav = []

def amount():
    global last
    inp = int(input("how many words do you want the quotes to have"))
    results = []
    for x in range(0,len(stories)):
        if(len(stories[x][0].split(" "))==inp):
            display(x)
            results.append(x)
            last=x
    y = input("press enter to go back")



def display_all():
    global last
    for y in range(0,len(stories)):
        display(y)
        last=y
    y = input("press enter to go back")

def display(x):
    print('"' + stories[x][0] + '"')

    print("   -" + stories[x][1])


def dis_fav():
    print(fav)
    for x in range(0, len(fav)):
        display(fav[x])
    print("there are " + str(len(fav)) + " movies in your fav")
    y = input("press enter to go back")

def author_search():
    global last

    author=input("what author do you want to look at")
    sear  =input("what word")
    for x in range(0,len(stories)):
        if(author in stories[x][1]):
            if(sear in stories[x][0]):
                display(x)
                last=x
    y = input("press enter to go back")

def search():
    global last
    results = []
    x = input("what are you searching for: ")
    for y in range(0, len(stories)):
        if x in stories[y][0]:
            results.append(y)
            display(y)
            last = y
    y = input("press enter to go back")

def search_author():
    global last
    results = []
    x = input("what are you searching for: ")
    for y in range(0, len(stories)):
        if x in stories[y][1]:
            results.append(y)
            display(y)
            last = y
    y = input("press enter to go back")

def keep():
    global fav
    fav.append(last)
    display(last)
    print("is added to your fav")
    y = input("press enter to go back")


def dis_rand():
    global fav
    global last
    x = random.randint(0, len(stories[0]))
    display(x)
    last = x
    y = input("press enter to go back")


def main():
    while True:
        print("""Welcome to Quote search engine
    s - search Quotes
    a - search authors
    f - display fav
    c - clear fav
    q - quit
    k - keep the last displayed result
    n - find a story with a certain amount of words 
    r - display a random Quote
    d - display all quotes
    as- display quotes from a certain author with certain words
    """)

        x = input("command: ")
        if x in (['s',"S"]):
            search()
        if x in (['q','Q']):
            quit()
        if x == 'f':
            dis_fav()
        if x == 'k':
            keep()
        if x in (["r", "R"]):
            dis_rand()
        if x in (['a','A']):
            search_author()
        if x in (["d","D"]):
            display_all()
        if x =='n':
            amount()
        if x =='as':
            author_search()



main()