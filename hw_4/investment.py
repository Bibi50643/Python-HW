class Investment:
      def __init__(self,principal,interest,n):
          self.principal = principal
          self.interest = interest
          self.n = n

      def value_after(self):

          return_investment = self.principal*(1+self.interest)**self.n
          return return_investment

      def __str__(self):
          return ( deposit.value_after())




deposit = Investment(1000,5.12,3)
print(deposit.__str__())