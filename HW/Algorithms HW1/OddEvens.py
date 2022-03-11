
def odd_even(n):
    
    x = [int(a) for a in str(n)]
    print(x)
    print(len(x))

    var = 0
    size = len(x)
    evens = 0
    odds = 0
    while(var < size):

        if(x[var] % 2 ==0):
            evens +=1
            var +=1
        else:
            odds +=1
            var +=1

    print(f"Evens: {evens} and Odds : {odds}")

    
variable = input("Enter a number:")
print(f"You enter {variable}")

odd_even(variable)