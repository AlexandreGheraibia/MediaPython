class CartRow:
    def __init__(this, media = None):
        this.media = media
        this.quantity = 1

    def increment(this):
        this.quantity+=1

    def decrement(this):
        if this.quantity >1  :
            this.quantity-=1

    def getMedia(this):
        return this.media

    def getQuantity(this):
        return this.quantity

    def __repr__(this):
        return f"{this.media} {this.quantity}"