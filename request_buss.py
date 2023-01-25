from logg import logging
import sqlite3

conn = sqlite3.connect('base.db')
cur = conn.cursor()


def bus_view():
    cur.execute("SELECT * FROM buss;")
    result = cur.fetchall()
    print(f"Всего записей {len(result)}")
    logging.info(f"посмотерть все автобусы ,{len(result)} штук")
    print(f"| id   |   Модель   | год выпуска |  гос номер      | мест  |     коментарий            |")
    for i in result:
        print(
            f"|{i[0]:5} | {i[1]:10} | {i[2]:11} | {i[3]:15} | {i[4]:5} | {i[5]:25} |")


def bus_add():
    model = input("модель: ")
    year = input("Год производства: ")
    number = input("Гос номер: ")
    places = input("кол-во мест: ")
    coment = input("Коментарий: ")
    rq = f"""INSERT INTO buss(model, year, number, places, coment) VALUES ('{model}','{year}', '{number}','{places}','{coment}');"""
    logging.info(rq)
    cur.execute(rq)
    conn.commit()


def bus_edit():
    i = int(input("Введите ID автобуса который редактировать: "))
    rq = f"""SELECT EXISTS(SELECT * FROM buss where id = {i})"""
    cur.execute(rq)
    if cur.fetchone()[0]:
        model = input("модель: ")
        year = input("Год производства: ")
        number = input("Гос номер: ")
        places = input("кол-во мест: ")
        coment = input("Коментарий: ")
        rq = """UPDATE buss set model = ?, year = ?, number = ?, places = ?, coment = ?    where id = ?"""
        data = (model, year, number, places, coment, i)
        rqd = ", ".join(map(str,  data))
        logging.info(f"{rq}, {rqd}")
        cur.execute(rq, data)
        conn.commit()
    else:
        print(f"Нет автобуса номер {i}")
        logging.error(f"Нет автобуса номер {i}")
    bus_view()


def bus_del():
    i = int(input("Введите ID автобуса который удаляем: "))
    rq = f"""SELECT EXISTS(SELECT * FROM buss where id = {i})"""
    cur.execute(rq)
    if cur.fetchone()[0]:
        y = input("Вы уверены в удалении?(Y/N): ")
        logging.info(f"Попытка удаления автобуса id={i}, {y}")
        if y.lower() == "y":
            rq = f"""DELETE FROM buss WHERE id={i}"""
            logging.info(rq)
            cur.execute(rq)
            conn.commit()
    else:
        print(f"Нет автобуса номер {i}")
        logging.error(f"Нет автобуса номер {i}")
    bus_view()
