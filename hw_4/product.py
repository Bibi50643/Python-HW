class Product:
    def __init__(self,name,n,price):
        self.name=name
        self.n=n
        self.price=price

    def get_price(self,n):
        if n<10:
            return self.price
        elif 10<n<99:
            return self.price*0.9
        elif n>100:
            return self.price*0.8

    def make_purchase(self,m):
        if m<=self.n:
            self.n-=m
            return self.get_price(m)*m
        if m>=self.n:        
            return 0
            
p1=Product("Alma",20,400)
p2=Product("Aпельсин",10,850)
p3=Product("Огурцы",45,250)
p4=Product("Бананы",3,1200)
p5=Product("Киви ",120,500)
total=p1.make_purchase(2)+p2.make_purchase(1)+p3.make_purchase(2)+p4.make_purchase(101)+p5.make_purchase(125)
print("total =",total)

