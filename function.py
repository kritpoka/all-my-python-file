#variable
i = 0

#function 
def number():#dymnamic typing 
    #code block 
    count = int(input("ใส่จำนวนที่ต้องการนับถอยหลัง :"))  
    print("เริ่ม")
    while count >= 0:
        print(str(count)+'!')
        count = count - 1
    print("จบ")
    
def numbers():
    total = int(input("all people :"))
    average = int(input("input point :"))
    answer = average/total
    print(answer)
    
def use():
    var = int(input("input your number:"))

    if var==1:
        print(number())

    elif var == 2:
        print(numbers())
    
    else:
        print("!")
    
while i == 0:
    print(use())
    check = int(input("Y/N :"))
    if check ==2:
       i += 1
       print(i)
    else:
        print("thank you !")
        
            





    

