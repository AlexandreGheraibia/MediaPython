from biblio import Classement, Media
#a Row
#   has a classement
#   has medias
########################################################################################################################
#Class Theme#
#############
class Row:
    def getName(this):
        return this.name

    def set(this,name):
        this.name

    def getId(this):
        return id

    def setId(this,id):
        this.id=id

    def getClassement(this):
        return this.classement

    def setClassement(this,classement):
        this.classement=classement

    def setMedias(this,medias):
        this.medias=medias

    def getMedias(this):
        return this.medias

    def ___repr__(this):
        return f"{this.name}"

    #constructeur
    def __init__(this):
        return

    def __init__(this,id,name):
        this.medias=[]
        this.id=id
        this.name=name

    def sortMedias(this):
        this.getClassement().setElements(this.getMedias())
        this.getClassement().triElements()
        this.setMedias(this.getClassement().getElements())

########################################################################################################################
#Main#
######
if __name__=="__main__":
####Init
    t1=Row(0,"Informatic")
    t1.setClassement(Classement.ClassementByAttribute(0))
####Define compare function suptAt of infAt
    t1.getClassement().setCompare(Classement.supAt)
    m1=t1.getMedias()
    m1.append(Media.Media(0, "Python pour les Nuls", 10))
    m1.append(Media.Book(1, "Python pour les Nuls le livre", 10, 120))
    m1.append(Media.Cd(2, "Python pour les Nuls le cd", 10, 2))
    m1.append(Media.Dvd(3, "Python pour les Nuls le dvd", 10, 3))
####init

####Display
    print(f"Row:\t\n {t1.getName()}")
    for media in  t1.getMedias():
        print("\tTitle:",media.getTitle(),f"Price:%.2f"%(media.getNetPrice()))
    for att in m1[0].__dict__:
        if att=="title" or att=='id'or att=="price":
####Sort by att
            t1.getClassement().setAttribute(att)
            print(f"\nRow sortBy {t1.getClassement().getAttribute()}:\t\n {t1.getName()}")
            t1.sortMedias()
            for media in  t1.getMedias():
                print("\tTitle:",media.getTitle(),f"Price:%.2f"%(media.getNetPrice()))
###display
"""
run results:
Row:	
 Informatic
	Title: Python pour les Nuls Price:12.00
	Title: Python pour les Nuls le livre Price:10.50
	Title: Python pour les Nuls le cd Price:12.00
	Title: Python pour les Nuls le dvd Price:9.60

Row sortBy id:	
 Informatic
	Title: Python pour les Nuls Price:12.00
	Title: Python pour les Nuls le livre Price:10.50
	Title: Python pour les Nuls le cd Price:12.00
	Title: Python pour les Nuls le dvd Price:9.60

Row sortBy title:	
 Informatic
	Title: Python pour les Nuls Price:12.00
	Title: Python pour les Nuls le cd Price:12.00
	Title: Python pour les Nuls le dvd Price:9.60
	Title: Python pour les Nuls le livre Price:10.50

Row sortBy price:	
 Informatic
	Title: Python pour les Nuls le dvd Price:9.60
	Title: Python pour les Nuls le livre Price:10.50
	Title: Python pour les Nuls Price:12.00
	Title: Python pour les Nuls le cd Price:12.00
"""







