# -*- coding: utf-8 -*-

import unittest

import deutschlandfunk

class TestDeutschlandfunk(unittest.TestCase):
	def test_get_broadcasts(self):
		self.assertEqual(deutschlandfunk.get_broadcasts(), None)
if __name__ == "__main__":
	unittest.main()

