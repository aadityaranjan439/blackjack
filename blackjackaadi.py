import random
import tkinter

mainWindow = tkinter.Tk()
mainWindow.title("Black Jack game")
mainWindow.geometry("640x480")

''' load cards function : function to load cards from file in same directory
for other directory specify the path'''


def load_cards(card_images):
    suits = ['heart', 'diamond', 'spade', 'club']
    face_cards = ['jack', 'king', 'queen']
    extension = 'png'
    for suit in suits:
        for card in range(1, 11):
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            card_image = tkinter.PhotoImage(name=name)
            card_images.append((card, card_image))
        for card in face_cards:
            name = 'cards/{}_{}.{}'.format(str(card), suit, extension)
            card_image = tkinter.PhotoImage(name=name)
            card_images.append((10, card_image))


def deal_card(frame):

    next_card = deck.pop()

    tkinter.Label(frame, image=next_card[1], relief='raised').grid(row=0, column=3, rowspan=2, sticky='nsew')
    return next_card


def deal_dealer():

    deal_card(dealer_card_frame)


def deal_player():
    deal_card(player_card_frame)


# creating variable to print result
result_text = tkinter.StringVar()
result = tkinter.Label(mainWindow, textvariable=result_text)
result.grid(row=0, column=0, sticky='ew', columnspan=4)

# creating card frame
card_frame = tkinter.Frame(mainWindow, relief='sunken', borderwidth=1, background='grey')
card_frame.grid(row=1, column=0, rowspan=2, columnspan=4)

# dealer card frame
dealer_card_frame = tkinter.Frame(card_frame, relief='sunken', borderwidth=1, background='black')
dealer_card_frame.grid(row=0, column=1, rowspan=2)
dealer_score = tkinter.IntVar()
dealer_score_val = tkinter.Label(dealer_card_frame, textvariable=dealer_score, background='grey', fg='orange')
dealer_score_text = tkinter.Label(dealer_card_frame, text='Dealer score: ', background='grey', fg='orange')
dealer_score_text.grid(row=0, column=0, sticky='ew')
dealer_score_val.grid(row=1, column=0, sticky='ew')

# player card frame
player_card_frame = tkinter.Frame(card_frame, relief='sunken', borderwidth=1, background='grey')
player_card_frame.grid(row=2, column=1, rowspan=2)
player_score = tkinter.IntVar()
tkinter.Label(player_card_frame, text='Player score: ', background='grey', fg='orange').grid(row=2, column=0)
tkinter.Label(player_card_frame, textvariable=player_score, background='grey', fg='orange').grid(row=3, column=0)

# creating button frame and buttons
button_frame = tkinter.Frame(mainWindow, relief='sunken', borderwidth=1, background='black')
button_frame.grid(row=3, column=0, rowspan=2, columnspan=4, sticky='ew')
dealer_button = tkinter.Button(button_frame, text='Dealer', command=deal_dealer)
dealer_button.grid(row=0, column=0, sticky='ew')
player_button = tkinter.Button(button_frame, text='Player', command=deal_player).grid(row=0, column=1, sticky='ew')

# loading cards in cards and creating a different list deck identical to cards
count = 0
cards = []
load_cards(cards)
deck = list(cards)
random.shuffle(deck)
# creating empty dealer hand and player hand lists
dealer_hand = []
player_hand = []

mainWindow.mainloop()
