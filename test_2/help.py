def find_by_family(self, event):
    status, customer_list = CustomerBl.find_by_family(self.search_family.variable.get())
    if status:
        self.table.refresh_table(customer_list)