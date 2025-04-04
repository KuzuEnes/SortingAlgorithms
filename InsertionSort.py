def insertion_sort(liste):
    for i in range(1, len(liste)):
        anahtar = liste[i]
        j = i - 1
        while j >= 0 and anahtar < liste[j]:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = anahtar
    return liste

# Örnek kullanım
sayilar = [12, 11, 13, 5, 6]
print(insertion_sort(sayilar))
# Time Complexity : O(n²)
# Space Complexity : O(1)
# 1.Dizinin ikinci elemanından başlayarak, her elemanı birbirinden önceki sıralı diziyle karşılaştır.
# 2.Karşılaştırılan elemandan daha büyük olan elemanları sağa kaydır ve uygun konuma elemanı yerleştir.
# 3.Bu işlem, dizinin son elemanına kadar devam eder.
# 4.Dizinin sonuna gelindiğinde, tüm elemanlar sıralı olur.
