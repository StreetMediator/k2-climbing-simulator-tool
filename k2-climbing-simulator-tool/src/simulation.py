import random
from src.player import Player

class K2Simulation:
    BASE_CAMP = 5000
    SUMMIT = 8611
    DEATH_ZONE = 8000

    def __init__(self, player: Player):
        self.player = player
        self.day = 0
        self.running = True

    def advance_day(self) -> str:
        if not self.running:
            return "Simulation ended."
        self.day += 1
        climb = random.uniform(50, 300)
        hazard = random.random()
        events = []

        if hazard < 0.15:
            self.player.stamina -= 20
            events.append("Avalanche! Stamina -20.")
        elif hazard < 0.3:
            self.player.stamina -= 10
            events.append("Crevass fall! Stamina -10.")

        success = self.player.climb(climb)
        if success:
            events.append(f"Climbed {climb:.0f}m.")
        else:
            events.append(f"Too exhausted to climb {climb:.0f}m. Resting.")
            self.player.rest(30)
            events.append("Rested 30 min.")

        if self.player.altitude >= self.SUMMIT:
            self.running = False
            events.append("SUMMIT REACHED! K2 conquered!")
        elif self.player.altitude >= self.DEATH_ZONE and self.player.stamina < 20:
            self.running = False
            events.append("Death zone + exhaustion. Expedition failed.")

        return f"Day {self.day}: {self.player.summary()} | {' | '.join(events)}"