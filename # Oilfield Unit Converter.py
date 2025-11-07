# Oilfield Unit Converter
"""This script provides a simple command-line interface for
converting various oilfield units.
I want to work with like minded individuals
to perfect this program even though it is merely for
praticing and mastering the skills of programming
Feel free to share ideas with me, I want to
have a converter that can convert several
parameters and not just in one direction but both ways
I have initially started with just a few parameters only as you'll see below"""
# Function to convert pressure

def convert_pressure():
    """
    Convert pressure values between various oilfield units.

    This function allows the user to input a pressure value in one unit
    and convert it to another unit, using standard conversion factors
    relative to the Pascal (Pa). It supports units commonly used in
    oilfield engineering, including psi, bar, mmHg, atm, and more.

    Supported Units and their Equivalent in Pascals:
    ------------------------------------------------
    | Unit                              | Symbol   | Equivalent in Pascals (Pa)     |
    |-----------------------------------|----------|--------------------------------|
    | Pascal                            | Pa       | 1 Pa                           |
    | Kilopascal                        | kPa      | 1 kPa = 1,000 Pa               |
    | Megapascal                        | MPa      | 1 MPa = 1,000,000 Pa           |
    | Bar                               | bar      | 1 bar = 100,000 Pa             |
    | Millibar                          | mbar     | 1 mbar = 100 Pa                |
    | Kilogram-force per cm²           | kg/cm²   | 1 kg/cm² ≈ 98,066.5 Pa         |
    | Millimeters of mercury            | mmHg     | 1 mmHg ≈ 133.322 Pa            |
    | Centimeters of water              | cmH₂O    | 1 cmH₂O ≈ 98.0665 Pa           |
    | Millimeters of water              | mmH₂O    | 1 mmH₂O ≈ 9.80665 Pa           |
    | Pounds per square inch            | psi      | 1 psi ≈ 6,894.76 Pa            |
    | Pounds per square foot            | psf      | 1 psf ≈ 47.8803 Pa             |
    | Inches of mercury                 | inHg     | 1 inHg ≈ 3,386.39 Pa           |
    | Inches of water                   | inH₂O    | 1 inH₂O ≈ 249.0889 Pa          |
    | Standard atmosphere               | atm      | 1 atm = 101,325 Pa             |
    | Technical atmosphere              | at       | 1 at = 98,066.5 Pa             |
    | Torr                              | Torr     | 1 Torr ≈ 133.322 Pa            |

    Notes:
        - `psia` (absolute) = `psi` + 101325
        - `psig` (gauge) is `psi` above atmospheric pressure

    Input:
        Prompts the user to:
        - Enter a pressure value (numeric)
        - Enter the unit to convert from (string)
        - Enter the unit to convert to (string)

    Output:
        Displays the converted pressure value or an error if invalid input.

    Example:
        Enter pressure value: 100
        Enter the unit to convert from (e.g., psi): psi
        Enter the unit to convert to (e.g., bar): bar

        ✅ 100 psi = 6.8948 bar

    Raises:
        ValueError: If a non-numeric value is entered for the pressure.

    Author:
        Orach Paul Francis
    """

    # Conversion factors to Pascal
    pressure_units = {
        "pa": 1,
        "kpa": 1000,
        "mpa": 1000000,
        "bar": 100000,
        "mbar": 100,
        "kg/cm2": 98066.5,
        "mmhg": 133.322,
        "cmh2o": 98.0665,
        "mmh2o": 9.80665,
        "psi": 6894.76,
        "psf": 47.8803,
        "inhg": 3386.39,
        "inh2o": 249.0889,
        "atm": 101325,
        "at": 98066.5,
        "torr": 133.322,
    }

    print("Supported units:")
    for unit in pressure_units:
        print(f" - {unit}")

    try:
        value = float(input("Enter pressure value: "))
        from_unit = input("Enter the unit to convert from (e.g., psi): ").lower()
        to_unit = input("Enter the unit to convert to (e.g., bar): ").lower()

        if from_unit not in pressure_units or to_unit not in pressure_units:
            print("❌ Invalid unit entered.")
            return

        # Convert from source unit to Pascal
        value_in_pa = value * pressure_units[from_unit]

        # Convert from Pascal to target unit
        converted_value = value_in_pa / pressure_units[to_unit]

        print(f"\n✅ {value} {from_unit} = {converted_value:.6f} {to_unit}")

    except ValueError:
        print("❌ Invalid input. Please enter numeric values.")


