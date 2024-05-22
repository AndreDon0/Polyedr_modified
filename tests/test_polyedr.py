import unittest
from unittest.mock import patch, mock_open
from common.tk_drawer import TkDrawer
from shadow.polyedr import Polyedr


class TestPolyedr(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        fake_file_content = """200.0	45.0	45.0	30.0
8	4	16
-0.5	-0.5	0.5
-0.5	0.5	0.5
0.5	0.5	0.5
0.5	-0.5	0.5
-0.5	-0.5	-0.5
-0.5	0.5	-0.5
0.5	0.5	-0.5
0.5	-0.5	-0.5
4	5    6    2    1
4	3    2    6    7
4	3    7    8    4
4	1    4    8    5"""

        fake_file_path = 'data/holey_box.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=fake_file_content)) as _file:
            self.polyedr = Polyedr(fake_file_path)
            _file.assert_called_once_with(fake_file_path)

    def test_num_vertexes(self):
        self.assertEqual(len(self.polyedr.vertexes), 8)

    def test_num_facets(self):
        self.assertEqual(len(self.polyedr.facets), 4)

    def test_num_edges(self):
        self.assertEqual(len(self.polyedr.edges), 16)

    def test_solve_task64(self):
        task64_file_content = """1.0   0.0   0.0   0.0
3   0   1
0.0   0.0   2.0
0.0   0.0   0.0
0.0   1.0   0.0
3   1   2   3
"""
        task64_file_path = 'data/task64.geom'
        with patch('shadow.polyedr.open'.format(__name__),
                   new=mock_open(read_data=task64_file_content)) as _file:
            tk = TkDrawer()
            polyedr64 = Polyedr(task64_file_path)
            answer = polyedr64.solve_task64(tk)
            self.assertAlmostEqual(answer, 2)
