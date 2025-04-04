def selection_sort(liste):
    n = len(liste)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if liste[j] < liste[min_index]:
                min_index = j
        liste[i], liste[min_index] = liste[min_index], liste[i]
    return liste

# Örnek kullanım
sayilar = [64, 25, 12, 22, 11]
print(selection_sort(sayilar))

# Time Complexity : O(n²)
# Space Complexity : O(1)

# 1.Dizinin ilk elemanını, dizideki en küçük (veya en büyük, sıralama türüne bağlı olarak) elemanla değiştir.
# 2.İkinci elemanı, dizinin ikinci elemanından başlayarak son elemana kadar olan alt dizideki en küçük (veya en büyük) elemanla değiştir.
# 3.Bu işlemi dizinin son elemanına kadar tekrarlayın.

