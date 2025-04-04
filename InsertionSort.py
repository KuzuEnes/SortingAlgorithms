def insertion_sort(liste):
    for i in range(1, len(liste)):
        anahtar = liste[i]
        j = i - 1
        while j >= 0 and anahtar < liste[j]:
            liste[j + 1] = liste[j]
            j -= 1
        liste[j + 1] = anahtar
    return liste


sayilar = [12, 11, 13, 5, 6]
print(insertion_sort(sayilar))
# Bu algoritma, bir elemanı diğerlerinden küçük veya büyük olduğu durumda uygun konuma yerleştirerek çalışır.
# Time Complexity : O(n²)
# Space Complexity : O(1)