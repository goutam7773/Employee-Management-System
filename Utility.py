def input_is_valid(msg,start=0,end=None):
    while True:
        inp = input(msg)
        if  not inp.isdecimal():
            print("Invaild input!,try again")
        elif start is not None and end is not None:
            if not(start<= int(inp) <= end):
                print("Invalid range try again!")
            else:
                return int(inp)
        else:
            return int(inp)