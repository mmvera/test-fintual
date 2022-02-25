from datetime import date, timedelta

# En la clase Stock guardamos los datos en una lista de diccionario 
# ej: [{'date': '2022,1,1', 'value': 10}, {'date': '2022,1,2', 'value': 10}, 
# {'date': '2022,1,3', 'value': 10}, {'date': '2022,1,4', 'value': 0}]

class Stock():

    def __init__(self,name):
        self.name = name
        self.list_reg = []

# Metodo para agregar los registros de una Stock con fecha y valor 

    def add_register(self,date, value):
        
        register = {}
        register["date"] = date
        register["value"] = value
        self.list_reg.append(register)
        pass

# Metodo que dada una fecha obtiene el precio de una Stock 

    def price(self,date):

        value = 0
        for reg in self.list_reg:
            if (date == reg["date"]):
                value = reg["value"]

        return value

# La clase Portfolio contiene una lista de Stock's 

class Portfolio():

    def __init__(self,name):
        self.name = name
        self.list_stock = []

# Metodo para agregar una Stock a un Potfolio

    def add_stock(self,stock):
        self.list_stock.append(stock)

#Metodo que dada dos fechas devuelve la ganancia en ese intevalo que obtuvo el Portfolio

    def profit (self,date1, date2):

        profit = 0
        for stck in self.list_stock:
            profit = profit + (stck.price(date2) - stck.price(date1))
        
        return profit

# Suponemos de date1 es la fecha donde se hizo la inversion inicial
# P = principal o inversión inicial
# G = ganancias o pérdidas
# n = número de años
# AP = tasa de rendimiento anualizada
# AP = ((P + G) / P) ^ (1 / n) - 1

    def profit_bonus(self,date1, date2):

        profit_annualized = 0
        prof = self.profit(date1,date2)
        value_init = 0 
        period = timedelta(days=365)
        period = date2 - date1
        for stck in self.list_stock: #sumamos todas las inversiones iniciales
            value_init = value_init + stck.price(date1)

        profit_annualized = ((value_init + prof)/value_init) ** (365/period.days) - 1

        return profit_annualized
            
# Probamos con un Portfolio con 2 Stock's

portf = Portfolio("Matias")
stock = Stock("stock1")

d = date(2022,1,1)
stock.add_register(d,10)
d = date(2022,1,2)
stock.add_register(d,20)
d = date(2022,1,3)
stock.add_register(d,20)
d = date(2022,1,4)
stock.add_register(d,50)

portf.add_stock(stock)

stock2 = Stock("Stock2")

d = date(2022,1,1)
stock2.add_register(d,10)
d = date(2022,1,2)
stock2.add_register(d,10)
d = date(2022,1,3)
stock2.add_register(d,10)
d = date(2022,1,4)
stock2.add_register(d,20)

portf.add_stock(stock2)

d1 = date(2022,1,1)
d2 = date(2022,1,4)

print(portf.profit(d1,d2))
print(portf.profit_bonus(d1,d2))