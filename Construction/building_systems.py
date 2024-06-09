def calculate_hvac_cost(area, hvac_type):
    # Base cost per square foot for different HVAC types (hypothetical)
    hvac_costs = {
        'basic': 50,
        'standard': 100,
        'premium': 150
    }

    # Calculate HVAC cost
    total_cost = area * hvac_costs[hvac_type]

    return total_cost


def calculate_electrical_cost(area, electrical_type):
    # Base cost per square foot for different electrical types (hypothetical)
    electrical_costs = {
        'basic': 40,
        'standard': 80,
        'premium': 120
    }

    # Calculate electrical cost
    total_cost = area * electrical_costs[electrical_type]

    return total_cost


def calculate_plumbing_cost(area, plumbing_type):
    # Base cost per square foot for different plumbing types (hypothetical)
    plumbing_costs = {
        'basic': 60,
        'standard': 120,
        'premium': 180
    }

    # Calculate plumbing cost
    total_cost = area * plumbing_costs[plumbing_type]

    return total_cost


def calculate_fire_protection_cost(area, fire_protection_type):
    # Base cost per square foot for different fire protection types (hypothetical)
    fire_protection_costs = {
        'basic': 30,
        'standard': 60,
        'premium': 90
    }

    # Calculate fire protection cost
    total_cost = area * fire_protection_costs[fire_protection_type]

    return total_cost


def calculate_security_system_cost(area, security_type):
    # Base cost per square foot for different security types (hypothetical)
    security_costs = {
        'basic': 20,
        'standard': 40,
        'premium': 60
    }

    # Calculate security system cost
    total_cost = area * security_costs[security_type]

    return total_cost


def calculate_networking_communication_cost(area, network_type):
    # Base cost per square foot for different networking types (hypothetical)
    network_costs = {
        'basic': 25,
        'standard': 50,
        'premium': 75
    }

    # Calculate networking and communication cost
    total_cost = area * network_costs[network_type]

    return total_cost


def calculate_building_systems_cost(area, hvac_type, electrical_type, plumbing_type, fire_protection_type,
                                    security_type, network_type):
    # Calculate costs for each component
    hvac_cost = calculate_hvac_cost(area, hvac_type)
    electrical_cost = calculate_electrical_cost(area, electrical_type)
    plumbing_cost = calculate_plumbing_cost(area, plumbing_type)
    fire_protection_cost = calculate_fire_protection_cost(area, fire_protection_type)
    security_system_cost = calculate_security_system_cost(area, security_type)
    network_communication_cost = calculate_networking_communication_cost(area, network_type)

    # Total building systems cost
    total_cost = (hvac_cost + electrical_cost + plumbing_cost + fire_protection_cost +
                  security_system_cost + network_communication_cost)

    return total_cost


def building_systems():
    print("Welcome to the Detailed Building Systems Cost Estimator\n")

    # Get user input for project size (in square feet)
    area = float(input("Enter the project size in square feet: "))

    # Get user input for HVAC type (basic/standard/premium)
    hvac_type = input("Enter the HVAC type (basic/standard/premium): ").lower()
    if hvac_type not in ['basic', 'standard', 'premium']:
        print("Invalid HVAC type. Please enter 'basic', 'standard', or 'premium'.")
        return

    # Get user input for electrical type (basic/standard/premium)
    electrical_type = input("Enter the electrical type (basic/standard/premium): ").lower()
    if electrical_type not in ['basic', 'standard', 'premium']:
        print("Invalid electrical type. Please enter 'basic', 'standard', or 'premium'.")
        return

    # Get user input for plumbing type (basic/standard/premium)
    plumbing_type = input("Enter the plumbing type (basic/standard/premium): ").lower()
    if plumbing_type not in ['basic', 'standard', 'premium']:
        print("Invalid plumbing type. Please enter 'basic', 'standard', or 'premium'.")
        return

    # Get user input for fire protection type (basic/standard/premium)
    fire_protection_type = input("Enter the fire protection type (basic/standard/premium): ").lower()
    if fire_protection_type not in ['basic', 'standard', 'premium']:
        print("Invalid fire protection type. Please enter 'basic', 'standard', or 'premium'.")
        return

    # Get user input for security system type (basic/standard/premium)
    security_type = input("Enter the security system type (basic/standard/premium): ").lower()
    if security_type not in ['basic', 'standard', 'premium']:
        print("Invalid security system type. Please enter 'basic', 'standard', or 'premium'.")
        return

    # Get user input for networking and communication system type (basic/standard/premium)
    network_type = input("Enter the networking and communication system type (basic/standard/premium): ").lower()
    if network_type not in ['basic', 'standard', 'premium']:
        print("Invalid networking and communication system type. Please enter 'basic', 'standard', or 'premium'.")
        return

    # Calculate the building systems cost
    total_cost = calculate_building_systems_cost(area, hvac_type, electrical_type, plumbing_type, fire_protection_type,
                                                 security_type, network_type)

    # Display the estimated cost
    print(f"\nThe estimated cost for the building systems is: INR {total_cost:,.2f}")


if __name__ == "__main__":
    building_systems()
