def count_substring(string, sub_string):
    sub_string_len = len(sub_string)
    count = 0
    for x in range(0, len(string)):
    
        if string[x:x+sub_string_len] == sub_string:
            count = count + 1

  
    return count