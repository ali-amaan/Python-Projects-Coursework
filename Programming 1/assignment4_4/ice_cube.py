# Implement the function ice_cube_heating here
def ice_cube_heating(energy, mass, start_temp, end_temp):
    if start_temp < end_temp <= 0:
        Q = 2.09 * mass * (end_temp - start_temp)
        if Q < energy:
            return energy - Q, end_temp
        if Q >= energy:
            return 0.0, ((energy / (2.09 * mass)) + start_temp)
    if start_temp >= 0.0 and end_temp <= 100:
        Q = 4.1819 * mass * (end_temp - start_temp)
        if Q < energy:
            return energy - Q, end_temp
        if Q >= energy:
            return 0.0, ((energy / (4.1819 * mass)) + start_temp)


# Implement the function ice_cube_melting here
def ice_cube_melting(energy, mass):
    Q = 333 * mass
    if energy >= Q:
        return energy - Q, True
    if energy < Q:
        return 0.0, False


# Implement the function ice_cube_vaporization here
def ice_cube_vaporization(energy, mass):
    Q = 2260 * mass
    if energy >= Q:
        return energy - Q, True
    if energy < Q:
        return 0.0, False


def print_heating_result(energy_total, mass, temp_init, temp_end, melted, vaporized):
    print("With {:.2f} kJ, an ice cube weighing {:.2f} kg heats from {:.2f} °C to {:.2f} °C."
          .format(energy_total, mass, temp_init, temp_end))
    if not melted and not vaporized:
        print("The ice cube stays solid.")
    elif melted and not vaporized:
        print("The ice cube has melted into fluid water.")
    else:
        print("The ice cube has vaporized and is now water vapor.")


def main():
    print("Welcome to the ice cube simulator! I will tell you stats about heating your ice cube.")
    mass = float(input("What is the mass of the ice cube (in kg)?\n"))
    while mass <= 0.0:
        print("Mass cannot be zero or negative!")
        mass = float(input("What is the mass of the ice cube?\n"))
    temp_init = float(input("What is the initial temperature of the ice cube (in °C)?\n"))
    while temp_init < -273.15 or temp_init > 0.0:
        print("The ice cube's temperature can't be under the absolute zero or above 0 degrees!")
        temp_init = float(input("What is the initial temperature of the ice cube (in °C)?\n"))
    energy_total = float(input("What is the total energy used for heating the ice cube (in kJ)?\n"))
    while energy_total < 0.0:
        print("Energy cannot be negative!")
        energy_total = float(input("What is the total energy used for heating the ice cube (in kJ)?\n"))

    melted = False
    vaporized = False
    energy_remaining, end_temp = ice_cube_heating(energy_total, mass, temp_init, 0.0)
    if energy_remaining != 0.0:
        energy_remaining, melted = ice_cube_melting(energy_remaining, mass)
        if energy_remaining != 0.0:
            energy_remaining, end_temp = ice_cube_heating(energy_remaining, mass, 0.0, 100.0)
            if energy_remaining != 0.0:
                energy_remaining, vaporized = ice_cube_vaporization(energy_remaining, mass)

    print_heating_result(energy_total, mass, temp_init, end_temp, melted, vaporized)

main()

