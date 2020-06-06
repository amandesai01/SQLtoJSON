from pypackage import s2j

db = s2j.s2j("localhost", "root", "root@1441", "proj")
print(db.execQuery("SELECT * FROM users;"))