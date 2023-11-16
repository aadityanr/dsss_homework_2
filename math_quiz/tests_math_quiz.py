import unittest
from math_quiz import random_generator, generate_random_operator, arithmetic_operation


class TestMathGame(unittest.TestCase):

    def test_random_generator(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_generator(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_generate_random_operator(self):
        for i in range(1,5):
            operator = generate_random_operator()
            self.assertIn(operator, ['+', '-', '*'])


    def test_arithmetic_operation(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (6, 7, '-', '6 - 7', -1),
                (6, 7, '*', '6 * 7', 42),
                (6, -7, '+', '6 + -7', -1)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                actual_expression, actual_answer = arithmetic_operation(num1, num2, operator)
                self.assertEqual(expected_problem, actual_expression)
                self.assertEqual(expected_answer, actual_answer)

if __name__ == "__main__":
    unittest.main()
