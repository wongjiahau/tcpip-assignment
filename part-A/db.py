import sqlite3
DB = 'stationsdb.sqlite'
db = sqlite3.connect(DB)
db.execute('''
    CREATE TABLE stations (
        id      integer PRIMARY KEY AUTOINCREMENT,
        code    text    UNIQUE NOT NULL,
        name    text    UNIQUE NOT NULL,
        type    text    NOT NULL
    );
''')

data = '''
SBK07  | Surian                   | Elevated
SBK08  | Mutiara Damansara        | Elevated
SBK09  | Bandar Utama             | Elevated
SBK10  | TTDI                     | Elevated
SBK12  | Phileo Damansara         | Elevated
SBK13  | Pusat Bandar Damansara   | Elevated
SBK14  | Semantan                 | Elevated
SBK15  | Muzium Negara            | Underground
SBK16  | Pasar Seni               | Underground
SBK17  | Merdeka                  | Underground
SBK18A | Bukit Bintang            | Underground
'''

cursor = db.cursor()
rows = data.strip().split("\n")
for row in rows:
    columns = [x.strip() for x in row.split("|")]
    cursor.execute(f'''
        INSERT INTO stations(code, name, type) 
        VALUES('{columns[0]}', '{columns[1]}', '{columns[2]}');
    ''')

db.commit()
db.close()