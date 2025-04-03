def bubble_sort(liste):
    n = len(liste)
    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste

sayilar = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(sayilar))

# Temel işleyiş mantığı, bir dizideki ardışık elemanları karşılaştırarak, eğer sıralama kriterlerine uymuyorsa yer değiştirmektir.
#Time Complexity : O(n²)

#Space Complexity : O(1)