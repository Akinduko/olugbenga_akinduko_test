class compare_string:
    def __init__(self, A, B):
        self.A = float(A)
        self.B = float(B)

    # Greater than Function
    def greater(self):
        condition = self.A > self.B
        return "{0} is greater than {1}".format(self.A, self.B) if condition else \
               "{0} is greater than {1}".format(self.B, self.A)

    # Less than Function
    def lesser(self):
        condition = self.A < self.B
        return "{0} is lesser than {1}".format(self.A, self.B) if condition else \
               "{0} is lesser than {1}".format(self.B, self.A)

    # Equal to  Function
    def equal(self):
        condition = self.A == self.B
        return "{0} is equal to {1}".format(self.A, self.B) if condition else \
               "{0} is not equal to {1}".format(self.B, self.A)
