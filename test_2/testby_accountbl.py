from model.entity.customer import *
from bl.account_bl import *
from model.da.db import DataAccess

da = DataAccess(Customer)

Custom_1 = Customer("ali", "alipour", "1234", "1231534789", "ali", "ali123")
da.save(Custom_1)

Custom_2 = Customer("reza", "rezaaii", "5678", "0078956678", "rezagood", "rezaiii12355")
da.save(Custom_2)

dd = DataAccess(account)
account_1 = Account("reza", "rezaaii", "5678")
account_1.customer = Custom_2
da.save(account_1)
account_2 = Account("ali", "alipor", "1234")
account_2.customer = Custom_1
da.save(account_2)

tt = Transaction("5678", "outcome", "10000", "انتقال وجه")
tt.sender = account_1
tt_2 = Transaction(1234, "income", 10000, "دریافت وجه")
tt_2.receiver = account_2
