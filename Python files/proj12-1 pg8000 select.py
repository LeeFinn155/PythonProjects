import pg8000
import getpass

passwd = getpass.getpass("Enter password for 'user' : ")

conn = pg8000.connect("user", host="172.22.80.39", password=passwd,
                      database="itt385", ssl=True)

cur = conn.cursor()

cur.execute("SELECT first_name,last_name FROM contacts LIMIT 5;")

#cur.execute("SELECT first_name,last_name FROM contacts WHERE last_name 'T%' LIMIT 5;")
# (Give me 5 last name's that begin with the letter 'T')

results = cur.fetchall()

for one_row in results:
    first = one_row[0]
    last  = one_row[1]

    print(first,last)
