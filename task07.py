error = f"Please enter correct integers:"
def inputter_int(input_descripton, arg_error, agr_not_less, agr_not_much, arg_is):
    while True:
        try:
            i = int(input(input_descripton))
            if i < agr_not_less or i > agr_not_much or i == arg_is or arg_is is True:
                print(arg_error)
                continue
            return i
            break
        except:
            print(arg_error)
            continue
n = inputter_int(f"", error, 1, 10000, 0)
k = inputter_int(f"", error, 2, 10, 0)
