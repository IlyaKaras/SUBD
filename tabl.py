import pymssql
import main

con = pymssql.connect(main.server,main.user,main.password,main.db)
cursor = con.cursor()

cursor.execute("""
    USE test3
    CREATE TABLE Motherboard_list_swzr17(
        Motherboard_id INT IDENTITY(1,1) PRIMARY KEY,
        Motherboard_name NVARCHAR(20),       
               )

    CREATE TABLE Cases_list_swzr17(
        Cases_id INT IDENTITY(1,1) PRIMARY KEY,
        Cases_name NVARCHAR(20),       
               )

    CREATE TABLE Storage_list_swzr17(
        Storage_id INT IDENTITY(1,1) PRIMARY KEY,
        Storage_name NVARCHAR(20),       
               )

    CREATE TABLE PowerUnit_list_swzr17(
        PowerUnit_id INT IDENTITY(1,1) PRIMARY KEY,
        PowerUnit_name NVARCHAR(20),       
               )
    
    CREATE TABLE CPU_list_swzr17(
        CPU_id INT IDENTITY(1,1) PRIMARY KEY,
        CPU_name NVARCHAR(20),       
               )

    CREATE TABLE GPU_list_swzr17(
        GPU_id INT IDENTITY(1,1) PRIMARY KEY,
        GPU_name NVARCHAR(20),       
               )

    CREATE TABLE RAM_list_swzr17(
        RAM_id INT IDENTITY(1,1) PRIMARY KEY,
        RAM_name NVARCHAR(20),       
               )

    CREATE TABLE Assembly_list_swzr17(
        id_list INT IDENTITY(1,1),
        Motherboard INT,     
        CPU INT,
        RAM INT,
        GPU INT,
        Storage INT,
        PowerUnit INT,
        Cases INT,
        CONSTRAINT FK_swzr171 FOREIGN KEY (Motherboard) REFERENCES Motherboard_list_swzr17(Motherboard_id),
        CONSTRAINT FK_swzr172 FOREIGN KEY (CPU) REFERENCES CPU_list_swzr17(CPU_id),
        CONSTRAINT FK_swzr173 FOREIGN KEY (RAM) REFERENCES RAM_list_swzr17(RAM_id),
        CONSTRAINT FK_swzr174 FOREIGN KEY (GPU) REFERENCES GPU_list_swzr17(GPU_id),
        CONSTRAINT FK_swzr175 FOREIGN KEY (Storage) REFERENCES Storage_list_swzr17(Storage_id),
        CONSTRAINT FK_swzr176 FOREIGN KEY (PowerUnit) REFERENCES PowerUnit_list_swzr17(PowerUnit_id),
        CONSTRAINT FK_swzr177 FOREIGN KEY (Cases) REFERENCES Cases_list_swzr17(Cases_id),                    
               )
    insert into Motherboard_list_swzr17 values('Motherboard')
    insert into Cases_list_swzr17 values('Cases')
    insert into Storage_list_swzr17 values('Storage')
    insert into PowerUnit_list_swzr17 values('PowerUnit')
    insert into CPU_list_swzr17 values('CPU')
    insert into GPU_list_swzr17 values('GPU')
    insert into RAM_list_swzr17 values('RAM')
    
""")
# for row in cursor:
#     print(row)
con.commit()
con.close()