# Name: Robert Vermeulen
# Course:       CPE 202
# Instructor:   Daniel Kauffman
# Assignment:   Tile Driver
# Term:         Spring 2021

import unittest

import tiledriver
from tiledriver import PuzzleState as PS  # only allowed use of from ... import


class TestMakeAdjacent(unittest.TestCase):

    def test_make_adjacent_1(self):
        state = PS((3, 2, 1, 0), "")
        self.assertEqual(tiledriver.make_adjacent(state),
                         [PS((3, 0, 1, 2), "J"), PS((3, 2, 0, 1), "L")])

    def test_make_adjacent_2(self):
        state = PS((3, 0, 1, 2), "J")
        self.assertEqual(tiledriver.make_adjacent(state),
                         [PS((0, 3, 1, 2), "JL")])

    def test_make_adjacent_3(self):
        state = PS((0, 3, 1, 2), "JL")
        self.assertEqual(tiledriver.make_adjacent(state),
                         [PS((1, 3, 0, 2), "JLK")])

    def test_make_adjacent_4(self):
        state = PS((1, 3, 0, 2), "JLK")
        self.assertEqual(tiledriver.make_adjacent(state),
                         [PS((1, 3, 2, 0), "JLKH")])

    def test_make_adjacent_5(self):
        state = PS((1, 3, 2, 0), "JLKH")
        self.assertEqual(tiledriver.make_adjacent(state),
                         [PS((1, 0, 2, 3), "JLKHJ")])

    def test_make_adjacent_6(self):
        state = PS((0, 2, 4, 5, 1, 8, 3, 6, 7), 'JJ')
        self.assertEqual(tiledriver.make_adjacent(state),
                         [PS((2, 0, 4, 5, 1, 8, 3, 6, 7), 'JJH')])

    def test_make_adjacent_7(self):
        state = PS((0, 2, 4, 5, 1, 8, 3, 6, 7), 'JJ')
        self.assertEqual(tiledriver.make_adjacent(state),
                         [PS((2, 0, 4, 5, 1, 8, 3, 6, 7), 'JJH')])

    def test_make_adjacent_8(self):
        state = PS((0, 2, 4, 5, 1, 8, 3, 6, 7), 'JJ')
        self.assertEqual(tiledriver.make_adjacent(state),
                         [PS((2, 0, 4, 5, 1, 8, 3, 6, 7), 'JJH')])






class Testat02(unittest.TestCase):

    def test_at0_2_1(self):
        state = PS((0, 3, 1, 2), '')
        self.assertEqual(tiledriver.at0_2(state),
                         [PS((1, 3, 0, 2), 'K'), PS((3, 0, 1, 2), 'H')])

    def test_at0_2_2(self):
        state = PS((0, 3, 1, 2), 'J')
        self.assertEqual(tiledriver.at0_2(state),
                         [PS((3, 0, 1, 2), 'JH')])

    def test_at0_2_3(self):
        state = PS((0, 3, 1, 2), 'L')
        self.assertEqual(tiledriver.at0_2(state),
                         [PS((1, 3, 0, 2), 'LK')])

    def test_at0_2_4(self):
        state = PS((0, 3, 1, 2), 'KLJ')
        self.assertEqual(tiledriver.at0_2(state),
                         [PS((3, 0, 1, 2), 'KLJH')])

    def test_at0_2_5(self):
        state = PS((0, 3, 1, 2), 'HJL')
        self.assertEqual(tiledriver.at0_2(state),
                         [PS((1, 3, 0, 2), 'HJLK')])



