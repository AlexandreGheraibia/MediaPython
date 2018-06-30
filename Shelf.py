import Media
import Classement
#a theme
#   has a classement
#   has medias
########################################################################################################################
#class Theme#
#############
class Theme:
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
#main#
######
if __name__=="__main__":
####init
    t1=Theme(0,"Informatic")
    t1.setClassement(Classement.ClassementByAttribute(0))
    m1=t1.getMedias()
    m1.append(Media.Media(0,"Python pour les Nuls",10))
    m1.append(Media.Book(1,"Python pour les Nuls le livre",10,120))
    m1.append(Media.Cd(2,"Python pour les Nuls le cd",10,2))
    m1.append(Media.Dvd(3,"Python pour les Nuls le dvd",10,3))

####display
    print(f"Theme:\t\n {t1.getName()}")
    for media in  t1.getMedias():
        print("\tTitle:",media.getTitle()," Price:",media.getNetPrice())

####sort by title
    print(f"\nTheme sortBy {t1.getClassement().getAttribute()}:\t\n {t1.getName()}")
    t1.sortMedias()
    for media in  t1.getMedias():
        print("\tTitle:",media.getTitle()," Price:",media.getNetPrice())

#####sort by price
    t1.getClassement().setAttribute("price")
    print(f"\nTheme sortBy {t1.getClassement().getAttribute()}:\t\n {t1.getName()}")
    t1.sortMedias()
    for media in  t1.getMedias():
        print("\tTitle:",media.getTitle()," Price:",media.getNetPrice())

#####sort by id
t1.getClassement().setAttribute("id")
print(f"\nTheme sortBy {t1.getClassement().getAttribute()}:\t\n {t1.getName()}")
t1.sortMedias()
for media in  t1.getMedias():
    print("\tTitle:",media.getTitle()," Price:",media.getNetPrice())

"""
run result:
Theme:	
 Informatic
	Title: Python pour les Nuls  Price: 12.0
	Title: Python pour les Nuls le livre  Price: 10.5
	Title: Python pour les Nuls le cd  Price: 12.0
	Title: Python pour les Nuls le dvd  Price: 9.600000000000001

Theme sortBy title:	
 Informatic
	Title: Python pour les Nuls  Price: 12.0
	Title: Python pour les Nuls le cd  Price: 12.0
	Title: Python pour les Nuls le dvd  Price: 9.600000000000001
	Title: Python pour les Nuls le livre  Price: 10.5

Theme sortBy price:	
 Informatic
	Title: Python pour les Nuls le dvd  Price: 9.600000000000001
	Title: Python pour les Nuls le livre  Price: 10.5
	Title: Python pour les Nuls  Price: 12.0
	Title: Python pour les Nuls le cd  Price: 12.0

Theme sortBy id:	
 Informatic
	Title: Python pour les Nuls  Price: 12.0
	Title: Python pour les Nuls le livre  Price: 10.5
	Title: Python pour les Nuls le cd  Price: 12.0
	Title: Python pour les Nuls le dvd  Price: 9.600000000000001

Process finished with exit code 0



"""







