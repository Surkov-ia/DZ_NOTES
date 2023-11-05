import Function as f
import Menu

def run():
    inputFromUser = ""
    while inputFromUser != "7":
        Menu.menu()
        inputFromUser = input().strip()
        if inputFromUser == "1": # 1 - вывод всех заметок из файла
            f.show("all")
        if inputFromUser == "2": # 2 - добавление заметки
            f.add()
        if inputFromUser == "3": # 3 - удаление заметки
            f.show("all"),f.idEditDelShow("del")
        if inputFromUser == "4": # 4 - редактирование заметки
            f.show("all"),f.idEditDelShow("edit")
        if inputFromUser == "5": # 5 - выборка заметок по дате
            f.show("date")
        if inputFromUser == "6": # 6 - показать заметку по id
            f.show("id"),f.idEditDelShow("show")
        if inputFromUser == "7": #  7 - выход
            Menu.goodBuy()
            break