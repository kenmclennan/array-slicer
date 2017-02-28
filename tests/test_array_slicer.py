import unittest
from array_slicer import ArraySlicer

class TestArraySlicer(unittest.TestCase):
    def setUp(self):
        self.array   = [1,2,3,4,5]
        self.subject = ArraySlicer(self.array)

    def test_initialization(self):
        self.assertIsInstance(self.subject, ArraySlicer)
        self.assertEqual(self.subject.array, self.array)

    def test_it_slices_an_array_into_n_parts(self):
        result = self.subject.slice_into(3)
        self.assertEqual(result, [[1,2],[3,4],[5]])

    def test_when_n_exceeds_array_length_it_pads_result(self):
        result = self.subject.slice_into(6)
        self.assertEqual(result, [[1],[2],[3],[4],[5],[]])

    def test_when_n_is_zero_it_returns_empty(self):
        result = self.subject.slice_into(0)
        self.assertEqual(result,[])

    def test_when_n_is_a_negative_integer_it_raises(self):
        self.assertRaises(ValueError,self.subject.slice_into,-1)

    def test_when_array_is_empty_it_returns_empty_slices(self):
        result = ArraySlicer([]).slice_into(2)
        self.assertEqual(result, [[],[]])


if __name__ == '__main__':
    unittest.main()