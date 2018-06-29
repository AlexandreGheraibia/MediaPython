#################################
#        classe Media           #
#################################
class Media():
    #constructeur de media
    def __init__(self):#le constructeur vide doit le premier constructeur
        return
    def __init__(self,id,title,price): #constructeur de media
        self.id=id
        self.title=title
        self.price=price
        #partten design A
        #self.publisher
        #pattern design B
        self.authors=[]

    #implementation de toString
    def __repr__(self):
        return f"({self.getTitle()})"

    def getTitle(self):
        return self.title

    def getId(self):
        return self.id

    def getPrice(self):
        return self.price

    def getNetPrice(self):
        return self.price*1.2

    def getAuthors(self):
        return self.authors

    def getPublisher(self):
        return self.publisher

    def setPublisher(self,publisher):
        self.publisher=publisher

    def setAuthors(self,authors):
        self.authors=authors

############
#parttern D#
############
##################################################################################################################
#        Classe Book            #
#################################
#la classe Book extend the Media class
class Book(Media):
    def getNetPrice(self):
        return self.getPrice()*1.05 #the price is private hence we call the method price

    def setNbPages(self,nbPages):
        self.nbPages=nbPages

    def __init__(self):
        return
    def __init__(self,id,title,price):
        super().__init__(id,title,price)

    def __init__(self,id,title,price,nbPages):
        super().__init__(id,title,price)
        self.nbPages=nbPages

    def getNbPages(self):
        return self.nbPages

##################################################################################################################
#        Classe Cd            #
###############################
 class Cd(Media):#la classe Cd extend the Media class
    def getNbTracks(self):
        return self.nbTracks

    def setNbTracks(self,nbTracks):
        self.nbTracks=nbTracks

    def __init__(self):
        return
    def __init(self,id,title,price):
        super().__init__(id,title,price)

    def __init(self,id,title,price,nbTracks):
        super().__init__(id,title,price)
        self.nbTracks=nbTracks

##################################################################################################################
#        Classe Dvd            #
################################

class Dvd(Media):#la classe Dvd extend the Media class
    def setZone(self,zone):
        self.zone=zone

    def getZone(self):
        return self.zone

    def __init__(self):
        return
    def __init__(self,id,title,price):

        super().__init__(id,title,price)

    def __init__(self,id,title,price,zone):
        super().__init__(id,title,price)
        self.zone=zone

    def getNetPrice(self):
        return (super().getPrice()*1.2)*(1.0-0.2)
    
################
#  Pattern C   #
################
#################################################################################################################
#		classe Author		#
#############################
class Author:
    def getId(self):
        return self.Id

    def setId(self,id):
        self.Id=id

    def setFirstName(self,firstName):
        self.firstName=firstName

    def getFirstName(self):
        return self.firstName

    def setLastName(self,lastName):
        self.lastName=lastName

    def getLastName(self):
        return self.lastName

    def __init__(self):
        return

    def __init__(self,id,firstName,lastName):
        self.id=id
        self.firstName=firstName
        self.lastName=lastName

    def __repr__(self):#toString
        return f"{self.firstName}"

#############
# pattern B #
#############
########################################################################################################
# Classe Publisher #
####################
class Publisher:
    def __initi__(self):
        return

    def __init__(self,id,name):
        self.id=id
        self.name=name

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def setId(self,id):
        self.id=id

    def setName(self,name):
        self.name=name

    def __repr__(self):
        return f"{self.getName()}"

#########################################################################################################

if __name__== '__main__':
    m1=Media(0,"Java pour les Nuls",10)
    print(f"\r {m1.getTitle()}\n {m1.getNetPrice()}\n {m1.getId()}")
    a1=Author(0,"Boris",'nom')
    m1.getAuthors().append(a1)
    m1.getAuthors().append(Author(1,"Alex","nom"))
    m1.getAuthors().append(Author(1,"Moustafa","nom"))
    m1.getAuthors().append(Author(1,"Florent","nom"))
    m1.getAuthors().append(Author(1,"Alex","nom"))
    for author in m1.getAuthors():
        print(author)
    #####################################
    #suppresion elem dans une liste
    ####################################
    del m1.getAuthors()[2:4]
    print(m1.getAuthors())
    for i in range(0,len(m1.getAuthors())):
        print({m1.getAuthors()[i].getFirstName()})

    m1.getAuthors().append(Author(1,"Alex","nom"))
    b1=Book(0,"Java pour les Nuls",10,120)
    print(b1.getNetPrice())
    print(Dvd(0,"Java pour les Nuls en Dvd",10,2).getTitle())
    print(Dvd(1,"Java pour les Nuls en Dvd",10,2).getNetPrice())