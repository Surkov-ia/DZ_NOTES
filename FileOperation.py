import CreateNote
import colorama
from colorama import Fore, Back
colorama.init()

def writeFile(array, mode):
    file = open("notes.csv", mode="w", encoding="utf-8")
    file.seek(0)
    file.close()
    file = open("notes.csv", mode=mode, encoding="utf-8")
    for notes in array:
        file.write(CreateNote.Note.toString(notes))
        file.write("\n")
    file.close

def readFile():
    try:
        array = []
        file = open("notes.csv", "r", encoding="utf-8")
        notes = file.read().strip().split("\n")
        for n in notes:
            splitN = n.split(";")
            note = CreateNote.Note(
                id = splitN[0], title = splitN[1], body = splitN[2], date = splitN[3])
            array.append(note)
    except Exception:
        print(Fore.LIGHTYELLOW_EX + "There are no saved notes...")
    finally:
        return array