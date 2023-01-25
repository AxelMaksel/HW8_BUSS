import sqlite3




conn = sqlite3.connect('base.db')
cur = conn.cursor()
cur.execute("SELECT * FROM prof;")
result = cur.fetchall()
ls={}
for i in result:
   ls[i[0]]=i[1]

print(ls)


rq = f"""SELECT EXISTS(SELECT * FROM buss where id = {2});"""
cur.execute(rq)
q=(cur.fetchone()[0])
# print(bool(q[0]))
print(q)
if q:
   print("#################")