import json
import sys
from pathlib import Path

DATA_FILE = Path("todos.json")


def load_todos():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_todos(todos):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=2)


def add_todo(title):
    todos = load_todos()
    todos.append({"title": title, "done": False})
    save_todos(todos)
    print(f"เพิ่มงานแล้ว: {title}")


def list_todos():
    todos = load_todos()
    if not todos:
        print("ยังไม่มีงานในรายการ")
        return
    for i, todo in enumerate(todos, start=1):
        mark = "x" if todo["done"] else " "
        print(f"{i}. [{mark}] {todo['title']}")


def main():
    if len(sys.argv) < 2:
        print('วิธีใช้: python todo.py add "ชื่องาน" | list')
        return

    command = sys.argv[1]

    if command == "add" and len(sys.argv) >= 3:
        add_todo(sys.argv[2])
    elif command == "list":
        list_todos()
    else:
        print("คำสั่งไม่ถูกต้อง")


if __name__ == "__main__":
    main()