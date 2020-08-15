if __name__ == '__main__':
    nums = input()
    nums = nums.split(' ')
    for i in range(len(nums)):
        nums[i] = int(nums[i])

    A = nums[0]
    B = nums[1]
    C = nums[2]
    D = nums[3]

    if (B > C) and (D > A) and ((C + D) > (A + B)) and (C and D > 0) and (A%2==0):
        print('Valores aceitos')
    else:
        print('Valores nao aceitos')