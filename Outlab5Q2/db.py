import csv
import sqlite3


def returnCount(category_name):
    connect = sqlite3.connect("cse_students.sqlite")
    cursor = connect.cursor()
    cursor.execute("select * from stock where ['Category Name']=:category_name", {"category_name": category_name})
    a = cursor.fetchone()
    if a == None:
        return "Invalid"
    else :
        return (a[1])
        connect.close()

def main():
    data = csv.reader(open('count.csv'), delimiter=',')
    column1, column2 = [], []

    for row in data:
        column1.append(row[0])
        column2.append(row[1])

    cat = column1[0]
    no = column2[0]

    try :
        conn = sqlite3.connect('cse_students.sqlite')
        c = conn.cursor()
        query = "CREATE TABLE stock (%s, %s)"
        c.execute(query % ([cat], [no]))
        size = len(column1)
        for i in range(size-1):
            c.execute("INSERT INTO stock VALUES (?, ?)", (column1[i+1], column2[i+1]))
        conn.commit()
        conn.close()
    except sqlite3.OperationalError:
        pass

    cat_name = input()
    output = returnCount(cat_name)
    print(output)


main()

