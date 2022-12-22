from main import input_to_elves, sum_elves, most_calories
import unittest

FILE_PATH = './test_input.txt'


class TestMain(unittest.TestCase):
    def test_input_to_elves(self):
        expected = [[1000, 2000, 3000], [4000],
                    [5000, 6000], [7000, 8000, 9000]]
        self.assertEqual(expected, input_to_elves(FILE_PATH))

    def test_sum_elves(self):
        elves = input_to_elves(FILE_PATH)
        expected = [6000, 4000, 11_000, 24_000]
        self.assertEqual(expected, sum_elves(elves))

    def test_most_calories(self):
        elves = input_to_elves(FILE_PATH)
        sums = sum_elves(elves)
        expected = 24_000
        self.assertEqual(expected, most_calories(sums))


if __name__ == '__main__':
    unittest.main()
