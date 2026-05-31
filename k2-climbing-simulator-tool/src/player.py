import random
from dataclasses import dataclass, field
from typing import List

@dataclass
class Player:
    name: str
    stamina: float = 100.0
    altitude: float = 0.0
    gear: List[str] = field(default_factory=list)

    def rest(self, minutes: int = 10) -> None:
        recovery = minutes * 0.5
        self.stamina = min(100.0, self.stamina + recovery)

    def climb(self, meters: float) -> bool:
        cost = meters * 1.2
        if self.stamina >= cost:
            self.stamina -= cost
            self.altitude += meters
            return True
        return False

    def add_gear(self, item: str) -> None:
        if item not in self.gear:
            self.gear.append(item)

    def summary(self) -> str:
        return (f"Player: {self.name} | Altitude: {self.altitude:.1f}m "
                f"| Stamina: {self.stamina:.1f}% | Gear: {', '.join(self.gear) or 'none'}")