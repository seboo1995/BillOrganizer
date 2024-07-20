import requests
import sqlite3
import pandas as pd
from config import sConnString

class SQLiteHandler():
    def __init__(self):
        self.engine = sqlite3.connect(sConnString)
    def getAllBills(self):
        lRes = self.engine.execute('select * from Bills')
        return lRes
    def addBill(self,values:dict):
        sql = f''' INSERT INTO Bills (ID,UserID,RecivierID,Amount,Period,PaidAt,Description,CardID,Tag,FileID)
                     VALUES(?,?,?,?,?,?,?,?,?,?) '''
        self.engine.execute(sql, values)
        self.engine.commit()
    def addCard(self,values):
        sql = f''' INSERT INTO Cards (ID,UserID,RecivierID,Amount,Period,PaidAt,Description,CardID,Tag,FileID)
                       VALUES(?,?,?,?,?,?,?,?,?,?) '''
        self.engine.execute(sql, values)
        self.engine.commit()



if __name__=='__main__':
    h = SQLiteHandler()
    values = (
        1,
        1,
        1,


    )
    h.addBill()
