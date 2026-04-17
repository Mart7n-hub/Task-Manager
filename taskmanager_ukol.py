ukoly = []
def hlavni_menu() -> None:
    """ Funkce hlavního menu, která poskytuje možnosti pro přidání, zobrazení a odstranění úkolu. """
    while True:
        print("Správce úkolů - Hlavní menu")
        vstup = input("1. Přidat nový úkol\n2. Zobrazit všechny úkoly\n3. Odstranit úkol\n4. Konec programu\nVyberte možnost (1-4): ")

        if vstup =="1":
            pridat_ukol()
    
        elif vstup =="2":
            zobrazit_ukoly()

        elif vstup == "3":
            smazat_ukol()

        elif vstup == "4":
            break

        else:
            print("Zadejte 1 až 4 prosím.")

def pridat_ukol() -> None:
    """ Tato funkce má uživateli umožnit zadat název a popis nového úkolu a uložit jej do seznamu úkolů. """
    while True:
        nazev_ukolu = input("Zadejte název úkolu: ")
        if nazev_ukolu != "":
            break
        else:
            print("Název nesmí být prázdný!")

    while True:
        popis_ukolu = input("Zadejte popis úkolu: ")
        if popis_ukolu != "":
            break
        else:
            print("Popis nesmí být prázdný!")

    ukoly.append({"nazev": nazev_ukolu, "popis": popis_ukolu})
    print("Úkol byl přidán!")

def zobrazit_ukoly() -> None:
    """ Tato funkce má zobrazit všechny úkoly v seznamu. """ 
    if len(ukoly) != 0:
        for index, ukol in enumerate(ukoly):
            print(f"{index + 1}. {ukol['nazev']} - {ukol['popis']}")
    else:
        print("Seznam je prázdný.")

def smazat_ukol() -> None:
    """ Tato funkce má uživateli umožnit zadat číslo úkolu, který chce odstranit, a tento úkol odstranit. """
    if len(ukoly) == 0:
        print("Váš seznam je prázdný.")
        return

    zobrazit_ukoly()

    vstup = input("Zadej číslo úkolu, který chcete smazat: ")

    if vstup.isdigit():
        smazat = int(vstup)
        index = smazat - 1
        if 0 <= index < len(ukoly):
            ukoly.pop(index)
            print("Úkol byl smazán.")
        else:
            print("Neplatné číslo.")
    else:
        print("Zadejte číslo!")

if __name__ == "__main__":
    hlavni_menu()

