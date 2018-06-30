#un compte
#    un client
#   des transactions
#   appartient a une banque et un client
import sys

from Banque import Bank
from Banque.Customer import Customer
import datetime

class Account:
    """
    si id generer à l'exterieur
    """
    def setId(this,id):
        this.id=id

    def getId(this):
        return this.id

    """def getName(this):
        return this.name

    def setName(this,name):
        return this.name
    """
    def getSold(this):
        return this.sold
    """
    private
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

    def __init__(this,id):
        this.id=id
        this.sold=0
        this.custumer=None
        this.bank=Bank()
        this.transactions=[]
        this.createThe=datetime.now

    def __repr__(this):
        return f"{name}"

    def retire(this,montant):
        if this.getSold()-montant>0 and montant>0:
            this.sold-=montant
            return montant
        else:
            if montant<0 :
                sys.stderr.write('-- transaction not allowed by retire opeation--')
            else
                sys.stderr.write('-- transaction was refused by retire --not enought found on account id'+this.getId())
            return 0

    def depose(this,montant):
        if montant>0:
            this.sold+=montant
            return montant
        else:
            sys.stderr.write('--transaction was refused by depose--negative montant')
            return 0


if __name__=="__main__":
