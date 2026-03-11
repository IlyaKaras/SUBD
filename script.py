import pymssql
import main

con = pymssql.connect(main.server,main.user,main.password,main.db)
cursor = con.cursor()

cursor.execute("""
    USE test3

    /*CREATE TABLE groups_swzr17(
        group_id INT IDENTITY(1000,1) PRIMARY KEY,
        group_name NVARCHAR(5),       
               )

    CREATE TABLE swzr17(
        id INT IDENTITY(1,1) PRIMARY KEY,
        name NVARCHAR(20),
        groups INT,       
               
        CONSTRAINT FK_1 FOREIGN KEY (groups) REFERENCES groups_swzr17(group_id)       
               )          
    */
    insert into groups_swzr17 values('v324')
    insert into swzr17 values('Ilya',1000)
               

    SELECT * FROM swzr17

""")
for row in cursor:
    print(row)
con.commit()
con.close()