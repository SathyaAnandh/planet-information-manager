"""
Planet Information Manager
Developed by Sathya Anandharaj

A console-based application for managing
planetary information in the Solar System.
"""

class Planet:
    def __init__(self, name, diameter, moons, gravity):
        self.name = name
        self.diameter = diameter
        self.moons = moons
        self.gravity = gravity

    def display(self):
        print("\n----------------------------")
        print(f"Planet Name : {self.name}")
        print(f"Diameter    : {self.diameter} km")
        print(f"Moons       : {self.moons}")
        print(f"Gravity     : {self.gravity} m/s²")
        print("----------------------------")


class PlanetManager:
    def __init__(self):
        self.planets = {
            "Mercury": Planet("Mercury", 4879, 0, 3.7),
            "Venus": Planet("Venus", 12104, 0, 8.87),
            "Earth": Planet("Earth", 12742, 1, 9.81),
            "Mars": Planet("Mars", 6779, 2, 3.71),
            "Jupiter": Planet("Jupiter", 139820, 95, 24.79),
            "Saturn": Planet("Saturn", 116460, 146, 10.44),
            "Uranus": Planet("Uranus", 50724, 27, 8.69),
            "Neptune": Planet("Neptune", 49244, 14, 11.15)
        }

    def view_all_planets(self):
        if not self.planets:
            print("\nNo planets available.")
            return

        print("\n=== PLANET LIST ===")
        for planet in self.planets.values():
            planet.display()

    def search_planet(self):
        name = input("\nEnter planet name: ").title()

        if name in self.planets:
            self.planets[name].display()
        else:
            print("Planet not found.")

    def add_planet(self):
        name = input("\nPlanet Name: ").title()

        if name in self.planets:
            print("Planet already exists.")
            return

        try:
            diameter = float(input("Diameter (km): "))
            moons = int(input("Number of moons: "))
            gravity = float(input("Gravity (m/s²): "))

            self.planets[name] = Planet(
                name,
                diameter,
                moons,
                gravity
            )

            print(f"{name} added successfully.")

        except ValueError:
            print("Invalid input.")

    def update_planet(self):
        name = input("\nEnter planet name to update: ").title()

        if name not in self.planets:
            print("Planet not found.")
            return

        try:
            diameter = float(input("New Diameter (km): "))
            moons = int(input("New Number of Moons: "))
            gravity = float(input("New Gravity (m/s²): "))

            self.planets[name] = Planet(
                name,
                diameter,
                moons,
                gravity
            )

            print("Planet updated successfully.")

        except ValueError:
            print("Invalid input.")

    def delete_planet(self):
        name = input("\nEnter planet name to delete: ").title()

        if name in self.planets:
            del self.planets[name]
            print("Planet deleted successfully.")
        else:
            print("Planet not found.")

    def menu(self):
        while True:
            print("\n================================")
            print("      PLANET INFORMATION MANAGER")
            print("================================")
            print("1. View All Planets")
            print("2. Search Planet")
            print("3. Add Planet")
            print("4. Update Planet")
            print("5. Delete Planet")
            print("6. Exit")

            choice = input("\nEnter your choice: ")

            if choice == "1":
                self.view_all_planets()

            elif choice == "2":
                self.search_planet()

            elif choice == "3":
                self.add_planet()

            elif choice == "4":
                self.update_planet()

            elif choice == "5":
                self.delete_planet()

            elif choice == "6":
                print("\nThank you for using Planet Information Manager.")
                break

            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    manager = PlanetManager()
    manager.menu()