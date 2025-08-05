from django.http import JsonResponse

def bubble_sort(request):
    if request.method == 'POST':
        data = request.POST.get('array', '')
        array = list(map(int, data.split(',')))
        sorted_array = bubble_sort_logic(array)
        return JsonResponse({'sortedArray': sorted_array})

def bubble_sort_logic(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
