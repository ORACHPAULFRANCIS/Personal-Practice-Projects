def convert_pressure():
    pressure_units = {
        "pa": 1,
        "kpa": 1_000,
        "mpa": 1_000_000,
        "bar": 100_000,
        "mbar": 100,
        "kg/cm2": 98_066.5,
        "mmhg": 133.322,
        "cmh2o": 98.0665,
        "mmh2o": 9.80665,
        "psi": 6_894.76,
        "psf": 47.8803,
        "inhg": 3_386.39,
        "inh2o": 249.0889,
        "atm": 101_325,
        "at": 98_066.5,
        "torr": 133.322,
    }

    print("\n🔁 Pressure Unit Conversion")
    print("Supported units:")
    for unit in pressure_units:
        print(f" - {unit}")

    try:
        value = float(input("\nEnter pressure value: "))
        from_unit = input("Enter the unit to convert from (e.g., psi): ").lower()
        to_unit = input("Enter the unit to convert to (e.g., bar): ").lower()

        if from_unit not in pressure_units or to_unit not in pressure_units:
            print("❌ Invalid unit entered. Please try again.")
            return

        value_in_pa = value * pressure_units[from_unit]
        converted_value = value_in_pa / pressure_units[to_unit]

        print(f"\n✅ {value} {from_unit} = {converted_value:.4f} {to_unit}")

    except ValueError:
        print("❌ Invalid input. Please enter numeric values.")


def main_menu():
    while True:
        print("\n==============================")
        print("🛢️  OILFIELD UNIT CONVERTER")
        print("==============================")
        print("Select the parameter to convert:")
        print("1. Pressure")
        # Future options can go here:
        # print("2. Temperature")
        # print("3. Flow Rate")
        # print("4. Volume")
        print("0. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            convert_pressure()
        elif choice == '0':
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select a valid option.")


# Run the converter menu
if __name__ == "__main__":
    main_menu()
