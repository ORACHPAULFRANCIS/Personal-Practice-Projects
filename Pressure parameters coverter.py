def convert_pressure():
    """Pressure Units and their equivalents in pascals
| Unit                              | Symbol | Equivalent in Pascals (Pa)                                    |
| --------------------------------- | ------ | ------------------------------------------------------------- |
| **Pascal**                        | Pa     | 1 Pa                                                          |
| **Kilopascal**                    | kPa    | 1 kPa = 1,000 Pa                                              |
| **Megapascal**                    | MPa    | 1 MPa = 1,000,000 Pa                                          |
| **Bar**                           | bar    | 1 bar = 100,000 Pa                                            |
| **Millibar**                      | mbar   | 1 mbar = 100 Pa                                               |
| **kgf/cm²** (Kilogram-force/cm²)  | kg/cm² | 1 kg/cm² ≈ 98,066.5 Pa                                        |
| **mmHg** (Millimeters of mercury) | mmHg   | 1 mmHg ≈ 133.322 Pa                                           |
| **cmH₂O** (Centimeters of water)  | cmH₂O  | 1 cmH₂O ≈ 98.0665 Pa                                          |
| **mmH₂O** (Millimeters of water)  | mmH₂O  | 1 mmH₂O ≈ 9.80665 Pa                                          |
| **psi** (Pounds/square inch)      | psi    | 1 psi ≈ 6,894.76 Pa                                           |
| **psf** (Pounds/square foot)      | psf    | 1 psf ≈ 47.8803 Pa                                            |
| **inHg** (Inches of mercury)      | inHg   | 1 inHg ≈ 3,386.39 Pa                                          |
| **inH₂O** (Inches of water)       | inH₂O  | 1 inH₂O ≈ 249.0889 Pa                                         |
| **Atmosphere (standard)**         | atm    | 1 atm = 101,325 Pa                                            |
| **Atmosphere (technical)**        | at     | 1 at = 98,066.5 Pa                                            |
| **Torr**                          | Torr   | 1 Torr ≈ 133.322 Pa                                           |
| **Gauge pressure (psig)**         | psig   | psig = psi above atmospheric (add 101,325 Pa to get absolute) |
| **Absolute pressure (psia)**      | psia   | psia = psi + 101,325 Pa                                       |
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

        print(f"\n✅ {value} {from_unit} = {converted_value:.4f} {to_unit}")

    except ValueError:
        print("❌ Invalid input. Please enter numeric values.")

