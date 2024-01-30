# Partition given string in such manner that i’th substring is sum of (i-1)’th and (i-2)’nd substring. 

# Examples:

# Input : "11235813"
# Output : ["1", "1", "2", "3", "5", "8", "13"]

# Input : "1111223"
# Output : ["1", "11", "12", "23"]

# Input : "1111213"
# Output : ["11", "1", "12", "13"]

# Input : "11121114"
# Output : []

# size of array will be atleast 3
# consider all possible substrings and check if you satisy the condition


def get_partitioned_string(s):
    partitioned_string_list = []
    def get_partitioned_string_from(start_index, current_partition_list):
        if (start_index >= len(s)) and (len(current_partition_list) >= 3):
            partitioned_string_list.append(current_partition_list[:])
            return
        
        # consider all possible indexes from start to (end - 2)
        for end_index in range(start_index + 1, len(s) + 1):
            if len(current_partition_list) > 1 and int(s[start_index: end_index]) != int(current_partition_list[-1]) + int(current_partition_list[-2]):
                continue
            current_partition_list.append(s[start_index: end_index])
            get_partitioned_string_from(end_index, current_partition_list)
            current_partition_list.pop()

    get_partitioned_string_from(0, [])
    return partitioned_string_list[0] if partitioned_string_list else [] 

print(get_partitioned_string('11121114'))