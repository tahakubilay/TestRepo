import random
import string

listlow="abcdefghijklmnoprstuvyzwq"
listup="ABCDEFGHIJKLMNOPRSTUVYZWQ"
listnumber="123456789"
listsymbols="!?+*.,:;"

length=int(input("Kaç haneli olsun: "))
 
all=listlow+listup+listsymbols+listnumber
password = "".join(random.sample(all,length))
print(password)