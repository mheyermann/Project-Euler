{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6bc8a40a-017a-42e8-b3b6-64e7bf2d1141",
   "metadata": {},
   "outputs": [],
   "source": [
    "import unittest\n",
    "import mean_var_std\n",
    "\n",
    "\n",
    "# the test case\n",
    "class UnitTests(unittest.TestCase):\n",
    "    def test_calculate(self):\n",
    "        actual = mean_var_std.calculate([2,6,2,8,4,0,1,5,7])\n",
    "        expected = {'mean': [[3.6666666666666665, 5.0, 3.0], [3.3333333333333335, 4.0, 4.333333333333333], 3.888888888888889], 'variance': [[9.555555555555557, 0.6666666666666666, 8.666666666666666], [3.555555555555556, 10.666666666666666, 6.222222222222221], 6.987654320987654], 'standard deviation': [[3.091206165165235, 0.816496580927726, 2.943920288775949], [1.8856180831641267, 3.265986323710904, 2.494438257849294], 2.6434171674156266], 'max': [[8, 6, 7], [6, 8, 7], 8], 'min': [[1, 4, 0], [2, 0, 1], 0], 'sum': [[11, 15, 9], [10, 12, 13], 35]}\n",
    "        self.assertAlmostEqual(actual, expected, \"Expected different output when calling 'calculate()' with '[2,6,2,8,4,0,1,5,7]'\")\n",
    "\n",
    "    def test_calculate2(self):\n",
    "        actual = mean_var_std.calculate([9,1,5,3,3,3,2,9,0])\n",
    "        expected = {'mean': [[4.666666666666667, 4.333333333333333, 2.6666666666666665], [5.0, 3.0, 3.6666666666666665], 3.888888888888889], 'variance': [[9.555555555555555, 11.555555555555557, 4.222222222222222], [10.666666666666666, 0.0, 14.888888888888891], 9.209876543209875], 'standard deviation': [[3.0912061651652345, 3.39934634239519, 2.0548046676563256], [3.265986323710904, 0.0, 3.8586123009300755], 3.0347778408328137], 'max': [[9, 9, 5], [9, 3, 9], 9], 'min': [[2, 1, 0], [1, 3, 0], 0], 'sum': [[14, 13, 8], [15, 9, 11], 35]}\n",
    "        self.assertAlmostEqual(actual, expected, \"Expected different output when calling 'calculate()' with '[9,1,5,3,3,3,2,9,0]'\")\n",
    "    \n",
    "    def test_calculate_with_few_digits(self):\n",
    "        self.assertRaisesRegex(ValueError, \"List must contain nine numbers.\", mean_var_std.calculate, [2,6,2,8,4,0,1,])\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    unittest.main()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
