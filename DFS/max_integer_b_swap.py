

def get_max_integer_with_k_swaps(M, k):
    M_list = [int(digit) for digit in str(M)]

    def get_max_number_from_index(index, remaining_swaps):
        if remaining_swaps == 0 or index >= len(M_list):
            return 
        
        
        # get maximum and swap with index
        max_digit = max(M_list[index:])
        max_index = [i for i in range(len(M_list) - 1, -1, -1) if M_list[i] == max_digit][0]

        M_list[max_index], M_list[index] = M_list[index], M_list[max_index]

        get_max_number_from_index(index + 1, k - 1)


    get_max_number_from_index(0, k)
    M_list = [str(n) for n in M_list]
    return ''.join(M_list)



print(get_max_integer_with_k_swaps(7599, 2))
