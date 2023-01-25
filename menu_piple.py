from logg import logging
import request_piple

def menu():
    logging.info("menu piple")
    while True:
        num_typ=input("что дальше?\n"
                      "1 - Посмотреть все записи\n"
                      "2 - Добавить работника в базу\n"
                      "3 - Редактировать работника\n"
                      "4 - Удалить работника\n"
                      "0 - выход\n")

        match num_typ:
            case "1":
                request_piple.piple_view()
            case "2":
                request_piple.piple_add()
            case "3":
                request_piple.piple_edit()
            case "4":
                request_piple.piple_del()
            case "0":
                break
            case _:
                print("Erro!!")

