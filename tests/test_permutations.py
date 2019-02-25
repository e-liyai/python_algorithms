from unittest import TestCase
from implementations import permutation


class PermutationTest(TestCase):

    def setUp(self):
        self.perm_result = permutation(list('abc'))

    def test_permutation(self):
        self.assertTrue(self.perm_result)

    def test_output_vales(self):
        self.assertEqual(self.perm_result[0], ['a', 'b', 'c'])
        self.assertEqual(self.perm_result[5], ['c', 'b', 'a'])
