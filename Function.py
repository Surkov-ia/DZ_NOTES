import FileOperation
import CreateNote
import Menu
import colorama
from colorama import Fore, Back
colorama.init()
number = 4  # сколько знаков МИНИМУМ может быть в тексте заметки

def add():  # Добавление заметки в фаил
    note = Menu.createNote(number)
    array = FileOperation.readFile()
    for notes in array:
        if CreateNote.Note.getId(note) == CreateNote.Note.getId(notes):
            CreateNote.Note.setId(note)
    array.append(note)
    FileOperation.writeFile(array, "a")
    print(Fore.LIGHTYELLOW_EX + "Note added...")

def show(text):   # Поиск по дате
    logic = True
    array = FileOperation.readFile()
    if text == "date":
        date = input(Fore.LIGHTYELLOW_EX + "Enter the date in the format dd.mm.yyyy: ")
    for notes in array:
        if text == "all": # Показать все заметки
            logic = False
            print(CreateNote.Note.mapNote(notes))
        if text == "id": # Показать ID заметок
            logic = False
            print("ID: " + CreateNote.Note.getId(notes))
        if text == "date": # Поиск по дате
            logic = False
            if date in CreateNote.Note.getDate(notes):
                print(CreateNote.Note.mapNote(notes))
    if logic == True:
        print(Fore.LIGHTYELLOW_EX + "There is not a single note...")

def idEditDelShow(text):
    id = input(Fore.LIGHTYELLOW_EX + "Enter the id of the required note:")
    array = FileOperation.readFile()
    logic = True
    for notes in array:
        if id == CreateNote.Note.getId(notes):
            logic = False
            if text == "edit":  # изменение заметок по ID
                note = Menu.createNote(number)
                CreateNote.Note.setTitle(notes, note.getTitle())
                CreateNote.Note.setBody(notes, note.getBody())
                CreateNote.Note.setDate(notes)
                print(Fore.LIGHTYELLOW_EX + "The note has been changed...")
            if text == "del":  # Удаление заметки
                array.remove(notes)
                print(Fore.LIGHTYELLOW_EX + "The note has been deleted...")
            if text == "show": # Вывод заметки по указанному ID
                print(CreateNote.Note.mapNote(notes))
    if logic == True:
        print(Fore.LIGHTYELLOW_EX + "There is no such note, perhaps you entered the wrong id")
    FileOperation.writeFile(array, "a")