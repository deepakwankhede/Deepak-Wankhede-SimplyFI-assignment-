def ind_curr(v):
    # if the value is 100, 10, 1
    if len(str(v)) <= 3:
        return v

    # if the value is 10,000, 1,000
    elif  3 < len(str(v)) <= 5:
        return f'{str(v)[:-3]},{str(v)[-3:]} '
        
    # if the value is greater the 10,000    
    else:
        c = str(v)[:-3]  
        l = []
        while c:
            l.append(c[-2:])
            c = c[:-2]
        
        l = l[::-1]
        result = ",".join(l) 
        
        return f'{result},{str(v)[-3:]}'
        
        
        
print(ind_curr(10000000000))