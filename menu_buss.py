from logg import logging
import request_buss

def menu():
    logging.info("menu buss")
    while True:
        num_typ=input("что дальше?\n"
                      "1 - Посмотреть все записи\n"
                      "2 - Добавить автобус в базу\n"
                      "3 - Редактировать автобус\n"
                      "4 - Удалить автобус\n"
                      "0 - выход\n")

        match num_typ:
            case "1":
                request_buss.bus_view()
            case "2":
                request_buss.bus_add()
            case "3":
                request_buss.bus_edit()
            case "4":
                request_buss.bus_del()
            case "0":
                break
            case _:
                print("Erro!!")

