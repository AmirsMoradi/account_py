from model.entity.customer import *
from bl.account_bl import *
from model.da.db import DataAccess

da = DataAccess(Customer)

Custom_1 = Customer("ali", "alipour", "1234", "1231534789", "ali", "ali123")
da.save(Custom_1)

Custom_2 = Customer("reza", "rezaaii", "5678", "0078956678", "rezagood", "rezaiii12355")
da.save(Custom_2)

dd = DataAccess(account)
account_1=Account("reza", "rezaaii", "5678")
da.save(account_1)


tt=Transaction("5678", "outcome", "10000","انتقال وجه")