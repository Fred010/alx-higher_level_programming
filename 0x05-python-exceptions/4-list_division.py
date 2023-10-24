#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    recent_list = []
    for index in range(list_length):
        try:
            recent_list.append(my_list_1[index] / my_list_2[index])
        except ZeroDivisionError:
            recent_list.append(0)
            print("division by 0")
            continue
        except IndexError:
            recent_list.append(0)
            print("out of range")
            continue
        except TypeError:
            recent_list.append(0)
            print("wrong type")
            continue
        finally:
            pass
    return recent_list
