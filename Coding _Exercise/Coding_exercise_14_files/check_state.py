solid = 0
gas = 100
def check_state(temp):
    if temp <= solid:
        print("Solid")
    elif solid < temp < gas:
        print("Liquid")
    else:
        print("Gas")