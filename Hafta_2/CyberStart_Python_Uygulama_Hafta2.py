import math
points = [(10,20),
        (10,12),
        (4,3),
        (3,11),
        (8,3),
        (5,7),
        (2,12),]

distances = []
distances_index = []

def euclideanDistance(i,j):
    x1 , y1 = points[i]
    x2 , y2 = points[j]

    return math.sqrt( ((x2 - x1)**2)  +  ((y2 - y1)**2) )


for i in range(len(points)):
    for j in range(len(points)):
        if i != j :
            mesafe = euclideanDistance(i,j)
            distances.append(mesafe)
            distances_index.append((i,j))
            print(f"Nokta:{i} ile nokta:{j} arasindaki mesafe = {mesafe:.2f}")


kisa_mesafe = min(distances)

index_no = distances.index(min(distances)) # distances arasından en kısa mesafenin olduğu indexin numarasını aldı. ==> yani 23 nolu index

asil_nokta = distances_index[index_no] # yukarıdaki döngülerde sırası ile distances_index içerisine mesafelerin karşılık geldiği x ve y numaraalarını eklemiştik
                                     # yukarıdan aldığımız endex no ile distances_index içerisindeki en kısa mesafeyi veren iki noktayı belirlemiş olduk.   

print(f"İki nokta arasi en kisa mesafe: {kisa_mesafe:.2f}")
print(f"Bu mesafe Nokta:{asil_nokta[0]} ile Nokta:{asil_nokta[1]} arasindadir.")


# ** ÇIKTI ** 
# Nokta:0 ile nokta:1 arasindaki mesafe = 8.00
# Nokta:0 ile nokta:2 arasindaki mesafe = 18.03
# Nokta:0 ile nokta:3 arasindaki mesafe = 11.40
# Nokta:0 ile nokta:4 arasindaki mesafe = 17.12
# Nokta:0 ile nokta:5 arasindaki mesafe = 13.93
# Nokta:0 ile nokta:6 arasindaki mesafe = 11.31
# Nokta:1 ile nokta:0 arasindaki mesafe = 8.00
# Nokta:1 ile nokta:2 arasindaki mesafe = 10.82
# Nokta:1 ile nokta:3 arasindaki mesafe = 7.07
# Nokta:1 ile nokta:4 arasindaki mesafe = 9.22
# Nokta:1 ile nokta:5 arasindaki mesafe = 7.07
# Nokta:1 ile nokta:6 arasindaki mesafe = 8.00
# Nokta:2 ile nokta:0 arasindaki mesafe = 18.03
# Nokta:2 ile nokta:1 arasindaki mesafe = 10.82
# Nokta:2 ile nokta:3 arasindaki mesafe = 8.06
# Nokta:2 ile nokta:4 arasindaki mesafe = 4.00
# Nokta:2 ile nokta:5 arasindaki mesafe = 4.12
# Nokta:2 ile nokta:6 arasindaki mesafe = 9.22
# Nokta:3 ile nokta:0 arasindaki mesafe = 11.40
# Nokta:3 ile nokta:1 arasindaki mesafe = 7.07
# Nokta:3 ile nokta:2 arasindaki mesafe = 8.06
# Nokta:3 ile nokta:4 arasindaki mesafe = 9.43
# Nokta:3 ile nokta:5 arasindaki mesafe = 4.47
# Nokta:3 ile nokta:6 arasindaki mesafe = 1.41
# Nokta:4 ile nokta:0 arasindaki mesafe = 17.12
# Nokta:4 ile nokta:1 arasindaki mesafe = 9.22
# Nokta:4 ile nokta:2 arasindaki mesafe = 4.00
# Nokta:4 ile nokta:3 arasindaki mesafe = 9.43
# Nokta:4 ile nokta:5 arasindaki mesafe = 5.00
# Nokta:4 ile nokta:6 arasindaki mesafe = 10.82
# Nokta:5 ile nokta:0 arasindaki mesafe = 13.93
# Nokta:5 ile nokta:1 arasindaki mesafe = 7.07
# Nokta:5 ile nokta:2 arasindaki mesafe = 4.12
# Nokta:5 ile nokta:3 arasindaki mesafe = 4.47
# Nokta:5 ile nokta:4 arasindaki mesafe = 5.00
# Nokta:5 ile nokta:6 arasindaki mesafe = 5.83
# Nokta:6 ile nokta:0 arasindaki mesafe = 11.31
# Nokta:6 ile nokta:1 arasindaki mesafe = 8.00
# Nokta:6 ile nokta:2 arasindaki mesafe = 9.22
# Nokta:6 ile nokta:3 arasindaki mesafe = 1.41
# Nokta:6 ile nokta:4 arasindaki mesafe = 10.82
# Nokta:6 ile nokta:5 arasindaki mesafe = 5.83
# İki nokta arasi en kisa mesafe: 1.41
# Bu mesafe Nokta:3 ile Nokta:6 arasindadir.