# Function to convert temperature from Fahrenheit to Celsius

def convert_temperature():
    """
    Convert temperature values between various units.

    This function allows users to input a temperature value in one unit and convert it
    to another, using formulas relative to Kelvin. Supported units include Celsius,
    Fahrenheit, Kelvin, Rankine, Delisle, Newton, Réaumur, and Rømer.

    Supported Units:
    ----------------
    | Celsius (c)
    | Fahrenheit (f)
    | Kelvin (k)
    | Rankine (r)
    | Delisle (de)
    | Newton (n)
    | Réaumur (re)
    | Rømer (ro)

    Input:
        Prompts the user to:
        - Enter a temperature value (numeric)
        - Enter the unit to convert from (string)
        - Enter the unit to convert to (string)

    Output:
        Displays the converted temperature value or an error if input is invalid.

    Example:
        Enter temperature value: 100
        Enter the unit to convert from (e.g., c): c
        Enter the unit to convert to (e.g., f): f

        ✅ 100 c = 212.0000 f

    Raises:
        ValueError: If a non-numeric value is entered for the temperature.

    Author:
        Orach Paul Francis
    """

    units = ['c', 'f', 'k', 'r', 'de', 'n', 're', 'ro']

    def to_kelvin(value, unit):
        conversions = {
            'c': lambda x: x + 273.15,
            'f': lambda x: (x - 32) * 5/9 + 273.15,
            'k': lambda x: x,
            'r': lambda x: x * 5/9,
            'de': lambda x: 373.15 - x * 2/3,
            'n': lambda x: x * 100/33 + 273.15,
            're': lambda x: x * 5/4 + 273.15,
            'ro': lambda x: (x - 7.5) * 40/21 + 273.15,
        }
        return conversions[unit](value)

    def from_kelvin(kelvin, unit):
        conversions = {
            'c': lambda x: x - 273.15,
            'f': lambda x: (x - 273.15) * 9/5 + 32,
            'k': lambda x: x,
            'r': lambda x: x * 9/5,
            'de': lambda x: (373.15 - x) * 3/2,
            'n': lambda x: (x - 273.15) * 33/100,
            're': lambda x: (x - 273.15) * 4/5,
            'ro': lambda x: (x - 273.15) * 21/40 + 7.5,
        }
        return conversions[unit](kelvin)

    print("Supported units: c, f, k, r, de, n, re, ro")
    try:
        value = float(input("Enter temperature value: "))
        from_unit = input("Enter the unit to convert from (e.g., c): ").lower()
        to_unit = input("Enter the unit to convert to (e.g., f): ").lower()

        if from_unit not in units or to_unit not in units:
            print("❌ Invalid unit entered.")
            return

        kelvin_value = to_kelvin(value, from_unit)
        result = from_kelvin(kelvin_value, to_unit)

        print(f"\n✅ {value} {from_unit} = {result:.4f} {to_unit}")

    except ValueError:
        print("❌ Invalid input. Please enter a numeric temperature.")


# Function to convert volume from barrels to liters

def convert_volume():
    """
    Convert volume between common oilfield units.

    Supported Units:
    ----------------
    | Liters (l)
    | Milliliters (ml)
    | Barrels (bbl)
    | Cubic meters (m3)
    | Cubic centimeters (cm3)
    | Gallons (US) (gal)
    | Cubic feet (ft3)
    | Cubic inches (in3)

    Base Unit: Liters

    Example:
        1 bbl = 158.987 liters
    """
    volume_units = {
        'l': 1,
        'ml': 0.001,
        'bbl': 158.987,
        'm3': 1000,
        'cm3': 0.001,
        'gal': 3.78541,
        'ft3': 28.3168,
        'in3': 0.0163871
    }

    print("Supported units: l, ml, bbl, m3, cm3, gal, ft3, in3")
    try:
        value = float(input("Enter volume value: "))
        from_unit = input("Convert from (e.g., bbl): ").lower()
        to_unit = input("Convert to (e.g., m3): ").lower()

        if from_unit not in volume_units or to_unit not in volume_units:
            print("❌ Invalid unit entered.")
            return

        # Convert to liters (base)
        liters = value * volume_units[from_unit]
        # Convert to target unit
        result = liters / volume_units[to_unit]

        print(f"\n✅ {value} {from_unit} = {result:.4f} {to_unit}")

    except ValueError:
        print("❌ Please enter a valid number.")


# Function to convert depth