class Testat12(unittest.TestCase):

    def test_at1_2_1(self):
        state = PS((3, 0, 1, 2), '')
        self.assertEqual(tiledriver.at1_2(state),
                         [PS((3, 2, 1, 0), 'K'), PS((0, 3, 1, 2), 'L')])

    def test_at1_2_2(self):
        state = PS((3, 0, 1, 2), 'H')
        self.assertEqual(tiledriver.at1_2(state),
                         [PS((3, 2, 1, 0), 'HK')])

    def test_at1_2_3(self):
        state = PS((3, 0, 1, 2), 'J')
        self.assertEqual(tiledriver.at1_2(state),
                         [PS((0, 3, 1, 2), 'JL')])

    def test_at1_2_4(self):
        state = PS((3, 0, 1, 2), 'LJH')
        self.assertEqual(tiledriver.at1_2(state),
                         [PS((3, 2, 1, 0), 'LJHK')])

    def test_at1_2_5(self):
        state = PS((3, 0, 1, 2), 'KHJ')
        self.assertEqual(tiledriver.at1_2(state),
                         [PS((0, 3, 1, 2), 'KHJL')])



class Testat22(unittest.TestCase):

    def test_at2_2_1(self):
        state = PS((1, 2, 0, 3), '')
        self.assertEqual(tiledriver.at2_2(state),
                         [PS((0, 2, 1, 3), 'J'), PS((1, 2, 3, 0), 'H')])

    def test_at2_2_2(self):
        state = PS((1, 2, 0, 3), 'L')
        self.assertEqual(tiledriver.at2_2(state),
                         [PS((0, 2, 1, 3), 'LJ')])

    def test_at2_2_3(self):
        state = PS((1, 2, 0, 3), 'K')
        self.assertEqual(tiledriver.at2_2(state),
                         [PS((1, 2, 3, 0), 'KH')])

    def test_at2_2_4(self):
        state = PS((1, 2, 0, 3), 'HKL')
        self.assertEqual(tiledriver.at2_2(state),
                         [PS((0, 2, 1, 3), 'HKLJ')])

    def test_at2_2_5(self):
        state = PS((1, 2, 0, 3), 'JLK')
        self.assertEqual(tiledriver.at2_2(state),
                         [PS((1, 2, 3, 0), 'JLKH')])



class Testat32(unittest.TestCase):

    def test_at3_2_1(self):
        state = PS((1, 2, 3, 0), '')
        self.assertEqual(tiledriver.at3_2(state),
                         [PS((1, 0, 3, 2), 'J'), PS((1, 2, 0, 3), 'L')])

    def test_at3_2_2(self):
        state = PS((1, 2, 3, 0), 'H')
        self.assertEqual(tiledriver.at3_2(state),
                         [PS((1, 0, 3, 2), 'HJ')])

    def test_at3_2_3(self):
        state = PS((1, 2, 3, 0), 'K')
        self.assertEqual(tiledriver.at3_2(state),
                         [PS((1, 2, 0, 3), 'KL')])

    def test_at3_2_4(self):
        state = PS((1, 2, 3, 0), 'LKH')
        self.assertEqual(tiledriver.at3_2(state),
                         [PS((1, 0, 3, 2), 'LKHJ')])

    def test_at3_2_5(self):
        state = PS((1, 2, 3, 0), 'JHK')
        self.assertEqual(tiledriver.at3_2(state),
                         [PS((1, 2, 0, 3), 'JHKL')])



class Testat03(unittest.TestCase):

    def test_at0_3_1(self):
        state = PS((0, 1, 2, 3, 4, 5, 6, 7, 8), '')
        self.assertEqual(tiledriver.at0_3(state),
                         [PS((3, 1, 2, 0, 4, 5, 6, 7, 8), 'K'),
                          PS((1, 0, 2, 3, 4, 5, 6, 7, 8), 'H')])

    def test_at0_3_2(self):
        state = PS((0, 1, 2, 3, 4, 5, 6, 7, 8), 'L')
        self.assertEqual(tiledriver.at0_3(state),
                         [PS((3, 1, 2, 0, 4, 5, 6, 7, 8), 'LK')])

    def test_at0_3_3(self):
        state = PS((0, 1, 2, 3, 4, 5, 6, 7, 8), 'J')
        self.assertEqual(tiledriver.at0_3(state),
                         [PS((1, 0, 2, 3, 4, 5, 6, 7, 8), 'JH')])

    def test_at0_3_4(self):
        state = PS((0, 1, 2, 3, 4, 5, 6, 7, 8), 'KHJJLL')
        self.assertEqual(tiledriver.at0_3(state),
                         [PS((3, 1, 2, 0, 4, 5, 6, 7, 8), 'KHJJLLK')])

    def test_at0_3_5(self):
        state = PS((0, 1, 2, 3, 4, 5, 6, 7, 8), 'LJLJ')
        self.assertEqual(tiledriver.at0_3(state),
                         [PS((1, 0, 2, 3, 4, 5, 6, 7, 8), 'LJLJH')])



