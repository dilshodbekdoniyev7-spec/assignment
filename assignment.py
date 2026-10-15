def classify(value):
    if value<248:
        return "Below range"
    elif value<=252:
        return "In range"
    else:
        return "Above range"

def calculate_average(total, count):
    return total/count



number_jars=int(input("Enter the number of jars: "))
Total=0
Below_range=0
In_range=0
Above_range=0

for i in range(number_jars):
    volume_jars = int(input("Enter the jar volume: "))
    Total=volume_jars+Total
    average_jars_volume=calculate_average(Total,number_jars)
    sl=classify(volume_jars)
    print(sl)

    if sl=="Below range":
     Below_range=Below_range+1 
    elif sl=="In range":
     In_range=In_range+1 
    else:
     Above_range=Above_range+1        

print(f'Total volume: {Total} ml')
print(f'Average volume: {average_jars_volume} ml')
print(f'Below range: {Below_range}')
print(f'In range: {In_range}')
print(f'Above range: {Above_range}')
    
