import mysql.connector

def get():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='0000',
        port=3306,
        database='planner'
    )

    return conn


def ins(title,priority):
    conn = get()
    cursor = conn.cursor()
    cursor.execute('show tables')

    t = cursor.fetchall()[0][0]
    

    cursor.execute(f'insert into {t}(title , priority) values(%s,%s)',(title,priority))
    conn.commit()
    cursor.close()
    conn.close()


def show():
    conn = get()
    cursor = conn.cursor()
    cursor.execute('show tables')
    t = cursor.fetchall()[0][0]
    cursor.execute(f'select * from {t} order by priority desc')
    r = cursor.fetchall()


    cursor.close()
    conn.close()
    return r

def showByPriority(prior):
    conn = get()
    cursor = conn.cursor()
    cursor.execute('show tables')
    t = cursor.fetchall()[0][0]
    cursor.execute(f'select * from {t} where priority >= {prior} and priority <= {prior+2} ')
    r = cursor.fetchall()


    cursor.close()
    conn.close()
    return r
