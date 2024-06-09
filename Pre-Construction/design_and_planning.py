def get_architect_fee(project_type, size):
    # Hypothetical rates for architect fees per square foot
    rates = {
        'residential': 150,
        'commercial': 200,
        'industrial': 250
    }
    return rates[project_type] * size


def get_engineering_fee(size):
    # Hypothetical rates for engineering fees per square foot
    rate_per_sqft = 50  # Assuming a flat rate for simplicity
    return rate_per_sqft * size


def get_planning_permission_cost(location):
    # Hypothetical costs for planning permissions based on location
    costs = {
        'urban': 10000,
        'suburban': 7000,
        'rural': 5000
    }
    return costs[location]


def get_consultant_fee(project_type):
    # Hypothetical consultant fees based on project type
    fees = {
        'residential': 20000,
        'commercial': 30000,
        'industrial': 40000
    }
    return fees[project_type]


def get_miscellaneous_costs():
    # Hypothetical miscellaneous costs
    return 10000  # Flat rate for simplicity


def calculate_design_planning_cost(project_type, size, location):
    # Calculate costs for each component
    architect_fee = get_architect_fee(project_type, size)
    engineering_fee = get_engineering_fee(size)
    planning_permission_cost = get_planning_permission_cost(location)
    consultant_fee = get_consultant_fee(project_type)
    miscellaneous_costs = get_miscellaneous_costs()

    # Total cost
    total_cost = (architect_fee + engineering_fee +
                  planning_permission_cost + consultant_fee +
                  miscellaneous_costs)

    return total_cost


def design_and_planning():
    print("Welcome to the Design and Planning Cost Estimator\n")

    # Get user input for project type
    project_type = input("Enter the project type (residential/commercial/industrial): ").lower()
    if project_type not in ['residential', 'commercial', 'industrial']:
        print("Invalid project type. Please enter 'residential', 'commercial', or 'industrial'.")
        return

    # Get user input for project size (in square feet)
    size = float(input("Enter the project size in square feet: "))

    # Get user input for project location (urban/suburban/rural)
    location = input("Enter the project location (urban/suburban/rural): ").lower()
    if location not in ['urban', 'suburban', 'rural']:
        print("Invalid location. Please enter 'urban', 'suburban', or 'rural'.")
        return

    # Calculate the design and planning cost
    total_cost = calculate_design_planning_cost(project_type, size, location)

    # Display the estimated cost
    print(f"\nThe estimated cost for design and planning is: INR {total_cost:,.2f}")


if __name__ == "__main__":
    design_and_planning()