class Testat13(unittest.TestCase):

    def test_at1_3_1(self):
        state = PS((1, 0, 2, 3, 4, 5, 6, 7, 8), '')
        self.assertEqual(tiledriver.at1_3(state),
                         [PS((1, 4, 2, 3, 0, 5, 6, 7, 8), 'K'),
                          PS((0, 1, 2, 3, 4, 5, 6, 7, 8), 'L'),
                          PS((1, 2, 0, 3, 4, 5, 6, 7, 8), 'H')])

    def test_at1_3_2(self):
        state = PS((1, 0, 2, 3, 4, 5, 6, 7, 8), 'J')
        self.assertEqual(tiledriver.at1_3(state),
                         [PS((0, 1, 2, 3, 4, 5, 6, 7, 8), 'JL'),
                          PS((1, 2, 0, 3, 4, 5, 6, 7, 8), 'JH')])

    def test_at1_3_3(self):
        state = PS((1, 0, 2, 3, 4, 5, 6, 7, 8), 'L')
        self.assertEqual(tiledriver.at1_3(state),
                         [PS((1, 4, 2, 3, 0, 5, 6, 7, 8), 'LK'),
                          PS((0, 1, 2, 3, 4, 5, 6, 7, 8), 'LL')])

    def test_at1_3_4(self):
        state = PS((1, 0, 2, 3, 4, 5, 6, 7, 8), 'H')
        self.assertEqual(tiledriver.at1_3(state),
                         [PS((1, 4, 2, 3, 0, 5, 6, 7, 8), 'HK'),
                          PS((1, 2, 0, 3, 4, 5, 6, 7, 8), 'HH')])

    def test_at1_3_5(self):
        state = PS((1, 0, 2, 3, 4, 5, 6, 7, 8), 'KKHHJJL')
        self.assertEqual(tiledriver.at1_3(state),
                         [PS((1, 4, 2, 3, 0, 5, 6, 7, 8), 'KKHHJJLK'),
                          PS((0, 1, 2, 3, 4, 5, 6, 7, 8), 'KKHHJJLL')])



class Testat23(unittest.TestCase):

    def test_at2_3_1(self):
        state = PS((2, 1, 0, 3, 4, 5, 6, 7, 8), '')
        self.assertEqual(tiledriver.at2_3(state),
                         [PS((2, 1, 5, 3, 4, 0, 6, 7, 8), 'K'),
                          PS((2, 0, 1, 3, 4, 5, 6, 7, 8), 'L')])

    def test_at2_3_2(self):
        state = PS((2, 1, 0, 3, 4, 5, 6, 7, 8), 'J')
        self.assertEqual(tiledriver.at2_3(state),
                         [PS((2, 0, 1, 3, 4, 5, 6, 7, 8), 'JL')])

    def test_at2_3_3(self):
        state = PS((2, 1, 0, 3, 4, 5, 6, 7, 8), 'H')
        self.assertEqual(tiledriver.at2_3(state),
                         [PS((2, 1, 5, 3, 4, 0, 6, 7, 8), 'HK')])

    def test_at2_3_4(self):
        state = PS((2, 1, 0, 3, 4, 5, 6, 7, 8), 'LKHHJ')
        self.assertEqual(tiledriver.at2_3(state),
                         [PS((2, 0, 1, 3, 4, 5, 6, 7, 8), 'LKHHJL')])

    def test_at2_3_5(self):
        state = PS((2, 1, 0, 3, 4, 5, 6, 7, 8), 'HHJLJH')
        self.assertEqual(tiledriver.at2_3(state),
                         [PS((2, 1, 5, 3, 4, 0, 6, 7, 8), 'HHJLJHK')])



