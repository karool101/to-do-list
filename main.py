import json
from datetime import datetime

PLIK = "tasks.json"

# ------------------ Operacje na pliku ------------------

def wczytaj_zadania():
    try:
        with open(PLIK, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def zapisz_zadania(tasks):
    with open(PLIK, "w") as f:
        json.dump(tasks, f, indent=4)

# ------------------ Funkcje programu ------------------

def dodaj_zadanie(tasks):
    tytul = input("Podaj treść zadania: ")
    priorytet = input("Podaj priorytet (niski/średni/wysoki): ")
    deadline = input("Podaj deadline (YYYY-MM-DD) lub Enter: ")

    task = {
        "title": tytul,
        "priority": priorytet,
        "deadline": deadline,
        "done": False
    }

    tasks.append(task)
    zapisz_zadania(tasks)
    print("✅ Dodano zadanie!")

def pokaz_zadania(tasks):
    if not tasks:
        print("Brak zadań.")
        return

    print("\n📋 Lista zadań:")
    for i, task in enumerate(tasks, 1):
        status = "✔" if task["done"] else " "
        deadline_info = ""

        if task["deadline"]:
            try:
                d = datetime.strptime(task["deadline"], "%Y-%m-%d")
                if d < datetime.now():
                    deadline_info = " ⚠️ (po terminie)"
                else:
                    deadline_info = f" (do {task['deadline']})"
            except:
                deadline_info = " (zła data)"

        print(f"{i}. [{status}] {task['title']} ({task['priority']}){deadline_info}")

def oznacz_wykonane(tasks):
    pokaz_zadania(tasks)
    try:
        nr = int(input("Podaj numer zadania do oznaczenia: "))
        tasks[nr - 1]["done"] = True
        zapisz_zadania(tasks)
        print("✅ Oznaczono jako wykonane!")
    except:
        print("❌ Błędny wybór")

def usun_zadanie(tasks):
    pokaz_zadania(tasks)
    try:
        nr = int(input("Podaj numer zadania do usunięcia: "))
        usuniete = tasks.pop(nr - 1)
        zapisz_zadania(tasks)
        print(f"🗑️ Usunięto: {usuniete['title']}")
    except:
        print("❌ Błędny wybór")

def filtruj(tasks):
    print("1. Tylko niewykonane")
    print("2. Tylko wykonane")
    wybor = input("Wybierz opcję: ")

    if wybor == "1":
        filtrowane = [t for t in tasks if not t["done"]]
    elif wybor == "2":
        filtrowane = [t for t in tasks if t["done"]]
    else:
        print("❌ Błędny wybór")
        return

    pokaz_zadania(filtrowane)

# ------------------ Menu ------------------

def menu():
    tasks = wczytaj_zadania()

    while True:
        print("\n--- MENEDŻER ZADAŃ ---")
        print("1. Dodaj zadanie")
        print("2. Pokaż zadania")
        print("3. Oznacz jako wykonane")
        print("4. Usuń zadanie")
        print("5. Filtruj zadania")
        print("6. Wyjdź")

        wybor = input("Wybierz opcję: ")

        if wybor == "1":
            dodaj_zadanie(tasks)
        elif wybor == "2":
            pokaz_zadania(tasks)
        elif wybor == "3":
            oznacz_wykonane(tasks)
        elif wybor == "4":
            usun_zadanie(tasks)
        elif wybor == "5":
            filtruj(tasks)
        elif wybor == "6":
            print("👋 Do zobaczenia!")
            break
        else:
            print("❌ Nieprawidłowa opcja")

# ------------------ Start programu ------------------

if __name__ == "__main__":
    menu()
