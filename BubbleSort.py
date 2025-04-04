def bubble_sort(liste):
    n = len(liste)
    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste

# Örnek kullanım
sayilar = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(sayilar))

#Time Complexity : O(n²)
#Space Complexity : O(1)

# 1.Dizinin ilk elemanından başlayarak, her elemanı bir sonraki elemanla karşılaştır.
# 2.Eğer bir önceki eleman, bir sonraki elemandan büyükse, bu iki elemanın yerini değiştir.
# 3.Bu işlem, dizinin sonuna kadar devam eder.
# 4.Dizinin sonuna gelindiğinde, en büyük eleman dizinin en sonuna gelir.
# 5.Bu adımlar, dizideki elemanlar sıralanana kadar tekrarlanır.