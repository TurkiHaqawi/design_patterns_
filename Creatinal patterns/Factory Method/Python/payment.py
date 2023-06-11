

# Abstract Class or Interface Class
class AbstractPayment:
    def process_payment(self, amount):
        pass


# Concrate Class for MadaPayment
class MadaPayment(AbstractPayment):
    def process_payment(self, amount):
        print("Mada Payment")


# Concrate Class for ApplyPayPayment
class ApplyPayPayment(AbstractPayment):
    def process_payment(self, amount):
        print("ApplyPay Payment")


# Concrate Class for PaypalPayment
class PaypalPayment(AbstractPayment):
    def process_payment(self, amount):
        print("Paypal Payment")


# Factory class
class PaymentFactory:
    @staticmethod
    def create_payment_process(payment_type):
        if payment_type == "ApplePay":
            return ApplyPayPayment()
        elif payment_type == "Mada":
            return MadaPayment()
        elif payment_type == "Paypal": 
            return PaypalPayment()
        else: 
            raise Exception("Unknown payment type")
        



# Client code
payment_type = "ApplePay"
amount = 50


pay = PaymentFactory.create_payment_process(payment_type)
print(pay.process_payment(amount))


# What we achive in this structure

# 1) فصلنا الافز والكرييشن عن ابستراكت كلاس و ذكونكريت كلاس
# 2) its ease to add new payment type.
# 3) encapsulate object creation.
