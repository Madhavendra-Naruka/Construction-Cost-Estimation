def calculate_routine_maintenance_cost(area, maintenance_type):
    # Base annual cost per square foot for different maintenance types (hypothetical)
    maintenance_costs = {
        'basic': 2 * 12,  # Annualize the monthly cost
        'standard': 4 * 12,
        'premium': 6 * 12
    }

    # Calculate routine maintenance cost
    total_cost = area * maintenance_costs[maintenance_type]

    return total_cost


def calculate_major_repairs_cost(area, repair_frequency):
    # Base annual cost per square foot for different frequencies of major repairs (hypothetical)
    repair_costs = {
        'low': 3 * 12,  # Annualize the monthly cost
        'medium': 6 * 12,
        'high': 9 * 12
    }

    # Calculate major repairs cost
    total_cost = area * repair_costs[repair_frequency]

    return total_cost


def calculate_utility_costs(area, utility_rate):
    # Base annual cost per square foot for utilities (hypothetical)
    utility_costs_per_sqft = 1.5 * 12  # Annualize the monthly cost

    # Calculate utility costs
    total_cost = area * utility_costs_per_sqft * utility_rate

    return total_cost


def calculate_staffing_costs(staff_count, staff_salary):
    # Calculate staffing costs (already annual)
    total_cost = staff_count * staff_salary

    return total_cost


def calculate_equipment_supplies_cost(area, equipment_rate):
    # Base annual cost per square foot for equipment and supplies (hypothetical)
    equipment_costs_per_sqft = 0.5 * 12  # Annualize the monthly cost

    # Calculate equipment and supplies cost
    total_cost = area * equipment_costs_per_sqft * equipment_rate

    return total_cost


def calculate_maintenance_operation_cost(area, maintenance_type, repair_frequency, utility_rate, staff_count,
                                         staff_salary, equipment_rate):
    # Calculate costs for each component
    routine_maintenance_cost = calculate_routine_maintenance_cost(area, maintenance_type)
    major_repairs_cost = calculate_major_repairs_cost(area, repair_frequency)
    utility_costs = calculate_utility_costs(area, utility_rate)
    staffing_costs = calculate_staffing_costs(staff_count, staff_salary)
    equipment_supplies_cost = calculate_equipment_supplies_cost(area, equipment_rate)

    # Total maintenance and operation cost
    total_cost = (routine_maintenance_cost + major_repairs_cost + utility_costs +
                  staffing_costs + equipment_supplies_cost)

    return total_cost


def maintenance_operation():
    print("Welcome to the Detailed Maintenance and Operation Cost Estimator (Annual Basis)\n")

    # Get user input for project size (in square feet)
    area = float(input("Enter the project size in square feet: "))

    # Get user input for maintenance type (basic/standard/premium)
    maintenance_type = input("Enter the maintenance type (basic/standard/premium): ").lower()
    if maintenance_type not in ['basic', 'standard', 'premium']:
        print("Invalid maintenance type. Please enter 'basic', 'standard', or 'premium'.")
        return

    # Get user input for repair frequency (low/medium/high)
    repair_frequency = input("Enter the repair frequency (low/medium/high): ").lower()
    if repair_frequency not in ['low', 'medium', 'high']:
        print("Invalid repair frequency. Please enter 'low', 'medium', or 'high'.")
        return

    # Get user input for utility rate multiplier
    utility_rate = float(input("Enter the utility rate multiplier (e.g., 1 for standard, 1.2 for 20% higher): "))

    # Get user input for the number of staff required
    staff_count = int(input("Enter the number of maintenance and operation staff required: "))

    # Get user input for the average staff salary (annual)
    staff_salary = float(input("Enter the average staff salary (annual) in INR: "))

    # Get user input for equipment and supplies rate multiplier
    equipment_rate = float(
        input("Enter the equipment and supplies rate multiplier (e.g., 1 for standard, 1.5 for 50% higher): "))

    # Calculate the maintenance and operation cost
    total_cost = calculate_maintenance_operation_cost(area, maintenance_type, repair_frequency, utility_rate,
                                                      staff_count, staff_salary, equipment_rate)

    # Display the estimated cost
    print(f"\nThe estimated annual cost for the maintenance and operation phase is: INR {total_cost:,.2f}")
    return total_cost

if __name__ == "__main__":
    maintenance_operation()
