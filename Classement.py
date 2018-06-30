#a classement
#has elements
#has a compare of elements

#a compare

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

    def __init__(this,id,compare):
        this.elements=[]
        this.id=id
        this.compare=compare

    def __init__(this,id,isCroissant):
        this.elements=[]
        this.id=id
        if isCroissant:
            this.compare=supAt
        else:
            this.compare=infAt

    def __repr__(this):
        return this.compare

    def triElements(this):
        for i in range(0,len(this.getElements())-1):
            for j in range(i+1,len(this.elements)):
                 if this.getCompare()(this.getElements()[i],this.getElements()[j]):
                    tmp=this.getElements()[i]
                    this.getElements()[i]=this.getElements()[j]
                    this.getElements()[j]=tmp



class ClassementMedia(Classement):
    def  __init__(this):
           return

    def __init__(this,id):
       super().__init__(id,supAt)

    def __init__(this,id,isCroissant):
        super().__init__(id,isCroissant)

    def triElements(this):
        for i in range(0,len(this.getElements())-1):
            for j in range(i+1,len(this.elements)):
                if this.getCompare()((this.getElements()[i]).getTitle(),(this.getElements()[j]).getTitle()):
                    tmp=(this.getElements()[i])
                    (this.getElements()[i])=(this.getElements()[j])
                    (this.getElements()[j])=tmp



if __name__=="__main__":
    c=Classement(0,False)
    c.setElements([1,2,4,3,5,9,7,8,6])
    c.triElements()
    print(c.getElements());


