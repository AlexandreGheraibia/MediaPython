#a classement
#has elements
#has a compare of elements

#a compare
import Media
def supAt(a,b):
    return a>b
def infAt(a,b):
    return a<b
def equalAt(a,b):
    return a==b

class Classement:
    #get,set
    def getId(this,id):
        return id

    def setId(this,id):
        this.id=id

    def setCompare(this,compare):
        this.compare=compare

    def getCompare(this):
        return this.compare

    def getElements(this):
        return this.elements

    def setElements(this,elem):
        this.elements=elem

    def __repr__(this):
        return f"{this.compare}"

    #constructeur
    def __init__(this):
        return

    def __init__(this,id):
        this.elements=[]
        this.id=id
        this.compare=supAt

    def __repr__(this):
        return this.compare

    def triElements(this):
        for i in range(0,len(this.getElements())-1):
            for j in range(i+1,len(this.elements)):
                 if this.getCompare()(this.getElements()[i],this.getElements()[j]):
                    tmp=this.getElements()[i]
                    this.getElements()[i]=this.getElements()[j]
                    this.getElements()[j]=tmp

class ClassementByAttribute(Classement):
    def getAttribute(this):
        return this.attribute

    def setAttribute(this,attribute):
        this.attribute=attribute

    def  __init__(this):
           return

    def __init__(this,id):
        this.attribute="title"
        super().__init__(id)

    def triElements(this):
        for i in range(0,len(this.getElements())-1):
            for j in range(i+1,len(this.elements)):
                if this.getCompare()(this.getAttributeElement(this.getElements()[i]),this.getAttributeElement(this.getElements()[j])):
                    tmp=(this.getElements()[i])
                    (this.getElements()[i])=(this.getElements()[j])
                    (this.getElements()[j])=tmp


    def getAttributeElement(this,elem):
        if this.getAttribute()=="title":
            return elem.getTitle()
        elif this.getAttribute()=="id":
            return elem.getId()
        elif this.getAttribute()=="price":
            return elem.getNetPrice()



if __name__=="__main__":
    c=Classement(0)
    c.setElements([1,2,4,3,5,9,7,8,6])
    c.triElements()
    m1=[]
    m1.append(Media.Media(0,"Python pour les Nuls",10))
    m1.append(Media.Book(0,"Python pour les Nuls le livre",10,120))
    m1.append(Media.Cd(0,"Python pour les Nuls le cd",10,2))
    m1.append(Media.Dvd(0,"Python pour les Nuls le dvd",10,3))
    print(c.getElements());
    c.setElements(m1)
    for elem in c.getElements():
            print(elem.__dict__)


