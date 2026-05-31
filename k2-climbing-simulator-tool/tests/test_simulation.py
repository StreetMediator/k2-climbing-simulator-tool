import unittest
from src.player import Player
from src.simulation import K2Simulation

class TestK2Simulation(unittest.TestCase):
    def test_initial_state(self):
        p = Player("Test")
        sim = K2Simulation(p)
        self.assertEqual(sim.day, 0)
        self.assertTrue(sim.running)
        self.assertEqual(p.altitude, 0.0)

    def test_advance_day_increases_altitude(self):
        p = Player("Test")
        sim = K2Simulation(p)
        sim.advance_day()
        self.assertGreater(sim.day, 0)
        self.assertGreaterEqual(p.altitude, 0.0)

    def test_summit_reached(self):
        p = Player("Summiter")
        p.altitude = 8600
        p.stamina = 100
        sim = K2Simulation(p)
        sim.advance_day()
        if p.altitude >= K2Simulation.SUMMIT:
            self.assertFalse(sim.running)

    def test_player_summary(self):
        p = Player("Alice")
        p.add_gear("Rope")
        summary = p.summary()
        self.assertIn("Alice", summary)
        self.assertIn("Rope", summary)

if __name__ == "__main__":
    unittest.main()