from venteEnLigne.Cart import Cart

########################################################################################################################
#Main#
######

from venteEnLigne.Media import Author, Book, Dvd, Cd

if __name__== '__main__':
    m1=Book(0,"Java pour les Nuls",10,120)
    #print(f"exemple affichage")
    #print(f"\r {m1.getTitle()}\n {m1.getNetPrice()}\n {m1.getId()}")
    a1=Author(0,"Boris",'nom')
    m1.getAuthors().append(a1)
    m1.getAuthors().append(Author(1,"Alex","nom"))
    m1.getAuthors().append(Author(1,"Moustafa","nom"))
    m1.getAuthors().append(Author(1,"Florent","nom"))
    m1.getAuthors().append(Author(1,"Alex","nom"))
    #for author in m1.getAuthors():
     #   print(author)
    #####################################
    # suppresion d'elems dans une liste
    ####################################
    del m1.getAuthors()[2:4]
    #print(m1.getAuthors())
   # print(f"\r\nexemple de parcours")
    """for i in range(0,len(m1.getAuthors())):
        print({m1.getAuthors()[i].getFirstName()})
    """
    m1.getAuthors().append(Author(1,"Alex","nom"))
    b1=Book(0,"Java pour les Nuls",10,120)
   # print(b1.getNetPrice())
    d1=Dvd(0,"Java pour les Nuls en Dvd",10,2)
    #print(d1.getTitle())
    #print(Dvd(1,"Java pour les Nuls en Dvd",10,2).getNetPrice())
    c1=Cd(0,"Java pour les Nuls en Cd",10,2)
    #print(f"\r\nexemple de polymorphisme")
    tabM=[Cd(0,"Cd Java pour les Nuls",10,2), b1,c1,d1,c1,Cd(0,"Java pour les Nuls en Cd",10,2)]
    basket=Cart()
    for m in tabM:
        basket.add(m)
    print(basket)
    print("total\t\t%d"%(basket.getTotalNetPrice()))
    basket.remove(c1)
    print("suppression de %s",c1.getTitle())
    print(basket)
    for m in tabM:
        print(m.getNetPrice())

    print("total\t\t%d"%(basket.getTotalNetPrice()))