class Testat33(unittest.TestCase):

    def test_at3_3_1(self):
        state = PS((3, 1, 2, 0, 4, 5, 6, 7, 8), '')
        self.assertEqual(tiledriver.at3_3(state),
                         [PS((3, 1, 2, 6, 4, 5, 0, 7, 8), 'K'),
                          PS((0, 1, 2, 3, 4, 5, 6, 7, 8), 'J'),
                          PS((3, 1, 2, 4, 0, 5, 6, 7, 8), 'H')])

    def test_at3_3_2(self):
        state = PS((3, 1, 2, 0, 4, 5, 6, 7, 8), 'K')
        self.assertEqual(tiledriver.at3_3(state),
                         [PS((3, 1, 2, 6, 4, 5, 0, 7, 8), 'KK'),
                          PS((3, 1, 2, 4, 0, 5, 6, 7, 8), 'KH')])

    def test_at3_3_3(self):
        state = PS((3, 1, 2, 0, 4, 5, 6, 7, 8), 'J')
        self.assertEqual(tiledriver.at3_3(state),
                         [PS((0, 1, 2, 3, 4, 5, 6, 7, 8), 'JJ'),
                          PS((3, 1, 2, 4, 0, 5, 6, 7, 8), 'JH')])

    def test_at3_3_4(self):
        state = PS((3, 1, 2, 0, 4, 5, 6, 7, 8), 'L')
        self.assertEqual(tiledriver.at3_3(state),
                         [PS((3, 1, 2, 6, 4, 5, 0, 7, 8), 'LK'),
                          PS((0, 1, 2, 3, 4, 5, 6, 7, 8), 'LJ')])

    def test_at3_3_5(self):
        state = PS((3, 1, 2, 0, 4, 5, 6, 7, 8), 'JLL')
        self.assertEqual(tiledriver.at3_3(state),
                         [PS((3, 1, 2, 6, 4, 5, 0, 7, 8), 'JLLK'),
                          PS((0, 1, 2, 3, 4, 5, 6, 7, 8), 'JLLJ')])



class Testat43(unittest.TestCase):

    def test_at4_3_1(self):
        state = PS((4, 1, 2, 3, 0, 5, 6, 7, 8), '')
        self.assertEqual(tiledriver.at4_3(state),
                         [PS((4, 1, 2, 3, 7, 5, 6, 0, 8), 'K'),
                          PS((4, 0, 2, 3, 1, 5, 6, 7, 8), 'J'),
                          PS((4, 1, 2, 0, 3, 5, 6, 7, 8), 'L'),
                          PS((4, 1, 2, 3, 5, 0, 6, 7, 8), 'H')])

    def test_at4_3_2(self):
        state = PS((4, 1, 2, 3, 0, 5, 6, 7, 8), 'H')
        self.assertEqual(tiledriver.at4_3(state),
                         [PS((4, 1, 2, 3, 7, 5, 6, 0, 8), 'HK'),
                          PS((4, 0, 2, 3, 1, 5, 6, 7, 8), 'HJ'),
                          PS((4, 1, 2, 3, 5, 0, 6, 7, 8), 'HH')])

    def test_at4_3_3(self):
        state = PS((4, 1, 2, 3, 0, 5, 6, 7, 8), 'L')
        self.assertEqual(tiledriver.at4_3(state),
                         [PS((4, 1, 2, 3, 7, 5, 6, 0, 8), 'LK'),
                          PS((4, 0, 2, 3, 1, 5, 6, 7, 8), 'LJ'),
                          PS((4, 1, 2, 0, 3, 5, 6, 7, 8), 'LL')])

    def test_at4_3_4(self):
        state = PS((4, 1, 2, 3, 0, 5, 6, 7, 8), 'J')
        self.assertEqual(tiledriver.at4_3(state),
                         [PS((4, 0, 2, 3, 1, 5, 6, 7, 8), 'JJ'),
                          PS((4, 1, 2, 0, 3, 5, 6, 7, 8), 'JL'),
                          PS((4, 1, 2, 3, 5, 0, 6, 7, 8), 'JH')])

    def test_at4_3_5(self):
        state = PS((4, 1, 2, 3, 0, 5, 6, 7, 8), 'K')
        self.assertEqual(tiledriver.at4_3(state),
                         [PS((4, 1, 2, 3, 7, 5, 6, 0, 8), 'KK'),
                          PS((4, 1, 2, 0, 3, 5, 6, 7, 8), 'KL'),
                          PS((4, 1, 2, 3, 5, 0, 6, 7, 8), 'KH')])

