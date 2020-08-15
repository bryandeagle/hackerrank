def count_substring(string, sub_string):
    l = len(sub_string)
    count = 0
    for i in range(len(string) - l+1):
        if string[i:i+l] == sub_string:
            count += 1
    return count
