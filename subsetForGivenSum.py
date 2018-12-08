def subArraySum(arr, sum):
    checkSum = arr[0]
    counter = 0
    i = 1
    while i <= len(arr):

        # If curr_sum exceeds
        # the sum, then remove
        # the starting elements
        while checkSum > sum and counter < i - 1:
            checkSum = checkSum - arr[counter]
            counter += 1

        if checkSum == sum:
            outputList = []
            for i in range(counter, i):
                outputList.append(arr[i])
            return outputList

        if i < len(arr):
            checkSum = checkSum + arr[i]
        i += 1

    return False

print(subArraySum([13,17,4,3,30,41,2,3,4,7,4], 15))