def calculate_exterior_finish_cost(area, finish_type, material_quality):
    # Base cost per square foot for different exterior finishes (hypothetical)
    finish_costs = {
        'brick': 50,
        'stucco': 40,
        'siding': 30
    }

    # Material quality cost factor (hypothetical)
    material_quality_factors = {
        'low': 1,
        'medium': 1.2,
        'high': 1.5
    }

    # Calculate base cost
    base_cost = area * finish_costs[finish_type]

    # Calculate material quality cost
    quality_cost = base_cost * material_quality_factors[material_quality]

    return quality_cost


def calculate_windows_doors_cost(num_windows, num_doors, window_cost, door_cost):
    # Calculate cost for windows and doors
    windows_cost = num_windows * window_cost
    doors_cost = num_doors * door_cost
    total_cost = windows_cost + doors_cost

    return total_cost


def calculate_roofing_cost(area, roofing_type):
    # Base cost per square foot for different roofing types (hypothetical)
    roofing_costs = {
        'shingles': 20,
        'metal': 30,
        'tile': 40
    }

    # Calculate roofing cost
    total_cost = area * roofing_costs[roofing_type]

    return total_cost


def calculate_additional_features_cost(additional_features):
    # Calculate total cost for additional features
    total_cost = sum(additional_features.values())

    return total_cost


def calculate_exterior_work_cost(area, finish_type, material_quality, num_windows, num_doors, window_cost, door_cost,
                                 roofing_type, additional_features):
    # Calculate costs for each component
    exterior_finish_cost = calculate_exterior_finish_cost(area, finish_type, material_quality)
    windows_doors_cost = calculate_windows_doors_cost(num_windows, num_doors, window_cost, door_cost)
    roofing_cost = calculate_roofing_cost(area, roofing_type)
    additional_features_cost = calculate_additional_features_cost(additional_features)

    # Total exterior work cost
    total_cost = exterior_finish_cost + windows_doors_cost + roofing_cost + additional_features_cost

    return total_cost


def exterior_work():
    print("Welcome to the Detailed Exterior Work Cost Estimator\n")

    # Get user input for project size (in square feet)
    area = float(input("Enter the project size in square feet: "))

    # Get user input for exterior finish type (brick/stucco/siding)
    finish_type = input("Enter the exterior finish type (brick/stucco/siding): ").lower()
    if finish_type not in ['brick', 'stucco', 'siding']:
        print("Invalid exterior finish type. Please enter 'brick', 'stucco', or 'siding'.")
        return

    # Get user input for material quality (low/medium/high)
    material_quality = input("Enter the material quality (low/medium/high): ").lower()
    if material_quality not in ['low', 'medium', 'high']:
        print("Invalid material quality. Please enter 'low', 'medium', or 'high'.")
        return

    # Get user input for number of windows and doors
    num_windows = int(input("Enter the number of windows: "))
    num_doors = int(input("Enter the number of doors: "))

    # Get user input for cost per window and door
    window_cost = float(input("Enter the cost per window: "))
    door_cost = float(input("Enter the cost per door: "))

    # Get user input for roofing type (shingles/metal/tile)
    roofing_type = input("Enter the roofing type (shingles/metal/tile): ").lower()
    if roofing_type not in ['shingles', 'metal', 'tile']:
        print("Invalid roofing type. Please enter 'shingles', 'metal', or 'tile'.")
        return

    # Get user input for additional features
    additional_features = {}
    while True:
        feature = input("Enter an additional feature (or 'done' to finish): ").lower()
        if feature == 'done':
            break
        cost = float(input(f"Enter the cost for {feature}: "))
        additional_features[feature] = cost

    # Calculate the exterior work cost
    total_cost = calculate_exterior_work_cost(area, finish_type, material_quality, num_windows, num_doors, window_cost,
                                              door_cost, roofing_type, additional_features)

    # Display the estimated cost
    print(f"\nThe estimated cost for the exterior work is: INR {total_cost:,.2f}")


if __name__ == "__main__":
    exterior_work()
