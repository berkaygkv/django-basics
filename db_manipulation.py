import pandas as pd
import csv, sqlite3

path_for_writing = r'C:\Users\berkayg\Desktop\Coding env\Main Folder\Upwork\Complete Data with PIDs.xlsx'
def csv_writer(path_for_writing):
    path = path_for_writing
    data = pd.read_excel(path)
    data = data.loc[data['Sourcing_competitor']=='sourcing_tripadvisor']
    data = data.iloc[:500]
    data.to_csv('Rests.csv', index=False)

def sql_writer():
    with open('Rests.csv','r', encoding='UTF-8') as fin: # `with` statement available in 2.5+
        # csv.DictReader uses first line in file for column headings by default
        dr = csv.reader(fin) # comma is default delimiter
        to_db = [i for i in dr]
    col = to_db[0]
    col.append('id')
    columns = tuple(to_db[0])
    edited_columns = tuple(z.replace(' ', '_') for z in columns)
    print(edited_columns)
    vals = f'{"?,"*len(columns)}'[:-1]
    values = to_db[1:]
    values.append(1)
    val_symbol = {len}
    con = sqlite3.connect(r'C:\Users\berkayg\Desktop\Coding env\Main Folder\django-scratch\hakkibey\db.sqlite3') # change to 'sqlite:///your_filename.db'
    cur = con.cursor()
    try:
        cur.execute('DROP TABLE resties_Restaurant')
    except:
        print('NO TABLE')
    cur.execute(f"CREATE TABLE resties_Restaurant {edited_columns};") # use your column names here
    for n,i in enumerate(values):
        try:
            i.append(n)
            print(len(i),'--',i)

            cur.executemany(f"INSERT INTO resties_Restaurant VALUES ({vals});", [i])
        except Exception as ee:
            print('Exception: ',ee)
    con.commit()
    con.close()

def search_all():
    conn=sqlite3.connect(r'C:\Users\berkayg\Desktop\Coding env\Main Folder\dj-project\src\hakkibey\db.sqlite3')
    c = conn.cursor()
    # c.execute('SELECT name from sqlite_master where type= "table"')
    c.execute('SELECT * from resties_Restaurant')
    rows = c.fetchall()
    names = list(map(lambda x: x[0], c.description))
    print(names)
    return rows
    result = []
    for row in rows:
        id, app, username, password = ' ' * (5 - (len(str(row[0])))), ' ' * (15 - (len(str(row[1])))), ' ' * (
                30 - (len(str(row[2])))), ' ' * (25 - (len(str(row[3]))))
        result.append(
            f'ID: {row[0]}{id}|  App: {row[1]}{app}|  Username: {row[2]}{username}|  Password: {row[3]}{password}')
    return result



#csv_writer(path_for_writing)
sql_writer()
# kk = search_all()
# print(kk)