def calculate_foundation_cost(area, foundation_type, depth, soil_condition, reinforcement, waterproofing):
    # Base cost per square foot for different foundation types (hypothetical)
    foundation_costs = {
        'slab': 50,
        'crawl_space': 70,
        'basement': 100
    }

    # Additional cost per foot of depth (hypothetical)
    depth_cost_factor = 5

    # Additional cost per square foot for different soil conditions (hypothetical)
    soil_cost_factors = {
        'stable': 1,
        'moderate': 1.2,
        'unstable': 1.5
    }

    # Additional cost per square foot for reinforcement (hypothetical)
    reinforcement_cost_factor = 10 if reinforcement else 0

    # Additional cost per square foot for waterproofing (hypothetical)
    waterproofing_cost_factor = 8 if waterproofing else 0

    # Calculate base cost
    base_cost = area * foundation_costs[foundation_type]

    # Calculate depth cost
    depth_cost = area * depth * depth_cost_factor

    # Calculate soil condition cost
    soil_cost = base_cost * soil_cost_factors[soil_condition]

    # Calculate reinforcement cost
    reinforcement_cost = area * reinforcement_cost_factor

    # Calculate waterproofing cost
    waterproofing_cost = area * waterproofing_cost_factor

    # Total foundation cost
    total_cost = base_cost + depth_cost + soil_cost + reinforcement_cost + waterproofing_cost

    return total_cost


def main():
    print("Welcome to the Detailed Foundation Cost Estimator\n")

    # Get user input for project size (in square feet)
    area = float(input("Enter the project size in square feet: "))

    # Get user input for foundation type (slab/crawl_space/basement)
    foundation_type = input("Enter the foundation type (slab/crawl_space/basement): ").lower()
    if foundation_type not in ['slab', 'crawl_space', 'basement']:
        print("Invalid foundation type. Please enter 'slab', 'crawl_space', or 'basement'.")
        return

    # Get user input for foundation depth (in feet)
    depth = float(input("Enter the foundation depth in feet: "))

    # Get user input for soil condition (stable/moderate/unstable)
    soil_condition = input("Enter the soil condition (stable/moderate/unstable): ").lower()
    if soil_condition not in ['stable', 'moderate', 'unstable']:
        print("Invalid soil condition. Please enter 'stable', 'moderate', or 'unstable'.")
        return

    # Get user input for reinforcement (yes/no)
    reinforcement = input("Do you need reinforcement (yes/no): ").lower() == 'yes'

    # Get user input for waterproofing (yes/no)
    waterproofing = input("Do you need waterproofing (yes/no): ").lower() == 'yes'

    # Calculate the foundation cost
    total_cost = calculate_foundation_cost(area, foundation_type, depth, soil_condition, reinforcement, waterproofing)

    # Display the estimated cost
    print(f"\nThe estimated cost for the foundation is: INR {total_cost:,.2f}")


if __name__ == "__main__":
    main()
