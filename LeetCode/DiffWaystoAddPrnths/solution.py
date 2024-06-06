class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        # Helper function to perform the computation
        def compute(left, right, op):
            if op == '+':
                return left + right
            elif op == '-':
                return left - right
            elif op == '*':
                return left * right

        # If the expression is a single number, return it as the only result
        if expression.isdigit():
            return [int(expression)]

        results = []
        # Iterate through each character in the expression
        for i in range(len(expression)):
            if expression[i] in "+-*":
                # Recursively solve for the left and right parts of the expression
                left_results = self.diffWaysToCompute(expression[:i])
                right_results = self.diffWaysToCompute(expression[i+1:])

                # Compute all combinations of left and right results with the current operator
                for left in left_results:
                    for right in right_results:
                        results.append(compute(left, right, expression[i]))

        return results