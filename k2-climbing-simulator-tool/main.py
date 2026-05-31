import sys
from src.player import Player
from src.simulation import K2Simulation

def main():
    print("=== K2 Climbing Simulator Tool ===")
    name = input("Enter climber name: ").strip() or "Climber"
    player = Player(name=name)
    player.add_gear("Ice axe")
    player.add_gear("Oxygen tank")
    player.add_gear("Rope")

    sim = K2Simulation(player)
    print(f"\nStarting from Base Camp ({K2Simulation.BASE_CAMP}m)...\n")

    while sim.running:
        input("Press Enter to advance a day...")
        print(sim.advance_day())
        print()

    print("Simulation complete.")
    print(f"Final altitude: {player.altitude:.1f}m")
    print(f"Final stamina: {player.stamina:.1f}%")

if __name__ == "__main__":
    main()