# DB

## How do you prevent SQL injection in Python (with psycopg2 or SQLAlchemy)?

The primary way to prevent SQL injection in Python with psycopg2 and SQLAlchemy is to always use parameterized queries, which ensure user input is treated as data, not executable code. Avoid raw string concatenation or f-strings for building queries with user input.

1. psycopg2
psycopg2 uses the %s placeholder for parameter substitution, regardless of the actual data type. The library handles the escaping and quoting internally and securely.

### Safe Example (Recommended)

```py
import psycopg2

conn = psycopg2.connect("dbname=testdb user=user password=password")
cursor = conn.cursor()

# Use %s as a placeholder and pass data as the second argument (a tuple)
username = "haki'; UPDATE users SET admin = 'true' WHERE username = 'haki" 
query = "SELECT admin FROM users WHERE username = %s"

# The library safely handles the 'username' value as data, not code
cursor.execute(query, (username,)) 
record = cursor.fetchone()
```

### Dangerous Example (AVOID)

```py
# AVOID THIS - Vulnerable to SQL Injection
username = "haki'; UPDATE users SET admin = 'true' WHERE username = 'haki"
# The string formatting directly inserts the malicious code into the query
cursor.execute(f"SELECT admin FROM users WHERE username = '{username}'") 
```
