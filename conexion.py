try:
    conn= pymysql.connect(host='localhost', user='root', passwd='', db='agenda' )
except Exception:
    print("ERROR")
cursor = conn.cursor()
cursor.execute('insert into comenta (correo,comentarios) values (%s, %s)',(aux_Correo, aux_Comentarios))
conn.commit()