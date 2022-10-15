import random
pass_part_one = []
pass_part_two = []
pass_part_three = []
password = []
debug_list = ["~"]

len_one = random.randint(1,16)
len_two = random.randint(1,16)
len_three = random.randint(1,16)

for i in range(len_one):
    pass_part_one += "N"

for i in range(len_two):
    pass_part_two += "Y"

for i in range(len_three):
    pass_part_three += "A"

final_pass = "".join(pass_part_one + pass_part_two + pass_part_three + debug_list)

print(final_pass)
"""
import random
ls = [random(10) for i in range(4)]
letters = ["n","y","a","~"]
print(N+"".join([letters[i]*ls[i] for i in range(4)]))
"""