class Testat53(unittest.TestCase):

    def test_at5_3_1(self):
        state = PS((5, 1, 2, 3, 4, 0, 6, 7, 8), '')
        self.assertEqual(tiledriver.at5_3(state),
                         [PS((5, 1, 2, 3, 4, 8, 6, 7, 0), 'K'),
                          PS((5, 1, 0, 3, 4, 2, 6, 7, 8), 'J'),
                          PS((5, 1, 2, 3, 0, 4, 6, 7, 8), 'L')])

    def test_at5_3_2(self):
        state = PS((5, 1, 2, 3, 4, 0, 6, 7, 8), 'K')
        self.assertEqual(tiledriver.at5_3(state),
                         [PS((5, 1, 2, 3, 4, 8, 6, 7, 0), 'KK'),
                          PS((5, 1, 2, 3, 0, 4, 6, 7, 8), 'KL')])

    def test_at5_3_3(self):
        state = PS((5, 1, 2, 3, 4, 0, 6, 7, 8), 'J')
        self.assertEqual(tiledriver.at5_3(state),
                         [PS((5, 1, 0, 3, 4, 2, 6, 7, 8), 'JJ'),
                          PS((5, 1, 2, 3, 0, 4, 6, 7, 8), 'JL')])

    def test_at5_3_4(self):
        state = PS((5, 1, 2, 3, 4, 0, 6, 7, 8), 'H')
        self.assertEqual(tiledriver.at5_3(state),
                         [PS((5, 1, 2, 3, 4, 8, 6, 7, 0), 'HK'),
                          PS((5, 1, 0, 3, 4, 2, 6, 7, 8), 'HJ')])

    def test_at5_3_5(self):
        state = PS((5, 1, 2, 3, 4, 0, 6, 7, 8), 'JLLKKHJH')
        self.assertEqual(tiledriver.at5_3(state),
                         [PS((5, 1, 2, 3, 4, 8, 6, 7, 0), 'JLLKKHJHK'),
                          PS((5, 1, 0, 3, 4, 2, 6, 7, 8), 'JLLKKHJHJ')])



class Testat63(unittest.TestCase):

    def test_at6_3_1(self):
        state = PS((6, 1, 2, 3, 4, 5, 0, 7, 8), '')
        self.assertEqual(tiledriver.at6_3(state),
                         [PS((6, 1, 2, 0, 4, 5, 3, 7, 8), 'J'),
                          PS((6, 1, 2, 3, 4, 5, 7, 0, 8), 'H')])

    def test_at6_3_2(self):
        state = PS((6, 1, 2, 3, 4, 5, 0, 7, 8), 'K')
        self.assertEqual(tiledriver.at6_3(state),
                         [PS((6, 1, 2, 3, 4, 5, 7, 0, 8), 'KH')])

    def test_at6_3_3(self):
        state = PS((6, 1, 2, 3, 4, 5, 0, 7, 8), 'L')
        self.assertEqual(tiledriver.at6_3(state),
                         [PS((6, 1, 2, 0, 4, 5, 3, 7, 8), 'LJ')])

    def test_at6_3_4(self):
        state = PS((6, 1, 2, 3, 4, 5, 0, 7, 8), 'JLLKK')
        self.assertEqual(tiledriver.at6_3(state),
                         [PS((6, 1, 2, 3, 4, 5, 7, 0, 8), 'JLLKKH')])

    def test_at6_3_5(self):
        state = PS((6, 1, 2, 3, 4, 5, 0, 7, 8), 'HKKL')
        self.assertEqual(tiledriver.at6_3(state),
                         [PS((6, 1, 2, 0, 4, 5, 3, 7, 8), 'HKKLJ')])



