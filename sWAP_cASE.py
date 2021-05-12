def swap_case(s):
    swap_all_cases = [x.upper() if x.islower() else x.lower() for x in s]
    
    return "".join(swap_all_cases)