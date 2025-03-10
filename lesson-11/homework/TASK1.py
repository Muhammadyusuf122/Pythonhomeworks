import sqlite3
with sqlite3.connect("roster.db") as connection:
    cursor = connection.cursor()
    cursor.execute(
        "DROP TABLE IF EXISTS ROSTER;"
        )
    cursor.execute(
        """CREATE TABLE ROSTER(
        name text,
        species text,
        age int
        )"""
)
    data= (
('Benjamin Sisko','Human',40),
('Jadzia Dax','Trill',300),
('Kira Nerys','Bajoran',29)
)
    cursor.executemany(
        """Insert into ROSTER(name,species,age) Values(?,?,?);""", data
)
    cursor.execute(
        "Update ROSTER SET name='Ezri Dax' where name='Jadzia Dax'; "
    )
    cursor.execute(
        "Select name, age FROM ROSTER where species='Bajoran'; "
    )
    cursor.execute(
        "DELETE FROM ROSTER WHERE AGE>100;"
    )
    cursor.execute(
        "Alter table ROSTER ADD COLUMN RANK TEXT;"
)
    ranks = (
        ('Benjamin Sisko',	'Captain'),
        ('Ezri Dax',	'Lieutenant'),
        ('Kira Nerys','Major')
)
    cursor.executemany(
        "Insert into ROSTER(name,rank) VALUES(?,?,?); ranks "
    )
    cursor.execute(
        "SELECT *FROM ROSTER ORDER BY age DESC;"
    )
rows= cursor.fetchall()
for row in rows:
    print(row)