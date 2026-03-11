import pymssql
import main

con = pymssql.connect(main.server,main.user,main.password,main.db)
cursor = con.cursor()

cursor.execute("""
    USE test3

    CREATE TABLE Facultyswzr17(
        Faculty_id INT IDENTITY(1000,1) PRIMARY KEY,
        Faculty_name NVARCHAR(5),       
               )

    CREATE TABLE Groupsswzr17(
        group_id INT IDENTITY(1,1) PRIMARY KEY,
        group_name NVARCHAR(20),
        faculty INT,       
               
        CONSTRAINT FK_swzr17_1 FOREIGN KEY (faculty) REFERENCES Facultyswzr17(Faculty_id),       
               )  

    CREATE TABLE Studentswzr17(
        id INT IDENTITY(1,1) PRIMARY KEY,
        stud_name NVARCHAR(20),
        groups INT,
        faculty INT ,   
               
        CONSTRAINT FK_swzr17_2 FOREIGN KEY (groups) REFERENCES Groupsswzr17(group_id),
        CONSTRAINT FK_swzr17_3 FOREIGN KEY (faculty) REFERENCES Facultyswzr17(Faculty_id),       
               )
               

    

""")
# for row in cursor:
#     print(row)
con.commit()
con.close()