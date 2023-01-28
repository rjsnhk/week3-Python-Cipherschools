class Laptop:
    def __init__(self,brand,model,price):
        self.brand_name=brand
        self.model_no=model
        self.price=price
        self.lap_name=brand+' '+model
        
    def discount(self,n):
        off=(n/100)*self.price
        return self.price-off


l1=Laptop('asus','12arfdv',84000)
l2=Laptop('vivo','12sdfgk3',203333)

# print(l1.lap_name)
print(l1.discount(20))