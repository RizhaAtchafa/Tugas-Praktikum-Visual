print("\n Tabel Perkalian 1-10")
print(50 * "=")
for i in range(1,11):
    for j in range(1,11):
        x = i*j
        if x<10:
            print( " | ", x, end=" | ")
        elif x >= 10 and x < 100:
            print(" | ", x, end=" | ")
        else:
            print(" | ", x, end=" | ")
    print()
    
