def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

# Örnek kullanım
sayilar = [12, 11, 13, 5, 6, 7]
print(heap_sort(sayilar))

#Time Complexity : O(nlogn)
#Space Complexity: O(1)

# 1.Heap Yapısı Oluşturma: İlk adımda, sıralanacak diziyi bir maksimum (max heap) veya minimum (min heap) heap yapısına dönüştürürüz. Bu, diziyi bir ağaç yapısı olarak düşündüğümüzde, her düğümün sol ve sağ alt düğümlerinden daha büyük (veya küçük) olduğu bir yapının oluşturulması anlamına gelir.
# 2.Heap Yapısının Sıralanması: Oluşturulan heap yapısında, kök düğüm (en büyük veya en küçük eleman) ile son elemanın yerini değiştirerek heap yapısını güncelleriz. Bu adım, heap yapısındaki kök elemanı alıp (veya kökten en son elemanı çıkarıp), yeni kökten başlayarak heap yapısını yeniden düzenlemeyi gerektirir.
# 3.Yeniden Düzenleme ve Tekrar Sıralama: Yeniden düzenlenen heap yapısını tekrar sıralayarak, sıralanmış bir dizi elde ederiz. Bu adım, heap yapısında tekrarlanan sıralama ve düzenleme işlemlerini gerektirir.
