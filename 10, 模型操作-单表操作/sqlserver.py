
import pymssql
import datetime
from threading import Thread
import inspect


def async_method(method,**args):
    method_args = inspect.getargspec(method).args
   # print(method_args)
    args_keys = list(args.keys())
    for args_key in args_keys:
        if args_key not in method_args:raise ValueError('传入的arg并不存在执行的method参数中')
    input_args = []
    for method_arg in method_args:
        if method_arg in args:
            input_args.append(args[method_arg])
        else:
            input_args.append(None)
    Thread(target=method, args=input_args).start()
def save_to_sql(sh,sql,values):
    if not sh.excuteManySql(sql, values):
        print('预测结果写入sql失败')
class Sql_Handle(object):
    def __init__(self,conf_sql, logger=None):
        self.host = conf_sql['base_config']['host']
        self.user = conf_sql['base_config']['user']
        self.password = conf_sql['base_config']['password']
        self.db = conf_sql['base_config']['db']

    def get_cursor(self):
        try:
            conn = pymssql.connect(self.host, self.user, self.password, self.db)
            cursor = conn.cursor()
        except Exception as error:
            print('msql:{}'.format(error))
            return None, None
        return conn, cursor

    def QuerySql(self,sql):
        conn, cursor = self.get_cursor()
        if cursor is None: return None
        try:
            cursor.execute(sql)
            row = cursor.fetchone()
        except Exception as error:
            print('msql:{}'.format(error))
            conn.close()
            return None
        finally:
            conn.close()

        if row is None: return None
        return row
    def QueryALLSql(self,sql):
        conn, cursor = self.get_cursor()
        if cursor is None: return None
        try:
            cursor.execute(sql)
            row = cursor.fetchall()
        except Exception as error:
            print('msql:{}'.format(error))
            conn.close()
            return None
        finally:
            conn.close()

        if row is None: return None
        return row

    def QueryBatchSql(self,sql):
        conn, cursor = self.get_cursor()
        if cursor is None: return None
        try:
            cursor.execute(sql)
            for row in cursor:
                yield row
        except Exception as error:
            print('msql:{}'.format(error))
            conn.close()
        finally:
            conn.close()

    def excuteSql(self,sql):
        conn, cursor = self.get_cursor()
        if cursor is None: return False
        try:
            cursor.execute(sql)
            conn.commit()
        except Exception as error:
            print('msql:{}'.format(error))
            conn.rollback()
            conn.close()
            return False
        finally:
            conn.close()
        return True

    def excuteManySql(self,sql,value):
        conn, cursor = self.get_cursor()
        if cursor is None: return False
        try:
            cursor.executemany(sql,value)
            conn.commit()
        except Exception as error:
            print('msql:{}'.format(error))
            conn.rollback()
            conn.close()
            return False
        finally:
            conn.close()
        return True
if __name__ == "__main__":
    import platform
    import os,yaml
    if (platform.system() == 'Windows'):
        base_path = "../../../../work/zhongke/python/"
    elif (platform.system() == 'Linux'):
        base_path = "/home/rfl_api/api/burn_optimize/"
    sql_dir = os.path.join(base_path, 'configs/config_sql.yaml')
    with open(sql_dir, 'r', encoding='utf-8') as f:
        conf_sql = yaml.load(f, Loader=yaml.FullLoader)
    sh = Sql_Handle(conf_sql)
   # sql = "SELECT * FROM Persons where Age > 20 and Time > '2022-11-14 11:07:42'"
    ##读取
    sql = "SELECT * FROM Persons"
    print(sh.QuerySql(sql))
    #写入
    # current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    # values = []
    # value = (current_time, 30)
    # values.append(value)
    # values = tuple(values)
    # sql = "INSERT INTO Persons(Time, Age) VALUES (%s,%s)"
    # async_method(save_to_sql, sh=sh, sql=sql, values=values)
    print(sh.excuteManySql(sql, values))

