# SQLite  DB-API 2.0 interface

SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows accessing the database using a nonstandard variant of the SQL query language

## Monty Python movies using basic sqlite3 functionality

- We need to create a new database and open a database connection to allow sqlite3 to work with it

- Call sqlite3.connect() to create a connection to the database tutorial.db in the current working directory, implicitly creating it if it does not exist:

```py
import sqlite3
con = sqlite3.connect("tutorial.db")
```

above code create a file in your directory named with `tutorial.db`

The returned Connection object con represents the connection to the on-disk database.

In order to execute SQL statements and fetch results from SQL queries, we will need to use a database cursor. Call con.cursor() to create the Cursor:

```py
cur = con.cursor()
```

we’ve got a database connection and a cursor, we can create a database table movie with columns for title, release year, and review score.

Execute the CREATE TABLE statement by calling cur.execute(...):

```py
cur.execute("CREATE TABLE movie(title, year, score)")
```

We can verify that the new table has been created by querying the sqlite_master table built-in to SQLite

should now contain an entry for the movie table definition

### Schema Table

Every SQLite database contains a single "schema table" that stores the schema for that database. The schema for a database is a description of all of the other tables, indexes, triggers, and views that are contained within the database. The schema table looks like this:

```sql
CREATE TABLE sqlite_schema(
  type text,
  name text,
  tbl_name text,
  rootpage integer,
  sql text
);
```

Execute that query by calling cur.execute(...), assign the result to res, and call res.fetchone() to fetch the resulting row:

```py
res = cur.execute("SELECT name FROM sqlite_master")
res.fetchone()
```

> IF NOT EXISTS important otherwise got error :
> cur.execute("CREATE TABLE movie(title, year, score)")
>
> sqlite3.OperationalError: table movie already exists

cur.execute("CREATE TABLE IF NOT EXISTS movie(title, year, score)")

res.fetchone() it will give anser on first time if you run again it show none

We can see that the table has been created, as the query returns a tuple containing the table’s name. If we query sqlite_master for a non-existent table spam, res.fetchone() will return None:

```py
res = cur.execute("SELECT name FROM sqlite_master WHERE name='spam'")
res.fetchone() is None
```

add two rows of data supplied as SQL literals by executing an INSERT statement, once again by calling cur.execute(...):

```py
cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")
```

The INSERT statement implicitly opens a transaction, which needs to be committed before changes are saved in the database (see Transaction control for details). Call con.commit() on the connection object to commit the transaction:

```py
con.commit()
```

```py
res = cur.execute("SELECT score FROM movie")
res.fetchall()
```

```py
data = [
    ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    ("Monty Python's The Meaning of Life", 1983, 7.5),
    ("Monty Python's Life of Brian", 1979, 8.0),
]
cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
con.commit()  # Remember to commit the transaction after executing INSERT.
```

Notice that ? placeholders are used to bind data to the query. Always use placeholders instead of string formatting to bind Python values to SQL statements, to avoid SQL injection attacks

QLite and Python types
SQLite natively supports the following types: NULL, INTEGER, REAL, TEXT, BLOB.

The following Python types can thus be sent to SQLite without any problem:

```
Python type  SQLite type

None NULL
int INTEGER
float REAL
str TEXT
bytes BLOB
```

## How to use placeholders to bind values in SQL queries¶

 beware of using Python’s string operations to assemble queries, as they are vulnerable to SQL injection attacks. For example, an attacker can simply close the single quote and inject OR TRUE to select all rows:

 ```py
 # Never do this -- insecure!
symbol = input()

sql = "SELECT * FROM stocks WHERE symbol = '%s'" % symbol
print(sql)

cur.execute(sql)
```

an SQL statement may use one of two kinds of placeholders: question marks (qmark style) or named placeholders (named style).

For the qmark style, parameters must be a sequence whose length must match the number of placeholders, or a ProgrammingError is raised

```py
con = sqlite3.connect(":memory:")
cur = con.execute("CREATE TABLE lang(name, first_appeared)")

# This is the named style used with executemany():
data = (
    {"name": "C", "year": 1972},
    {"name": "Fortran", "year": 1957},
    {"name": "Python", "year": 1991},
    {"name": "Go", "year": 2009},
)
cur.executemany("INSERT INTO lang VALUES(:name, :year)", data)

# This is the qmark style used in a SELECT query:
params = (1972,)
cur.execute("SELECT * FROM lang WHERE first_appeared = ?", params)
print(cur.fetchall())
con.close()
```

by executing a SELECT query, this time iterating over the results of the query:

```py
for row in cur.execute("SELECT year, title FROM movie ORDER BY year"):
    print(row)
```

 by calling con.close() to close the existing connection,

```py
res = new_cur.execute("SELECT title, year FROM movie ORDER BY score DESC")
title, year = res.fetchone()
print(f'The highest scoring Monty Python movie is {title!r}, released in {year}')
```

## MD5

```py
import hashlib
def md5sum(t):
    return hashlib.md5(t).hexdigest()
con = sqlite3.connect(":memory:")
con.create_function("md5", 1, md5sum)
for row in con.execute("SELECT md5(?)", (b"foo",)):
    print(row)

con.close()
```
