class Check:
    num = input("Enter binary no:.")

    @classmethod
    def check_binary(cls):
        for a in cls.num:
            if a != "0" and a != "1":
                print("please enter valid binary no.")
                exit()
        print("Correct binary format")
        return

    @classmethod
    def swap_binary(cls):
        swap_no = cls.num
        i = 0
        while i <= len(swap_no):
            if swap_no[i] == "0":
                swap_no[i] = "1"
            else:
                swap_no[i] = "0"
            i += 1
        print(swap_no)
        return
    pass


binary = Check()
binary.check_binary()
binary.swap_binary()
