import unittest
from main import check_eligibility

class TestBooksellerManagerEligibility(unittest.TestCase):

    def test_eligibility_pass(self):
        # Test case: meets requirements
        result = check_eligibility(4, 2)  # More than minimum required experience
        self.assertIn("Congratulations! You are eligible", result)

    def test_eligibility_fail_booksales(self):
        # Test case: not enough bookselling experience
        result = check_eligibility(2, 2)  # Not enough bookselling years
        self.assertIn("Sorry, you do not meet the requirements", result)
        self.assertIn("3 years of being a bookseller", result)

    def test_eligibility_fail_manager(self):
        # Test case: not enough manager experience
        result = check_eligibility(4, 0)  # Not enough manager years
        self.assertIn("Sorry, you do not meet the requirements", result)
        self.assertIn("1 year as a bookseller manager", result)

    def test_eligibility_fail_both(self):
        # Test case: neither criteria is met
        result = check_eligibility(1, 0)  # Neither criteria met
        self.assertIn("Sorry, you do not meet the requirements", result)

if __name__ == "__main__":
    unittest.main()
