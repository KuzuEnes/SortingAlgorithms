def quick_sort(liste):
    if len(liste) <= 1:
        return liste

    pivot = liste[len(liste) // 2]
    sol = [x for x in liste if x < pivot]
    orta = [x for x in liste if x == pivot]
    sag = [x for x in liste if x > pivot]

    return quick_sort(sol) + orta + quick_sort(sag)

# Örnek kullanım
sayilar = [10, 7, 8, 9, 1, 5]
print(quick_sort(sayilar))

#Time Complexity : O(nlogn)
#Space Complexity: O(logn)

# 1.Bölme (Partitioning): Diziden bir eleman seçilir ve bu elemana “pivot” denir. Dizi, pivot elemanın solunda pivot’tan küçük, sağında ise pivot’tan büyük elemanlar olacak şekilde bölünür. Bu işlem, pivot elemanın doğru konumunu bulana kadar devam eder.
# 2.Fethetme (Conquering): Pivot eleman, doğru konumuna yerleştirildikten sonra, diziyi ikiye böleriz. Her iki alt dizi için aynı işlemi tekrar ederiz. Bu adım, dizinin her ikiye bölünmesiyle rekürsif olarak gerçekleşir.
# 3.Birleştirme (Merge): Bu adımda genellikle bir şey yapmamıza gerek yoktur, çünkü Quick Sort diziyi bölerek ve sıralayarak kendini düzenler.
