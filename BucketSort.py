def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    min_val = min(arr)
    max_val = max(arr)
    bucket_count = len(arr)
    bucket_size = (max_val - min_val) / bucket_count + 1

    buckets = [[] for _ in range(bucket_count)]

    for num in arr:
        index = int((num - min_val) / bucket_size)
        buckets[index].append(num)

    sorted_arr = []
    for bucket in buckets:
        sorted_arr.extend(sorted(bucket))

    return sorted_arr

# Örnek kullanım
sayilar = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
print(bucket_sort(sayilar))

#Time Complexity : O(n²)
#Space Complexity: O(n + k)

# 1.Bucketlara Atama (Assignment to Buckets): İlk adımda, sıralanacak dizideki elemanlar belirli aralıklara atanarak bucketlara yerleştirilir. Bu aralıklar, sıralanacak elemanların dağılımına bağlı olarak belirlenir.
# 2.Bucketları Sıralama (Sorting Buckets): Her bir bucket içindeki elemanlar, bir stabil sıralama algoritması kullanılarak sıralanır. Bu adımda, bucketlarda bulunan elemanların sırası belirlenir.
# 3.Birleştirme (Merging): Son olarak, sıralanmış bucketlar birleştirilerek tam sıralanmış bir dizi elde edilir. Bu adımda, her bir bucket sırasıyla birleştirilerek orijinal dizinin sırası elde edilir.
