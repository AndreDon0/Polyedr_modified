import unittest
from unittest.mock import patch, mock_open
from common.tk_drawer import TkDrawer
from shadow.polyedr import Polyedr


class TestPolyedr(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        fake_file_content = """200.0	45.0	45.0	30.0
8	6	24
-0.5	-0.5	0.5
-0.5	0.5	0.5
0.5	0.5	0.5
0.5	-0.5	0.5
-0.5	-0.5	-0.5
-0.5	0.5	-0.5
0.5	0.5	-0.5
0.5	-0.5	-0.5
4	1    2    3    4
4	5    6    2    1
4	3    2    6    7
4	3    7    8    4
4	1    4    8    5
4	8    7    6    5
"""

        fake_file_path = 'data/holey_cube.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)

    def test_num_vertexes(self):
        self.assertEqual(len(self.polyedr.vertexes), 8)

    def test_num_facets(self):
        self.assertEqual(len(self.polyedr.facets), 6)

    def test_num_edges(self):
        self.assertEqual(len(self.polyedr.edges), 24)

    def test_solve_task64_1(self):
        answer = self.polyedr.solve_task64()
        self.assertAlmostEqual(answer, 0.0)

    def test_solve_task64_2(self):
        p = Polyedr("data/task64.geom")
        answer = p.solve_task64()
        self.assertAlmostEqual(answer, 2.0)
