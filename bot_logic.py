import random
def gen_pass(pass_length):
    from bot_logic import gen_pass
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)
        
    return password
from bot_logic import gen_pass
gen_pass(5)










