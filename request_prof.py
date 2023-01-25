from logg import logging
import sqlite3

conn = sqlite3.connect('base.db')
cur = conn.cursor()




def prof_view():
    cur.execute("SELECT * FROM prof;")
    result = cur.fetchall()
    print(f"Всего записей {len(result)}")
    logging.info(f"view all prof ,{len(result)} pieces")
    print(f"| id   |  Специализация   |")
    for i in result:
        print(
            f"|{i[0]:5} | {i[1]:16} |")


def prof_add():
    prof = input("Специальность: ")
    rq = f"""INSERT INTO prof (name) VALUES ('{prof}');"""
    logging.info(rq)
    cur.execute(rq)
    conn.commit()


def prof_edit():
    i = int(input("Введите ID специальности которую редактировать: "))
    rq = f"""SELECT EXISTS(SELECT * FROM prof where id = {i})"""
    cur.execute(rq)
    if cur.fetchone()[0]:
        prof = input("Специальность: ")
        rq = f"""UPDATE prof set name = '{prof}' where id = {i}"""
        logging.info(rq)
        cur.execute(rq)
        conn.commit()
    else:
        print(f"Нет специальности номер {i}")
        logging.error(f"Нет специальности номер {i}")
    prof_view()


def prof_del():
    i = int(input("Введите ID специальности которую удаляем: "))
    rq = f"""SELECT EXISTS(SELECT * FROM prof where id = {i})"""
    cur.execute(rq)
    if cur.fetchone()[0]:
        y = input("Вы уверены в удалении?(Y/N): ")
        logging.info(f"Попытка удаления специальности id={i}, {y}")
        if y.lower() == "y":
            rq = f"""DELETE FROM prof WHERE id={i}"""
            logging.info(rq)
            cur.execute(rq)
            conn.commit()
    else:
        print(f"Нет специальности номер {i}")
        logging.error(f"Нет специальности номер {i}")
    prof_view()
