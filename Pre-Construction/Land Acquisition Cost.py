def get_land_rate(area_type, city_tier):
    # Define the base land rates based on area type and city tier (rates are hypothetical)
    rates = {
        'rural': {
            'tier_1': 500,  # rate per square foot in INR
            'tier_2': 300,
            'tier_3': 150
        },
        'urban': {
            'tier_1': 2000,
            'tier_2': 1500,
            'tier_3': 1000
        }
    }
    return rates[area_type][city_tier]


def calculate_land_cost(area, area_type, city_tier, proximity_infra, land_use, topography, legal_docs):
    # Get the base rate for the specified area type and city tier
    rate_per_sqft = get_land_rate(area_type, city_tier)

    # Adjust the rate based on additional parameters
    proximity_factor = {'near': 1.2, 'average': 1.0, 'far': 0.8}
    land_use_factor = {'residential': 1.0, 'commercial': 1.5, 'agricultural': 0.7}
    topography_factor = {'flat': 1.0, 'hilly': 0.9}

    rate_per_sqft *= proximity_factor[proximity_infra]
    rate_per_sqft *= land_use_factor[land_use]
    rate_per_sqft *= topography_factor[topography]

    # Calculate the base cost
    base_cost = area * rate_per_sqft

    # Add legal and documentation costs
    total_cost = base_cost + legal_docs

    return total_cost


def main():
    print("Welcome to the Land Acquisition Cost Estimator\n")

    # Get user input for area
    area = float(input("Enter the area of the land in square feet: "))

    # Get user input for area type (rural/urban)
    area_type = input("Enter the area type (rural/urban): ").lower()
    if area_type not in ['rural', 'urban']:
        print("Invalid area type. Please enter 'rural' or 'urban'.")
        return

    # Get user input for city tier (tier_1/tier_2/tier_3)
    city_tier = input("Enter the city tier (tier_1/tier_2/tier_3): ").lower()
    if city_tier not in ['tier_1', 'tier_2', 'tier_3']:
        print("Invalid city tier. Please enter 'tier_1', 'tier_2', or 'tier_3'.")
        return

    # Get user input for proximity to infrastructure (near/average/far)
    proximity_infra = input("Enter the proximity to key infrastructure (near/average/far): ").lower()
    if proximity_infra not in ['near', 'average', 'far']:
        print("Invalid proximity. Please enter 'near', 'average', or 'far'.")
        return

    # Get user input for land use type (residential/commercial/agricultural)
    land_use = input("Enter the land use type (residential/commercial/agricultural): ").lower()
    if land_use not in ['residential', 'commercial', 'agricultural']:
        print("Invalid land use type. Please enter 'residential', 'commercial', or 'agricultural'.")
        return

    # Get user input for land topography (flat/hilly)
    topography = input("Enter the land topography (flat/hilly): ").lower()
    if topography not in ['flat', 'hilly']:
        print("Invalid topography. Please enter 'flat' or 'hilly'.")
        return

    # Get user input for legal and documentation costs
    legal_docs = float(input("Enter the estimated legal and documentation costs in INR: "))

    # Calculate the land cost
    total_cost = calculate_land_cost(area, area_type, city_tier, proximity_infra, land_use, topography, legal_docs)

    # Display the estimated cost
    print(f"\nThe estimated cost of the land is: INR {total_cost:,.2f}")


if __name__ == "__main__":
    main()
