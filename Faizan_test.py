"""Unit test for stringcase
"""
from unittest import TestCase
from os import path
from stringcase import camelcase
import sys
from stringcase import capitalcase
from stringcase import constcase
from unittest import main
from stringcase import alphanumcase
from stringcase import trimcase
from stringcase import titlecase
from stringcase import spinalcase
from stringcase import snakecase
from stringcase import uppercase
from stringcase import sentencecase
from stringcase import pascalcase
from stringcase import pathcase
from stringcase import lowercase
sys.path.append(path.dirname(__file__))
import stringcase

class StringcaseTest(TestCase):
    def camelcase(self):

        eq = self.assertEqual
        eq('fooBar', camelcase('foo_bar'))
        eq('fooBar', camelcase('FooBar'))
        eq('', camelcase(''))
        eq('none', camelcase(None))

    def capitalcase(self):
        

        eq = self.assertEqual

        eq('', capitalcase(''))
        eq('FooBar', capitalcase('fooBar'))

    def constcase(self):
        

        eq = self.assertEqual

        eq('FOO_BAR', constcase('fooBar'))
        eq('FOO_BAR', constcase('foo_bar'))
        eq('FOO_BAR', constcase('foo-bar'))
        eq('FOO_BAR', constcase('foo.bar'))
        eq('_BAR_BAZ', constcase('_bar_baz'))
        eq('_BAR_BAZ', constcase('.bar_baz'))
        eq('', constcase(''))
        eq('NONE', constcase(None))

    def lowercase(self):
        

        eq = self.assertEqual

        eq('none', lowercase(None))
        eq('', lowercase(''))
        eq('foo', lowercase('Foo'))

    def pascalcase(self):
        

        eq = self.assertEqual

        eq('FooBar', pascalcase('foo_bar'))
        eq('', pascalcase(''))
        eq('None', pascalcase(None))

    def pathcase(self):
        

        eq = self.assertEqual

        eq('foo/bar', pathcase('fooBar'))
        eq('foo/bar', pathcase('foo_bar'))
        eq('foo/bar', pathcase('foo-bar'))
        eq('foo/bar', pathcase('foo.bar'))
        eq('/bar/baz', pathcase('_bar_baz'))
        eq('/bar/baz', pathcase('.bar_baz'))
        eq('', pathcase(''))
        eq('none', pathcase(None))

    def sentencecase(self):
        
        eq = self.assertEqual
        eq('Foo bar', sentencecase('fooBar'))
        eq('Foo bar', sentencecase('foo_bar'))
        eq('Foo bar', sentencecase('foo-bar'))
        eq('Foo bar', sentencecase('foo.bar'))
        eq('Bar baz', sentencecase('_bar_baz'))
        eq('Bar baz', sentencecase('.bar_baz'))
        eq('', sentencecase(''))
        eq('None', sentencecase(None))

    def uppercase(self):
        
        eq = self.assertEqual
        eq('NONE', uppercase(None))
        eq('', uppercase(''))
        eq('FOO', uppercase('foo'))

    def snakecase(self):
        
        eq = self.assertEqual
        eq('foo_bar', snakecase('fooBar'))
        eq('foo_bar', snakecase('foo_bar'))
        eq('foo_bar', snakecase('foo-bar'))
        eq('foo_bar', snakecase('foo.bar'))
        eq('_bar_baz', snakecase('_bar_baz'))
        eq('_bar_baz', snakecase('.bar_baz'))
        eq('', snakecase(''))
        eq('none', snakecase(None))

    def spinalcase(self):
        
        eq = self.assertEqual
        eq('foo-bar', spinalcase('fooBar'))
        eq('foo-bar', spinalcase('foo_bar'))
        eq('foo-bar', spinalcase('foo-bar'))
        eq('foo-bar', spinalcase('foo.bar'))
        eq('-bar-baz', spinalcase('_bar_baz'))
        eq('-bar-baz', spinalcase('.bar_baz'))
        eq('', spinalcase(''))
        eq('none', spinalcase(None))

    def titlecase(self):
        
        eq = self.assertEqual
        eq('Foo Bar', titlecase('fooBar'))
        eq('Foo Bar', titlecase('foo_bar'))
        eq('Foo Bar', titlecase('foo-bar'))
        eq('Foo Bar', titlecase('foo.bar'))
        eq(' Bar Baz', titlecase('_bar_baz'))
        eq(' Bar Baz', titlecase('.bar_baz'))
        eq('', titlecase(''))
        eq('None', titlecase(None))

    def trimcase(self):
        

        eq = self.assertEqual

        eq('foo bar baz', trimcase(' foo bar baz '))
        eq('', trimcase(''))

    def alphanumcase(self):
        
        eq = self.assertEqual
        eq('', alphanumcase(''))
     


if __name__ == '__main__':
    
    main()