from unittest import TestCase
from implementations import clearBit, clearBitsMostSignificantThroughI, clearBitsithrough0


class BitManipulationTest(TestCase):

    def test_clear_bit(self):
        self.assertEqual(clearBit(3, 1), 1)

    def test_clearBitsMostSignificantThroughI(self):
        self.assertEqual(clearBitsMostSignificantThroughI(8, 3), 0)

    def test_clearBitsithrough0(self):
        self.assertEqual(clearBitsithrough0(7, 1), 4)
