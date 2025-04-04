def merge_sort(liste):
    if len(liste) > 1:
        orta = len(liste) // 2
        sol = liste[:orta]
        sag = liste[orta:]

        merge_sort(sol)
        merge_sort(sag)

        i = j = k = 0

        while i < len(sol) and j < len(sag):
            if sol[i] < sag[j]:
                liste[k] = sol[i]
                i += 1
            else:
                liste[k] = sag[j]
                j += 1
            k += 1

        while i < len(sol):
            liste[k] = sol[i]
            i += 1
            k += 1

        while j < len(sag):
            liste[k] = sag[j]
            j += 1
            k += 1
    return liste

# Örnek kullanım
sayilar = [38, 27, 43, 3, 9, 82, 10]
print(merge_sort(sayilar))

#Time Complexity : O(nlogn)
#Space Complexity: O(n)

# 1.Bölme (Divide): İlk olarak, sıralanacak diziyi ortadan ikiye böleriz. Bu işlem, dizinin ortasını bulmak ve ikiye ayırmak için yapılır. Bu adım, dizinin eleman sayısı tek veya çift olsa da aynı şekilde uygulanır.
# 2.Fethetme (Conquer): Her iki yarıyı (veya alt diziyi) ayrı ayrı sıralamak için Merge Sort algoritmasını tekrar uygularız. Bu, dizinin parçalara kadar bölünene kadar tekrarlanır. Bu adımda, dizinin uzunluğu 1'e ulaştığında birleştirme adımına geçilir.
# 3.Birleştirme (Merge): Parçalara ayrılmış olan dizileri birleştirerek sıralı bir dizi oluştururuz. Birleştirme işlemi sırasında, iki alt dizi sıralı olarak kabul edilir ve bunlar tek bir sıralı dizi haline getirilir.
