import json

while True:
    print("TODO:\n操作方法:1todo見る 2todo追加 3todo削除 4todo終了")
    user_enter = input("user enter: ")

    if user_enter == "1":
        print("todo見る")
        with open("todo.json", "r", encoding="utf-8") as file:
            todo = json.load(file)
        print(todo)   
    elif user_enter == "2":
        print("todo追加")
        with open("todo.json", "r", encoding="utf-8") as file:
            todo = json.load(file)
        todo.append(input("todo: "))
        with open("todo.json", "w", encoding="utf-8") as file:
            json.dump(todo, file)
    elif user_enter == "3":
        print("todo削除")
        with open("todo.json", "r", encoding="utf-8") as file:
            todo = json.load(file)
        todo.pop(int(input("todo番号: ")))
        with open("todo.json", "w", encoding="utf-8") as file:
            json.dump(todo, file)
    elif user_enter == "4":
        print("todo終了")
        break

    #最初に戻る
    continue
