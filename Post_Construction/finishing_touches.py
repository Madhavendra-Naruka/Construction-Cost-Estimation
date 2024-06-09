def calculate_painting_cost(area, paint_type):
    # Base cost per square foot for different types of paint (hypothetical)
    paint_costs = {
        'basic': 10,
        'standard': 20,
        'premium': 30
    }

    # Calculate painting cost
    total_cost = area * paint_costs[paint_type]

    return total_cost


def calculate_flooring_cost(area, flooring_type):
    # Base cost per square foot for different flooring finishes (hypothetical)
    flooring_costs = {
        'tile': 50,
        'wood': 100,
        'carpet': 75,
        'marble': 150
    }

    # Calculate flooring cost
    total_cost = area * flooring_costs[flooring_type]

    return total_cost


def calculate_fixtures_cost(fixtures_count, fixtures_type):
    # Base cost per fixture for different fixture types (hypothetical)
    fixtures_costs = {
        'basic': 500,
        'standard': 1000,
        'premium': 2000
    }

    # Calculate fixtures cost
    total_cost = fixtures_count * fixtures_costs[fixtures_type]

    return total_cost


def calculate_cabinetry_cost(cabinet_area, cabinetry_type):
    # Base cost per square foot for different cabinetry types (hypothetical)
    cabinetry_costs = {
        'basic': 200,
        'standard': 400,
        'premium': 600
    }

    # Calculate cabinetry cost
    total_cost = cabinet_area * cabinetry_costs[cabinetry_type]

    return total_cost


def calculate_decor_cost(decor_items, decor_type):
    # Base cost per item for different decor types (hypothetical)
    decor_costs = {
        'basic': 100,
        'standard': 200,
        'premium': 300
    }

    # Calculate decor cost
    total_cost = decor_items * decor_costs[decor_type]

    return total_cost


def calculate_final_cleanup_cost(area):
    # Base cost per square foot for final clean-up (hypothetical)
    cleanup_cost_per_sqft = 5

    # Calculate final clean-up cost
    total_cost = area * cleanup_cost_per_sqft

    return total_cost


def calculate_finishing_touches_cost(area, paint_type, flooring_type, fixtures_count, fixtures_type, cabinet_area,
                                     cabinetry_type, decor_items, decor_type):
    # Calculate costs for each component
    painting_cost = calculate_painting_cost(area, paint_type)
    flooring_cost = calculate_flooring_cost(area, flooring_type)
    fixtures_cost = calculate_fixtures_cost(fixtures_count, fixtures_type)
    cabinetry_cost = calculate_cabinetry_cost(cabinet_area, cabinetry_type)
    decor_cost = calculate_decor_cost(decor_items, decor_type)
    final_cleanup_cost = calculate_final_cleanup_cost(area)

    # Total finishing touches cost
    total_cost = (painting_cost + flooring_cost + fixtures_cost + cabinetry_cost + decor_cost + final_cleanup_cost)

    return total_cost


def finishing_touches():
    print("Welcome to the Detailed Finishing Touches Cost Estimator\n")

    # Get user input for project size (in square feet)
    area = float(input("Enter the project size in square feet: "))

    # Get user input for paint type (basic/standard/premium)
    paint_type = input("Enter the paint type (basic/standard/premium): ").lower()
    if paint_type not in ['basic', 'standard', 'premium']:
        print("Invalid paint type. Please enter 'basic', 'standard', or 'premium'.")
        return

    # Get user input for flooring type (tile/wood/carpet/marble)
    flooring_type = input("Enter the flooring type (tile/wood/carpet/marble): ").lower()
    if flooring_type not in ['tile', 'wood', 'carpet', 'marble']:
        print("Invalid flooring type. Please enter 'tile', 'wood', 'carpet', or 'marble'.")
        return

    # Get user input for number of fixtures
    fixtures_count = int(input("Enter the number of fixtures: "))

    # Get user input for fixtures type (basic/standard/premium)
    fixtures_type = input("Enter the fixtures type (basic/standard/premium): ").lower()
    if fixtures_type not in ['basic', 'standard', 'premium']:
        print("Invalid fixtures type. Please enter 'basic', 'standard', or 'premium'.")
        return

    # Get user input for cabinetry area (in square feet)
    cabinet_area = float(input("Enter the cabinetry area in square feet: "))

    # Get user input for cabinetry type (basic/standard/premium)
    cabinetry_type = input("Enter the cabinetry type (basic/standard/premium): ").lower()
    if cabinetry_type not in ['basic', 'standard', 'premium']:
        print("Invalid cabinetry type. Please enter 'basic', 'standard', or 'premium'.")
        return

    # Get user input for number of decor items
    decor_items = int(input("Enter the number of decor items: "))

    # Get user input for decor type (basic/standard/premium)
    decor_type = input("Enter the decor type (basic/standard/premium): ").lower()
    if decor_type not in ['basic', 'standard', 'premium']:
        print("Invalid decor type. Please enter 'basic', 'standard', or 'premium'.")
        return

    # Calculate the finishing touches cost
    total_cost = calculate_finishing_touches_cost(area, paint_type, flooring_type, fixtures_count, fixtures_type,
                                                  cabinet_area, cabinetry_type, decor_items, decor_type)

    # Display the estimated cost
    print(f"\nThe estimated cost for the finishing touches is: INR {total_cost:,.2f}")
    return total_cost

if __name__ == "__main__":
    finishing_touches()