def convert_depth():
    """
    Convert depth between common oilfield units.

    Supported Units:
    ----------------
    | Meters (m)
    | Kilometers (km)
    | Centimeters (cm)
    | Millimeters (mm)
    | Feet (ft)
    | Inches (in)
    | Yards (yd)
    | Miles (mi)

    Base Unit: Meters
    """
    depth_units = {
        'm': 1,
        'km': 1000,
        'cm': 0.01,
        'mm': 0.001,
        'ft': 0.3048,
        'in': 0.0254,
        'yd': 0.9144,
        'mi': 1609.34
    }

    print("Supported units: m, km, cm, mm, ft, in, yd, mi")
    try:
        value = float(input("Enter depth value: "))
        from_unit = input("Convert from (e.g., ft): ").lower()
        to_unit = input("Convert to (e.g., m): ").lower()

        if from_unit not in depth_units or to_unit not in depth_units:
            print("❌ Invalid unit entered.")
            return

        # Convert to meters (base)
        meters = value * depth_units[from_unit]
        # Convert to target
        result = meters / depth_units[to_unit]

        print(f"\n✅ {value} {from_unit} = {result:.4f} {to_unit}")

    except ValueError:
        print("❌ Invalid input. Enter a number.")

# Function to convert density

def convert_density():
    """
    Convert density between oilfield-related units.

    Supported Units:
    ----------------
    | Kilogram per cubic meter (kg/m3)
    | Gram per cubic centimeter (g/cm3)
    | Pound per cubic foot (lb/ft3)
    | Pound per gallon (lb/gal)

    Base Unit: kg/m³
    """
    density_units = {
        'kg/m3': 1,
        'g/cm3': 1000,
        'lb/ft3': 16.0185,
        'lb/gal': 119.826
    }

    print("Supported units: kg/m3, g/cm3, lb/ft3, lb/gal")
    try:
        value = float(input("Enter density value: "))
        from_unit = input("Convert from (e.g., lb/gal): ").lower()
        to_unit = input("Convert to (e.g., g/cm3): ").lower()

        if from_unit not in density_units or to_unit not in density_units:
            print("❌ Invalid unit entered.")
            return

        # Convert to kg/m3
        kg_m3 = value * density_units[from_unit]
        # Convert to target unit
        result = kg_m3 / density_units[to_unit]

        print(f"\n✅ {value} {from_unit} = {result:.4f} {to_unit}")

    except ValueError:
        print("❌ Please enter a valid number.")

# Function to convert flowrate

def convert_flowrate():
    """
    Convert flow rate between oilfield units.

    Supported Units:
    ----------------
    | Liters per second (l/s)
    | Liters per minute (l/min)
    | Cubic meters per hour (m3/h)
    | Barrels per day (bbl/d)
    | Barrels per hour (bbl/h)
    | Gallons per minute (gpm)

    Base Unit: liters/second
    """
    flow_units = {
        'l/s': 1,
        'l/min': 1 / 60,
        'm3/h': 1000 / 3600,
        'bbl/d': 158.987 / 86400,
        'bbl/h': 158.987 / 3600,
        'gpm': 3.78541 / 60
    }

    print("Supported units: l/s, l/min, m3/h, bbl/d, bbl/h, gpm")
    try:
        value = float(input("Enter flow rate value: "))
        from_unit = input("Convert from (e.g., bbl/d): ").lower()
        to_unit = input("Convert to (e.g., gpm): ").lower()

        if from_unit not in flow_units or to_unit not in flow_units:
            print("❌ Invalid unit entered.")
            return

        # Convert to base (l/s)
        liters_per_sec = value * flow_units[from_unit]
        # Convert to target unit
        result = liters_per_sec / flow_units[to_unit]

        print(f"\n✅ {value} {from_unit} = {result:.4f} {to_unit}")

    except ValueError:
        print("❌ Invalid input. Please enter a numeric flow rate.")


# Function to display the menu and handle user input

def show_menu():
    print("\n--- Oilfield Unit Converter ---")
    print("1. Convert Pressure")
    print("2. Convert Temperature")
    print("3. Convert Volume")
    print("4. Convert Depth")
    print("5. Convert Density")
    print("6. Convert Flow Rate")
    print("7. Exit")

# Main function to run the converter

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            convert_pressure()
        elif choice == '2':
            convert_temperature()
        elif choice == '3':
            convert_volume()
        elif choice == '4':
            convert_depth()
        elif choice == '5':
            convert_density()
        elif choice == '6':
            convert_flowrate()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