class Testat73(unittest.TestCase):

    def test_at7_3_1(self):
        state = PS((7, 1, 2, 3, 4, 5, 6, 0, 8), '')
        self.assertEqual(tiledriver.at7_3(state),
                         [PS((7, 1, 2, 3, 0, 5, 6, 4, 8), 'J'),
                          PS((7, 1, 2, 3, 4, 5, 0, 6, 8), 'L'),
                          PS((7, 1, 2, 3, 4, 5, 6, 8, 0), 'H')])

    def test_at7_3_2(self):
        state = PS((7, 1, 2, 3, 4, 5, 6, 0, 8), 'K')
        self.assertEqual(tiledriver.at7_3(state),
                         [PS((7, 1, 2, 3, 4, 5, 0, 6, 8), 'KL'),
                          PS((7, 1, 2, 3, 4, 5, 6, 8, 0), 'KH')])

    def test_at7_3_3(self):
        state = PS((7, 1, 2, 3, 4, 5, 6, 0, 8), 'L')
        self.assertEqual(tiledriver.at7_3(state),
                         [PS((7, 1, 2, 3, 0, 5, 6, 4, 8), 'LJ'),
                          PS((7, 1, 2, 3, 4, 5, 0, 6, 8), 'LL')])

    def test_at7_3_4(self):
        state = PS((7, 1, 2, 3, 4, 5, 6, 0, 8), 'H')
        self.assertEqual(tiledriver.at7_3(state),
                         [PS((7, 1, 2, 3, 0, 5, 6, 4, 8), 'HJ'),
                          PS((7, 1, 2, 3, 4, 5, 6, 8, 0), 'HH')])

    def test_at7_3_5(self):
        state = PS((7, 1, 2, 3, 4, 5, 6, 0, 8), 'JLLKKH')
        self.assertEqual(tiledriver.at7_3(state),
                         [PS((7, 1, 2, 3, 0, 5, 6, 4, 8), 'JLLKKHJ'),
                          PS((7, 1, 2, 3, 4, 5, 6, 8, 0), 'JLLKKHH')])



class Testat83(unittest.TestCase):

    def test_at8_3_1(self):
        state = PS((8, 1, 2, 3, 4, 5, 6, 7, 0), '')
        self.assertEqual(tiledriver.at8_3(state),
                         [PS((8, 1, 2, 3, 4, 0, 6, 7, 5), 'J'),
                          PS((8, 1, 2, 3, 4, 5, 6, 0, 7), 'L')])

    def test_at8_3_2(self):
        state = PS((8, 1, 2, 3, 4, 5, 6, 7, 0), 'K')
        self.assertEqual(tiledriver.at8_3(state),
                         [PS((8, 1, 2, 3, 4, 5, 6, 0, 7), 'KL')])

    def test_at8_3_3(self):
        state = PS((8, 1, 2, 3, 4, 5, 6, 7, 0), 'H')
        self.assertEqual(tiledriver.at8_3(state),
                         [PS((8, 1, 2, 3, 4, 0, 6, 7, 5), 'HJ')])

    def test_at8_3_4(self):
        state = PS((8, 1, 2, 3, 4, 5, 6, 7, 0), 'JJLLKHHK')
        self.assertEqual(tiledriver.at8_3(state),
                         [PS((8, 1, 2, 3, 4, 5, 6, 0, 7), 'JJLLKHHKL')])

    def test_at8_3_5(self):
        state = PS((8, 1, 2, 3, 4, 5, 6, 7, 0), 'JLKKHH')
        self.assertEqual(tiledriver.at8_3(state),
                         [PS((8, 1, 2, 3, 4, 0, 6, 7, 5), 'JLKKHHJ')])



