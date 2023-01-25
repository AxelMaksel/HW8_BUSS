from logg import logging
import sqlite3

conn = sqlite3.connect('base.db')
cur = conn.cursor()


cur.execute("SELECT * FROM prof;")
result = cur.fetchall()
ls_prof = {}
for i in result:
    ls_prof[i[0]] = i[1]


def piple_view():
    cur.execute("SELECT * FROM piple;")
    result = cur.fetchall()
    print(f"Всего записей {len(result)}")
    logging.info(f"view all piple ,{len(result)} pieces")
    print(f"| id   |  Фамилия   | год рождения|  таб. номер     |  специальность  |      коментарий           |")
    for i in result:
        print(
            f"|{i[0]:5} | {i[1]:10} | {i[2]:11} | {i[3]:15} | {ls_prof[i[4]]:15} | {i[5]:25} |")


def piple_add():
    family = input("Фамилия: ")
    year = input("Год рождения: ")
    number = input("Табельный номер: ")
    prof = input("специальность: ")
    coment = input("Коментарий: ")
    rq = f"""INSERT INTO piple(family, year, number, prof, coment) VALUES ('{family}','{year}', '{number}','{prof}','{coment}');"""
    logging.info(rq)
    cur.execute(rq)
    conn.commit()


def piple_edit():
    i = int(input("Введите ID работника которого редактировать: "))
    rq = f"""SELECT EXISTS(SELECT * FROM piple where id = {i})"""
    cur.execute(rq)
    if cur.fetchone()[0]:
        family = input("Фамилия: ")
        year = input("Год рождения: ")
        number = input("Табельный номер: ")
        prof = input("специальность: ")
        coment = input("Коментарий: ")
        rq = f"""UPDATE piple set family = ?, year = ?, number = ?, prof = ?, coment = ?    where id = ?"""
        data = (family, year, number, prof, coment, i)
        rqd = ", ".join(map(str,  data))
        logging.info(f"{rq}, {rqd}")
        cur.execute(rq, data)
        conn.commit()
    else:
        print(f"Нет работника номер {i}")
        logging.error(f"Нет работника номер {i}")
    piple_view()


def piple_del():
    i = int(input("Введите ID Работника которого удаляем: "))
    rq = f"""SELECT EXISTS(SELECT * FROM piple where id = {i})"""
    cur.execute(rq)
    if cur.fetchone()[0]:
        y = input("Вы уверены в удалении?(Y/N): ")
        logging.info(f"Попытка удаления работника id={i}, {y}")
        if y.lower() == "y":
            rq = f"""DELETE FROM piple WHERE id={i}"""
            logging.info(rq)
            cur.execute(rq)
            conn.commit()
    else:
        print(f"Нет работника номер {i}")
        logging.error(f"Нет работника номер {i}")
    piple_view()
