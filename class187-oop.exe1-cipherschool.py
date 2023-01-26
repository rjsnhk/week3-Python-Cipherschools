class Laptop:
    def __init__(self,brand,model,price):
        self.brand_name=brand
        self.model_no=model
        self.price=price
        self.lap_name=brand+' '+model
l1=Laptop('asus','12arfdv',84000)
l2=Laptop('vivo','12sdfgk3',203333)

print(l1.lap_name)