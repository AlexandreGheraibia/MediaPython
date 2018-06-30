#un compte
#    un client
#   des transactions
#   appartient a une banque et un client
from Banque import Bank
from Banque.Customer import Customer
import datetime

class Account:

    def setId(this,id):
        this.id=id

    def getId(this):
        return this.id

    def getName(this):
        return this.name

    def setName(this,name):
        return this.name

    def getSold(this):
        return this.sold
    """
    def setSold(this,sold):
        this.sold=sold
    """
    def getTransaction(this):
        return this.transaction()

    def setCustomer(this,customer):
        this.customer=customer

    def getCustomer(this,customer):
        return customer

    def __init__(this):
        return

    def __init__(this,id,name,sold):
        this.id=id
        this.name=name
        this.sold=sold
        this.custumer=Customer()
        this.bank=Bank()
        this.transactions=[]
        this.createThe=datetime.now


    def __repr__(this):
        return f"{name}"
