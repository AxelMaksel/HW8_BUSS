import menu_buss as mb
import menu_piple as mp
import menu_prof as mpr

def menu():
    while True:
        num_typ=input("Выбери пунк\n"
                      "1 - Автобусы\n"
                      "2 - Работники\n"
                      "3 - Специальности\n"
                      "0 - выход\n")

        match num_typ:
            case "1":
                mb.menu()
            case "2":
                mp.menu()
            case "3":
                mpr.menu()
            case "0":
                break
            case _:
                print("Erro!!")

menu()