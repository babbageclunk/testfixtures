from testfixtures import StringComparison as S, compare
from testfixtures import Comparison as C
from unittest import TestCase

class Tests(TestCase):

    def test_equal_yes(self):
        self.failUnless('on 40220'==S('on \d+'))

    def test_equal_no(self):
        self.failIf('on xxx'==S('on \d+'))

    def test_not_equal_yes(self):
        self.failIf('on 40220'!=S('on \d+'))

    def test_not_equal_no(self):
        self.failUnless('on xxx'!=S('on \d+'))

    def test_comp_in_sequence(self):
        self.failUnless((
            1,2,'on 40220'
            )==(
            1,2,S('on \d+')
            ))

    def test_not_string(self):
        self.failIf(40220==S('on \d+'))
    
    def test_repr(self):
        compare('<S:on \\d+>',
                repr(S('on \d+')))

    def test_str(self):
        compare('<S:on \\d+>',
                str(S('on \d+')))

    def test_sort(self):
        a = S('a')
        b = S('b')
        c = S('c')
        compare(sorted(('d',c,'e',a,'a1',b,)),
                [a,'a1',b,c,'d','e',])

