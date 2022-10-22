from win10toast import ToastNotifier
from random import randint


def bubbleSort(array):
    n = len(array)
    for i in range(n):
        already_sorted = True

        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = False

        if already_sorted:
            break

    return array


toaster = ToastNotifier()
array = [randint(-3000, 3000) for i in range(3000)]

toaster.show_toast("Dou-ME : 근처에 도움이 필요합니다!",
                   "도움을 주려면 이 창을 눌러주세요!",
                   icon_path=None,
                   duration=5,
                   threaded=True)

# 작업 끝날 때 까지
while toaster.notification_active():
    bubbleSort(array)

toaster.show_toast("Bubble Sort",
                   f"The array is sorted {array}",
                   icon_path=None,
                   duration=10,
                   threaded=False)