def counting_sort_exp(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1

    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        counting_sort_exp(arr, exp)
        exp *= 10
    return arr

# Örnek kullanım
sayilar = [170, 45, 75, 90, 802, 24, 2, 66]
print(radix_sort(sayilar))

#Time Complexity : O(n+k)
#Space Complexity: O(n + k)

# 1.Basamaklara Göre Sıralama (Sorting by Digits): İlk adımda, elemanlar basamak değerlerine göre gruplanır ve sıralanır. Bu, en az önemli basamaktan (örneğin, birler basamağı) başlayarak en önemli basamağa (örneğin, binler basamağı) kadar yapılır.
# 2.Stable Sıralama Kullanma (Using Stable Sorting): Her bir basamak değeri için sıralama işlemi, stabil bir sıralama algoritması kullanılarak yapılır. Stabil bir sıralama algoritması, aynı değere sahip elemanların sıralanma sırasını değiştirmemesini sağlar.
# 3.Her Basamak İçin Sıralama İşlemi (Sorting Process for Each Digit): En az önemli basamaktan başlayarak en önemli basamağa kadar her bir basamak değeri için sıralama işlemi gerçekleştirilir. Bu, elemanların basamak değerlerine göre gruplanmasını ve sıralanmasını içerir.
# 4.Tekrarlama (Iteration): Sıralama işlemi, elemanların en önemli basamağına kadar tekrarlanır. Bu, elemanların tamamen sıralanmasını sağlar.

