# -*- coding: utf-8 -*-
import random
import string
original_orderid_letter = string.ascii_letters
original_orderid_digital = string.digits
orderid_list = random.sample(original_orderid_letter,3) + random.sample(original_orderid_digital,7)
orderid = ''.join(orderid_list)
print(orderid)

