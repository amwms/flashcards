import json
import os

def press_q_to_quit():
    print("(Press q to quit)")
    while(True):
        i = input()
        if i == "q":
            return


def add_flashcard(card_title, card_label, card_text):
    json_result = {
         "card_title": card_title,
         "card_text": card_text,
      }

    with open('db/db.json', 'r') as open_file:
        json_object = json.load(open_file)

        if card_label in json_object:
            json_object[card_label].append(json_result)
        else:
            json_object[card_label] = []
            json_object[card_label].append(json_result)
        
        with open('db/db.json', 'w') as db_file:
            json.dump(json_object, db_file, indent=4)

def list_decks():
    print("\u001b[1m"+"Decks:"+"\u001b[0m")
    with open('db/db.json', 'r') as open_file:
        json_object = json.load(open_file)
        
        for label in json_object:
            print(label)

    print("")
    press_q_to_quit()
    return

def show_deck(deck):
    os.system('clear') 
    print("\u001b[1m" + deck + ":\u001b[0m")
    print(" - - - - - - - - - - - - - - - -")       

    with open('db/db.json', 'r') as open_file:
        json_object = json.load(open_file)
        
        for card in json_object[deck]:
            print(card["card_title"] + "   " + card["card_text"])

    print("")
    press_q_to_quit()
    return


def prompt_add_flashcard():
    while(True):
        card_title = input("Input the card title:") 
        card_label = input("Input what deck should the card be added to:") 
        card_text = input("Input the card description:") 

        add_flashcard(card_title, card_label, card_text)

        print("\u001b[32;1mCard Added to deck " + card_label + "\u001b[0m")

        next_action = input("Do you want to add another card? y/n")
        if next_action == "n":
            return

def prompt_show_deck():
    while(True):
        deck = input("Which deck would you like to see? (or q to quit)")
        if deck == "q":
            return

        with open('db/db.json', 'r') as open_file:
            json_object = json.load(open_file)
            if deck in json_object:
                show_deck(deck)
            else:
                print("\u001b[31;1m"+"No such deck exists!"+"\u001b[0m")


def list_deck_cards():
    while(True):
        os.system('clear') 
        print("\u001b[1m"+"Actions"+"\u001b[0m")
        print("(1) Show deck")
        print("(2) List decks")
        print("(3) Back")

        action_id = input("\u001b[36;1m"+"What do you want to do?"+"\u001b[0m")
        action_id = int(action_id)

        if action_id == 1:
            prompt_show_deck()
        elif action_id == 2:
            list_decks()
        elif action_id == 3:
            return
        else:
            print("That is not a correct action. Please choose a correct action:")

def add_flashcards():
    while(True):
        os.system('clear') 
        print("\u001b[1m"+"Actions:"+"\u001b[0m")
        print("(1) Add card")
        print("(2) List decks")
        print("(3) Back")

        action_id = input("\u001b[36;1m"+"What do you want to do?"+"\u001b[0m")
        action_id = int(action_id)

        if action_id == 1:
            prompt_add_flashcard()
        elif action_id == 2:
            list_decks()
        elif action_id == 3:
            return
        else:
            print("That is not a correct action. Please choose a correct action:")

def control():
    while(True):
        os.system('clear') 
        print("\u001b[1m"+"Actions:"+"\u001b[0m")
        print("(1) Add cards")
        print("(2) List decks")
        print("(3) List cards in deck")
        print("(4) Quit")

        action_id = input("\u001b[36;1m"+"What do you want to do?"+"\u001b[0m")
        action_id = int(action_id)


        if action_id == 1:
            os.system('clear') 
            add_flashcards()
        elif action_id == 2:
            os.system('clear')
            list_decks()
        elif action_id == 3:
            os.system('clear')
            list_deck_cards()
        if action_id == 4:
            return
        else:
            print("That is not a correct action id. Please choose a correct action:")

control()