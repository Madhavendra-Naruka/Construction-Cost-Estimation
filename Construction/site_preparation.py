def calculate_land_clearing_cost(area, vegetation_density):
    # Hypothetical cost per square foot based on vegetation density
    density_factor = {
        'low': 2,
        'medium': 4,
        'high': 6
    }
    cost_per_sqft = density_factor[vegetation_density]
    total_cost = area * cost_per_sqft
    return total_cost


def calculate_excavation_cost(area, soil_type):
    # Hypothetical cost per square foot based on soil type
    soil_factor = {
        'soft': 5,
        'medium': 10,
        'hard': 15
    }
    cost_per_sqft = soil_factor[soil_type]
    total_cost = area * cost_per_sqft
    return total_cost


def calculate_grading_cost(area):
    # Hypothetical cost per square foot for grading
    cost_per_sqft = 3
    total_cost = area * cost_per_sqft
    return total_cost


def calculate_utilities_setup_cost(area):
    # Hypothetical flat rate cost for utilities setup
    base_cost = 10000
    cost_per_sqft = 1
    total_cost = base_cost + (area * cost_per_sqft)
    return total_cost


def calculate_access_roads_cost(length):
    # Hypothetical cost per linear foot for temporary access roads
    cost_per_linear_foot = 50
    total_cost = length * cost_per_linear_foot
    return total_cost


def calculate_site_preparation_cost(area, vegetation_density, soil_type, access_road_length):
    # Calculate costs for each component
    land_clearing_cost = calculate_land_clearing_cost(area, vegetation_density)
    excavation_cost = calculate_excavation_cost(area, soil_type)
    grading_cost = calculate_grading_cost(area)
    utilities_setup_cost = calculate_utilities_setup_cost(area)
    access_roads_cost = calculate_access_roads_cost(access_road_length)

    # Total site preparation cost
    total_cost = (land_clearing_cost + excavation_cost + grading_cost +
                  utilities_setup_cost + access_roads_cost)

    return total_cost


def site_preparation():
    print("Welcome to the Detailed Site Preparation Cost Estimator\n")

    # Get user input for project size (in square feet)
    area = float(input("Enter the project size in square feet: "))

    # Get user input for vegetation density (low/medium/high)
    vegetation_density = input("Enter the vegetation density (low/medium/high): ").lower()
    if vegetation_density not in ['low', 'medium', 'high']:
        print("Invalid vegetation density. Please enter 'low', 'medium', or 'high'.")
        return

    # Get user input for soil type (soft/medium/hard)
    soil_type = input("Enter the soil type (soft/medium/hard): ").lower()
    if soil_type not in ['soft', 'medium', 'hard']:
        print("Invalid soil type. Please enter 'soft', 'medium', or 'hard'.")
        return

    # Get user input for access road length (in linear feet)
    access_road_length = float(input("Enter the length of access roads in linear feet: "))

    # Calculate the site preparation cost
    total_cost = calculate_site_preparation_cost(area, vegetation_density, soil_type, access_road_length)

    # Display the estimated cost
    print(f"\nThe estimated cost for site preparation is: INR {total_cost:,.2f}")
    return total_cost

if __name__ == "__main__":
    site_preparation()
