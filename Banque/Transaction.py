import datetime
class Transaction:

    def __init__(this,id,title,montant,fromTo,goTo):
        this.id=id
        this.title=title
        this.montant=montant
        this.date=datetime.now()
        this.fomTo=fromTo
        this.goTo=goTo

    """ def setId(this,id):
        this.id=id
    """
    def getId(this):
        return this.id

    def setTitle(this,title):
        this.title=title

    def getTitle(this):
        return this.name

    def getFromTo(this):
        return this.fomTo

    def getGoTo(this):
        return this.goTo

    def getDate(this):
        return date

