def main():
    mass_kg = int(input("Enter mass in kilograms: "))
    energy_joules = mass_kg * (3 * 10**8)**2
    print(f"Equivalent energy: {energy_joules} Joules")


if __name__ == "__main__":
    main()
