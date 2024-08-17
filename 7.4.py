def common_elements():

    set_div3 = {x for x in range(100) if x % 3 == 0}
    set_div5 = {x for x in range(100) if x % 5 == 0}

    common_set = set_div3 & set_div5

    return common_set

print(common_elements())