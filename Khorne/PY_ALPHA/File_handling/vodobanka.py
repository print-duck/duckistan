import hashlib
class bank:
    accounts={}
    
    
class account:
    def __init__(self,name,customerId,pin):
        self.name=name
        self.id=customerId
        self.balance=500
        self.pin=(hashlib.md5(pin.encode())).digest()
        self.data={'name':self.name,'balance':self.balance,'pin':self.pin}
        bank.accounts[self.id]=self.data
        
        
baron=bank()
delamain=account('smith','20','3030')
