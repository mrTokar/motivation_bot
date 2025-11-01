import os

PATH_TO_DIR = os.getcwd() + "\\source"

def select_file(*extensions: str, comment="") -> str:
    while True:
        #print list
        print(f"Выбитие необходимый файл {comment} из предложенных ниже. Если нужный файл отсутствует, добавьте его в дирректорию")
        print(PATH_TO_DIR)
        i = 1
        for file in os.listdir(PATH_TO_DIR):
            if len(extensions) == 0 or file.endswith(extensions):
                print(f"{i}. {file}")
                i += 1

        #print warning
        if (i == 1):
            print("WARNING:", end=" ")
            if len(extensions) >0:
                print("В дирректории отсутствуют файлы с необходимыми расширениями:", *extensions)
            else:
                print("В дирректории отсутствуют файлы.")
            print("Добавьте файл и повторите попытку.")

        #user input
        print("\nВведите 0 для обновления списка файлов")
        usr_input = input(">>> ").strip()
        if usr_input.isdigit() and 1 <= int(usr_input) < i:
            selected_file = os.listdir(PATH_TO_DIR)[int(usr_input) - 1]
            return os.path.join(PATH_TO_DIR, selected_file)

def request(comment, default_answer=True) -> bool:
    print(comment, end="")
    if default_answer:
        print(" [Y/n]: ", end="")
    else:
        print(" [y/N]: ", end="")

    usr_input = input().strip().lower()
    if default_answer:
        if usr_input in ["n", "no"]:
            return False
        return True
    else:
        if usr_input in ["y", "yes"]:
            return True
        return False

if __name__ == "__main__":
    print(select_file(".md", comment="для тестирования"))
