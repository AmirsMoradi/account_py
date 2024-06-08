from model.da.db import DataAccess
from model.entity.customer import *

da = DataAccess(Customer)

cu = Customer(None,"ali", "alipour","1234","1231534789","ali","ali123")
da.save(cu)
print(cu)
# Account(1,"ali","mohseni",222146619,)
