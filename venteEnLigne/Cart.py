from venteEnLigne.CartRow import CartRow

class Cart:
    def __init__(this):
        this.cartRowList=[]

    def add(this,media):
        row=this.isElementContained(media)
        if row==None:
            this.cartRowList.append(CartRow(media))
        else:
            row.increment()


    def isElementContained(this,media):
        res=None
        for row in this.cartRowList:
            if row.getMedia()==media:
                return row
        return res

    def remove(this,media):
        row=this.isElementContained(media)
        if not (row==None):
            if row.getQuantity()>1:
                row.decrement()
            else:
                this.cartRowList.remove(row)

    def getTotalNetPrice(this):
        sum=0
        for row in this.cartRowList:
            sum+=row.getMedia().getNetPrice()*row.getQuantity()
        return sum

    def __repr__(this):
        return f"{this.cartRowList}"