# DC-DC Converter Simulation
# Buck, Boost and Buck-Boost Converter

class DCDCConverter:

    def __init__(self, input_voltage, duty_cycle):
        self.vin = input_voltage
        self.duty = duty_cycle / 100

    def buck_converter(self):
        # Vout = D × Vin
        return self.duty * self.vin

    def boost_converter(self):
        # Vout = Vin / (1-D)
        return self.vin / (1 - self.duty)

    def buck_boost_converter(self):
        # Vout = -(D × Vin) / (1-D)
        return -(self.duty * self.vin) / (1 - self.duty)

    def display_results(self):
        print("\n====================================")
        print("        DC-DC CONVERTER")
        print("====================================")

        print(f"Input Voltage : {self.vin:.2f} V")
        print(f"Duty Cycle    : {self.duty * 100:.2f}%")

        print("\nOutput Voltages")
        print("------------------------------------")

        print(
            f"Buck Converter       : "
            f"{self.buck_converter():.2f} V"
        )

        print(
            f"Boost Converter      : "
            f"{self.boost_converter():.2f} V"
        )

        print(
            f"Buck-Boost Converter : "
            f"{self.buck_boost_converter():.2f} V"
        )

        print("\nSimulation Status: COMPLETED")


# Main Program

print("===== DC-DC Converter Simulation =====")

vin = float(input("Enter input voltage (V): "))
duty = float(input("Enter duty cycle (%): "))

if vin <= 0:
    print("Invalid input voltage!")

elif duty <= 0 or duty >= 100:
    print("Duty cycle must be between 0% and 100%!")

else:
    converter = DCDCConverter(vin, duty)
    converter.display_results()
