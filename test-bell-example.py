from unittest import TestCase
from bellexample import bell_state

class TestBellState(TestCase):
    def test_is_00_observed_prob_50_percent(self):
        self.assertTrue(bell_state()['00'] >= 450)

    def test_is_11_observed_prob_50_percent(self):
        self.assertTrue(bell_state()['11'] >= 450)
    
    def test_has_only_2_measurements(self):
        self.assertTrue(len(bell_state()) == 2)