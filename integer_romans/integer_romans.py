class integer_romans:
    def int_to_roman(self,num) -> str:
        roman_mapping = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }
        
        if num == 0:
            return ""
        else:
            for key,symbol in roman_mapping.items():
                if num >= key:
                    return symbol + self.int_to_roman(num-key)
            return ""
        



my_int = integer_romans()
print(my_int.int_to_roman(1994))
print(my_int.int_to_roman(58))
print(my_int.int_to_roman(9))
print(my_int.int_to_roman(4))