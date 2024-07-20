import sqlitecloud
from config import sConnString

class SQLiteHandler():
    def __init__(self):
        self.engine = sqlitecloud.connect(sConnString)
        self.engine.execute('USE database Bills')
    def getAllBills(self):
        lRes = self.engine.execute('select * from Bills')
        return lRes
    def addBill(self,values:dict):
        sql = f''' INSERT OR IGNORE INTO Bills
                     VALUES(?,?,?,?,?,?,?,?,?,?) '''
        self.engine.execute(sql, values)
        self.engine.commit()

    def addCard(self,values:tuple):
        sql = f''' insert into Cards values (?,?,?,?)'''
        self.engine.execute(sql,values)
        self.engine.commit()
    def addRecivier(self,values:tuple):
        sql = ''' insert or ignore into Reciviers values (?,?,?,?,?,?)'''
        self.engine.execute(sql,values)
        self.engine.commit()
    def addUser(self,values:tuple):
        sql = ''' insert or ignore into Users values (?,?,?,?,?)'''
        self.engine.execute(sql,values)
        self.engine.commit()



if __name__=='__main__':
    h = SQLiteHandler()
    tCardValues = (1,'DebitCard','SparkasseBankFrankenmarkt','ATSomeOther')
    tRecivierValues = (1,'MaxEnergy','ElectricityProvider','Electricity','BankToBeUpdated','ATMaxEnergy')
    tUsersValues = (1,'Sebair','sebair_selmani@yahoo.com','pass','20240720')
    tBillValues = (2,25,'July','June','BillForJuly','Electricity',1,1,1,1)


    h.addBill(tBillValues)