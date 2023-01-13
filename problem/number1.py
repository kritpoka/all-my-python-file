h = int(input("hour :"))
m = int(input("minute :"))
s = int(input("sec :"))

def sec_calculate():
    Hsec = h * 3600
    Msec = m * 60
    amount = s + Hsec + Msec
    print(amount)

sec_calculate()
