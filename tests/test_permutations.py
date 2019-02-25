from unittest import TestCase
from implementations import permutation
from implementations import permutation2


class PermutationTest(TestCase):

    def setUp(self):
        self.perm_result = permutation(list('abc'))
        self.perm2_result = list(permutation2(list('xyz')))

    def test_permutation(self):
        self.assertTrue(self.perm_result)

    def test_permutation2(self):
        self.assertTrue(self.perm2_result)

    def test_output_vales(self):
        self.assertEqual(self.perm_result[0], ['a', 'b', 'c'])
        self.assertEqual(self.perm_result[5], ['c', 'b', 'a'])

    def test_perm2_output_vales(self):
        print(self.perm2_result)
        self.assertEqual(self.perm2_result[0], ['x', 'y', 'z'])
        self.assertEqual(self.perm2_result[5], ['z', 'y', 'x'])
