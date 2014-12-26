from random import randint

def bubblesort(nums):
    while True:
        swapped = False
        for i in range(0,len(nums)-1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                swapped = True 

        if not swapped:
            break
    return nums

def mergesort(nums):
    if len(nums) <= 1:
        return nums

    left = nums[:len(nums)/2]
    right = nums[len(nums)/2:]

    return merge(mergesort(left),mergesort(right))

def merge(left, right):
    result =    []
    index_l =   0
    index_r =   0

    while index_l < len(left) and index_r < len(right):
        if left[index_l] < right[index_r]:
            result.append(left[index_l])
            index_l += 1
        else:
            result.append(right[index_r])
            index_r += 1

    return result + left[index_l:] + right[index_r:]

def main(args):
    list = [randint(1,500) for x in range(0,int(args[1]))]
    print 'Unsorted: ' + ' '.join([str(x) for x in list])
    print 'Merge Sort: ' + ' '.join([str(x) for x in mergesort(list)])
    print 'Bubble Sort: ' + ' '.join([str(x) for x in bubblesort(list)])

if __name__ == '__main__':
    import sys
    main(sys.argv)