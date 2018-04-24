def miniMaxSum(arr):
    min_list = arr[0:4]
    max_list = arr[0:4]
    
    for [index,value] in enumerate(arr[4:]):
        x = min_list[0]
        y = max_list[0]
        
        for item in min_list:
            if item > x:
                x = item
        for item in max_list:
            if item < y:
                y = item
                
        if value < x:
            for [min_index,item] in enumerate(min_list):
                if item == x:
                    min_list[min_index] = value
                    break
                    
        if value > y:
            for [max_index,item] in enumerate(max_list):
                if item == y:
                    max_list[max_index] = value
                    break
    
    return (sum(min_list), sum(max_list))

if __name__ == '__main__':
    arr = [1,2,3,4,5]
    print "Input: " + str(arr)
    print "Output:" + str(miniMaxSum(arr))

    arr = [140638725, 436257910, 953274816, 734065819, 362748590]
    print "Input: " + str(arr)
    print "Output:" + str(miniMaxSum(arr))

    arr = [0, 0, 1, 0]
    print "Input: " + str(arr)
    print "Output:" + str(miniMaxSum(arr))
