from BankDetails import BankDetails  # If in same folder

class CreditCards(BankDetails):
    def __init__(self, custid, cname, bal, credit_limit, credit_score):
        super().__init__(custid, cname, bal)
        self.credit_limit = credit_limit
        self.credit_score = credit_score

    def display_cc_details(self):
        print(f'Credit Limit: {self.credit_limit}, Credit Score: {self.credit_score}')
