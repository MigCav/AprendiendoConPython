"""""
tareas  =   ['🏦 Get quarters.','🧺 Do laundry.','🌳 Take a walk.','💈 Get a haircut.','🍵 Make some tea.','💻 Complete Lists chapter.','💖 Call mom.',"📺 Watch My Hero Academia"]
print(tareas[0])
print(tareas[3:6])
print(tareas[4:9])
print(tareas[9])
"""

"""""
Create a program stock_analysis.py that implements three functions:

A function max_price(a, b) that finds the maximum price of a stock over the days from a to b inclusive.
A function min_price(a, b) that finds the minimum price of a stock over the days from a to b inclusive.
A function price_at(x) that finds the price on day x.
"""
stock_prices = [ 6.15, 5.81, 5.70, 5.65, 5.33, 5.62, 5.19, 6.13, 7.20, 7.34, 7.95, 7.53, 7.39, 7.59, 7.27 ]
"""
def max_value(a, b):
    print(max(stock_prices[a: b]))

max_value(2, 5)

def min_value(a, b):
    print(min(stock_prices[a:b]))
    
min_value(1,3)

def price_at(a):
    print(stock_prices[a])
    
price_at(0)
"""
"""""
Bonus: Dig into how to find out when the stock changes from going up to going down and vice versa if you want a bigger challenge
"""
#a almacena el valor de i

def variacion():
    j = 0
    c = 0
    for i in stock_prices[1: ]:
        a = stock_prices[0]
        b = i
        if j == 0:
            if b < a:
                print("al segundo dia el precio bajó")
                j += 2
                c = b
            elif b == a:
                j += 2
                c = b
                break
            else:
                print("el precio al segundo dia subió")
                c = b
        else:
            if b > c:
                print("el pecio subió en el dia {}".format(j+1))
                c = b
                j += 1
            elif b == c:
                c = b
                j += 1
                pass
            else:
                print("el precio bajó en el dia {}".format(j+1))
                c = b
                j += 1
                
variacion()