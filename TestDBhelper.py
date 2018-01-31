from yp.dbhelper import DBhelper


class TestDBhelper(object):
    def __init__(self):
        pass

    def test_save(self):
        sql = "insert into User(id,name,age) VALUES(%s,%s,%s)"
        params = ('8', 'ye', '30')
        dehelper = DBhelper()
        dehelper.insert(sql, *params)


    def test_query(self):
        sql = "select * from User"
        dehelper = DBhelper()
        conn = dehelper.connectDatabase()
        cur = conn.cursor()
        result = cur.execute(sql)
        # for r in cur.fetchall():
        #     print(type(r))
        results = cur.fetchall();
        for row in results:
            print(row[0],"----",row[1],"----",row[2])

        print(type(result))

        # for row in result

    if __name__ == "__main__":
        print("begin : ------------------")
        from TestDBhelper import TestDBhelper
        t = TestDBhelper()
        t.test_query()
        print("end : ------------------")
