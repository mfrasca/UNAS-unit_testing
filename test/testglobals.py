# -*- coding: utf-8 -*-
#
# copyright by its authors
#
# This file is part of the didactic code used at the UNAS
#
# UNAS didactic code is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# UNAS didactic code is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License along
# with UNAS didactic code. If not, see <http://www.gnu.org/licenses/>.


# este archivo contiene las pruebas unitarias para las funciones globales
# definidas en los módulos.


import unittest


class GlobalTests(unittest.TestCase):

    def test_mergevalues_equal(self):
        'if the values are equal, return it'
        1/0

    def test_mergevalues_conflict(self):
        'if they conflict, return both'
        1/0

    def test_mergevalues_one_empty(self):
        'if one is empty, return the non empty one'
        1/0

    def test_mergevalues_both_empty(self):
        'if both are empty, return the empty string'
        1/0

    def test_mergevalues_none_as_empty_string(self):
        'the function does not distinguish between None and the empty string'
        1/0
