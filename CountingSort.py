def counting_sort(arr):
    if not arr:
        return []

    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1

    count = [0] * range_of_elements
    output = [0] * len(arr)

    for num in arr:
        count[num - min_val] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for num in reversed(arr):
        output[count[num - min_val] - 1] = num
        count[num - min_val] -= 1

    return output

# Örnek kullanım
sayilar = [4, 2, 2, 8, 3, 3, 1]
print(counting_sort(sayilar))

#Time Complexity : O(n+k)
#Space Complexity: O(n + k)

# 1.Sayıları Sayma (Counting): İlk adımda, sıralanacak dizideki her bir elemanın kaç kez tekrarlandığını belirlemek için bir sayıcı kullanılır. Bu sayıcı, her elemanın frekansını (kaç kez tekrarlandığını) sayar.
# 2.Kümülatif Frekanslar Oluşturma (Cumulative Frequencies): Ardından, her bir elemanın kaç kez görüldüğünü temsil eden sayıları bir araya getirerek bir kümülatif frekans tablosu oluşturulur. Bu adımda, her elemanın konumu belirlenir.
# 3.Elemanları Yerleştirme (Placing Elements): Son olarak, orijinal dizideki elemanların sırasını belirlemek için kümülatif frekans tablosu kullanılır. Bu adımda, her elemanın frekansı kullanılarak orijinal dizideki doğru konumu belirlenir ve elemanlar sıralanır.
