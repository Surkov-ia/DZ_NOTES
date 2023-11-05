import CreateNote
import colorama
from colorama import Fore, Back , Style
colorama.init()

def createNote(number): # Описание создания записки
    title = checkLenTextInput(
        input(Fore.LIGHTYELLOW_EX + "Enter the name of the note: "), number)
    body = checkLenTextInput(
        input(Fore.LIGHTYELLOW_EX + "Enter a Description of the note: "), number)
    return CreateNote.Note(title=title, body=body)

def menu():  # описание меню программы
    # print(Back.BLACK + Fore.LIGHTYELLOW_EX +
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX +
          "\n Notes"
          "\n"
          "\n 1 - output all notes from a file                 "
          "\n 2 - adding a note                             "
          "\n 3 - deleting a note                               "
          "\n 4 - edit a note                        "
          "\n 5 - selection of notes by date                        "
          "\n 6 - show a note by id                      "
          "\n 7 - exit                                        "
          "\n"
          "\n Enter the function number: ")

def checkLenTextInput(text, n): # Проверка на длину символов
    while len(text) <= n:
        print(Fore.LIGHTYELLOW_EX + f"The text must be more than {n} characters\n")
        text = input(Fore.LIGHTYELLOW_EX + "Enter the text: ")
    else:
        return text

def goodBuy(): # Сообщение при выходе из программы
    print(Fore.LIGHTYELLOW_EX + "The program has finished its work")