import json
import os
from datetime import datetime

from note_controller import NoteController


def main():
    controller = NoteController()

    while True:
        print("\n===== Меню =====")
        print("1: Просмотр заметок")
        print("2: Добавление новой заметки")
        print("3: Редактирование заметок")
        print("4: Удаление заметок")
        print("5: Выход из меню")

        choice = input("Выберите действие: ")

        if choice == '1':
            controller.display_notes()
        elif choice == '2':
            controller.add_note()
        elif choice == '3':
            controller.edit_note()
        elif choice == '4':
            controller.delete_note()
        elif choice == '5':
            print("Выход из программы.")
            break
        else:
            print("Такого варианта не существует. Пожалуйста, выберите существующий вариант.")


if __name__ == "__main__":
    main()