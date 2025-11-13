import sqlite3
con = sqlite3.connect("tutorial.db")

cur = con.cursor()

# IF NOT EXISTS important otherwise got error     cur.execute("CREATE TABLE movie(title, year, score)")
    # ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# sqlite3.OperationalError: table movie already exists

cur.execute("CREATE TABLE IF NOT EXISTS movie(title, year, score)")

res = cur.execute("SELECT name FROM sqlite_master")
# res.fetchone()

print(res.fetchone())

res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")
# res.fetchone() is None
print(res.fetchone() is None)
# cur.execute("""
#     INSERT INTO movie VALUES
#         ('Monty Python and the Holy Grail', 1975, 8.2),
#         ('And Now for Something Completely Different', 1971, 7.5)
# """)
# data = [
#     ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
#     ("Monty Python's The Meaning of Life", 1983, 7.5),
#     ("Monty Python's Life of Brian", 1979, 8.0),
# ]
# cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
# con.commit()  # Remember to commit the transaction after executing INSERT.
# con.commit()

res = cur.execute("SELECT score FROM movie")
print(res.fetchall())
for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
    print(row)

res = cur.execute("SELECT title, year FROM movie ORDER BY score DESC")
title, year = res.fetchone()
print(f'The highest scoring Monty Python movie is {title!r}, released in {year}')
cur.close()


import hashlib
def md5sum(t):
    return hashlib.md5(t).hexdigest()
con = sqlite3.connect(":memory:")
con.create_function("md5", 1, md5sum)
for row in con.execute("SELECT md5(?)", (b"foo",)):
    print(row)

con.close()