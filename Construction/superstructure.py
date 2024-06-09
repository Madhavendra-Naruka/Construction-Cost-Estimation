def calculate_superstructure_cost(area, floors, superstructure_type, material_quality, labor_cost_per_sqft,
                                  additional_features):
    # Base cost per square foot for different superstructure types (hypothetical)
    superstructure_costs = {
        'steel_frame': 150,
        'concrete_frame': 120,
        'wood_frame': 100
    }

    # Material quality cost factor (hypothetical)
    material_quality_factors = {
        'low': 1,
        'medium': 1.2,
        'high': 1.5
    }

    # Calculate base cost
    base_cost = area * superstructure_costs[superstructure_type] * floors

    # Calculate material quality cost
    material_quality_cost = base_cost * material_quality_factors[material_quality]

    # Calculate labor cost
    labor_cost = area * labor_cost_per_sqft * floors

    # Calculate additional features cost
    additional_features_cost = sum(additional_features.values())

    # Total superstructure cost
    total_cost = material_quality_cost + labor_cost + additional_features_cost

    return total_cost


def superstructure():
    print("Welcome to the Detailed Superstructure Cost Estimator\n")

    # Get user input for project size (in square feet)
    area = float(input("Enter the project size in square feet: "))

    # Get user input for number of floors
    floors = int(input("Enter the number of floors: "))

    # Get user input for superstructure type (steel_frame/concrete_frame/wood_frame)
    superstructure_type = input("Enter the superstructure type (steel_frame/concrete_frame/wood_frame): ").lower()
    if superstructure_type not in ['steel_frame', 'concrete_frame', 'wood_frame']:
        print("Invalid superstructure type. Please enter 'steel_frame', 'concrete_frame', or 'wood_frame'.")
        return

    # Get user input for material quality (low/medium/high)
    material_quality = input("Enter the material quality (low/medium/high): ").lower()
    if material_quality not in ['low', 'medium', 'high']:
        print("Invalid material quality. Please enter 'low', 'medium', or 'high'.")
        return

    # Get user input for labor cost per square foot
    labor_cost_per_sqft = float(input("Enter the labor cost per square foot: "))

    # Get user input for additional features
    additional_features = {}
    while True:
        feature = input("Enter an additional feature (or 'done' to finish): ").lower()
        if feature == 'done':
            break
        cost = float(input(f"Enter the cost for {feature}: "))
        additional_features[feature] = cost

    # Calculate the superstructure cost
    total_cost = calculate_superstructure_cost(area, floors, superstructure_type, material_quality, labor_cost_per_sqft,
                                               additional_features)

    # Display the estimated cost
    print(f"\nThe estimated cost for the superstructure is: INR {total_cost:,.2f}")


if __name__ == "__main__":
    superstructure()
