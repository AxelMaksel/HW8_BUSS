from logg import logging
import request_prof

def menu():
    logging.info("menu prof")
    while True:
        num_typ=input("что дальше?\n"
                      "1 - Посмотреть все записи\n"
                      "2 - Добавить специализацию в базу\n"
                      "3 - Редактировать специализацию\n"
                      "4 - Удалить специализацию\n"
                      "0 - выход\n")

        match num_typ:
            case "1":
                request_prof.prof_view()
            case "2":
                request_prof.prof_add()
            case "3":
                request_prof.prof_edit()
            case "4":
                request_prof.prof_del()
            case "0":
                break
            case _:
                print("Erro!!")

