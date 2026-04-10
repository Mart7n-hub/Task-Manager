tasks = []
def pridat_ukol():
    while True:
        task_name = input("Zadejte název úkolu: ")
        task_des = input("Zadejte popis úkolu: ")

        if task_name != "" and task_des != "":
            tasks.append({"name": task_name, "description": task_des})
            print("Úkol byl přidán!")
            break
        else:
            print("Zadali jste špatně...")

def zobrazit_seznam():
    if len(tasks) != 0:
        for index, task in enumerate(tasks):
            print(f"{index + 1}. {task['name']} - {task['description']}")
    else:
        print("Seznam je prazdny.")

def smazat_ukol():
    if len(tasks) == 0:
        print("Váš seznam je prázdný.")
        return

    zobrazit_seznam()

    delete = int(input("Zadej cislo ukolu, ktere chcete smazat: "))
    index = delete - 1

    if 0 <= index < len(tasks):
        tasks.pop(index)
        print("Úkol byl smazán.")
    else:
        print("Neplatné číslo.")

while True:
    print("Správce ukolu - Hlavni menu")
    vstup = int(input("1. Přidat nový úkol\n2. Zobrazit všechny úkoly\n3. Odstranit úkol\n4. Konec programu\nVyberte moznost (1-4): "))

    if vstup ==1:
        pridat_ukol()
    
    elif vstup ==2:
        zobrazit_seznam()

    elif vstup == 3:
        smazat_ukol()

    elif vstup == 4:
        break

    else:
        print("Zadejte 1 az 4 prosim.")