class TestMergeThatShit(unittest.TestCase):

    def test_mergethatshit_1(self):
        before = [3, 7, 1, 4, 0, 2, 6, 8, 5]
        self.assertEqual(tiledriver.mergethatshit(before, 0),
                         ([0, 1, 2, 3, 4, 5, 6, 7, 8], 14))

    def test_mergethatshit_2(self):
        before = [3, 7, 9, 12, 4, 10, 2, 14, 11, 1, 8, 13, 5, 6, 0]
        self.assertEqual(tiledriver.mergethatshit(before, 0),
                         ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                           11, 12, 13, 14], 57))

    def test_mergethatshit_3(self):
        before = [3, 1, 2, 0]
        self.assertEqual(tiledriver.mergethatshit(before, 0),
                         ([0, 1, 2, 3], 5))

    def test_mergethatshit_4(self):
        before = [3, 7, 1, 4, 2, 6, 8, 5]
        self.assertEqual(tiledriver.mergethatshit(before, 0),
                         ([1, 2, 3, 4, 5, 6, 7, 8], 10))

    def test_mergethatshit_5(self):
        before = [3, 1, 2, 6, 5, 8, 7, 4, 0]
        self.assertEqual(tiledriver.mergethatshit(before, 0),
                         ([0, 1, 2, 3, 4, 5, 6, 7, 8], 16))

    def test_mergethatshit_6(self):
        before = [3, 7, 4, 1, 0, 2, 6, 8, 5]
        self.assertEqual(tiledriver.mergethatshit(before, 0),
                         ([0, 1, 2, 3, 4, 5, 6, 7, 8], 15))




class TestIsSolvable(unittest.TestCase):

    def test_is_solvable_1(self):
        self.assertTrue(tiledriver.is_solvable((3, 2, 1, 0)))

    def test_is_solvable_2(self):
        self.assertFalse(tiledriver.is_solvable((0, 2, 1, 3)))

    def test_is_solvable_3(self):
        self.assertTrue(tiledriver.is_solvable((3, 7, 1, 4, 0, 2, 6, 8, 5)))

    def test_is_solvable_4(self):
        self.assertFalse(tiledriver.is_solvable((3, 7, 4, 1, 0, 2, 6, 8, 5)))

    def test_is_solvable_5(self):
        self.assertTrue(tiledriver.is_solvable((3, 1, 2, 6, 5, 8, 7, 4, 0)))





class TestSolvePuzzle(unittest.TestCase):

    def test_solve_puzzle_1(self):
        self.assertEqual(tiledriver.solve_puzzle((3, 2, 1, 0)), "JLKHJL")

    def test_solve_puzzle_2(self):
        self.assertEqual(tiledriver.solve_puzzle((3, 0, 1, 2)), "LKHJL")

    def test_solve_puzzle_3(self):
        self.assertEqual(tiledriver.solve_puzzle((1, 0, 2, 3, 4, 5, 6, 7, 8)),
                                                 "L")

    def test_solve_puzzle_4(self):
        self.assertEqual(tiledriver.solve_puzzle((3, 7, 1, 4, 0, 2, 6, 8, 5)),
                                                 "JHKKLJLJ")

    def test_solve_puzzle_5(self):
        self.assertEqual(tiledriver.solve_puzzle((3, 1, 2, 6, 5, 8, 7, 4, 0)),
                                                 "JLKLJJ")


if __name__ == "__main__":
    unittest.main()

