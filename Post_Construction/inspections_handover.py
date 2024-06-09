def calculate_inspection_cost(area, inspection_types):
    # Base cost per square foot for different inspection types (hypothetical)
    inspection_costs = {
        'structural': 10,
        'electrical': 8,
        'plumbing': 7
    }

    # Calculate inspection costs
    total_cost = 0
    for inspection in inspection_types:
        if inspection in inspection_costs:
            total_cost += area * inspection_costs[inspection]

    return total_cost


def calculate_touchup_repair_cost(area, repair_complexity):
    # Base cost per square foot for different levels of repair complexity (hypothetical)
    repair_costs = {
        'minor': 5,
        'moderate': 10,
        'major': 15
    }

    # Calculate touch-up and repair cost
    total_cost = area * repair_costs[repair_complexity]

    return total_cost


def calculate_documentation_certification_cost(document_types):
    # Base cost for different types of documentation and certification (hypothetical)
    document_costs = {
        'occupancy_certificate': 5000,
        'safety_certificate': 3000,
        'energy_certificate': 2000
    }

    # Calculate documentation and certification cost
    total_cost = 0
    for document in document_types:
        if document in document_costs:
            total_cost += document_costs[document]

    return total_cost


def calculate_cleaning_preparation_cost(area, cleaning_type):
    # Base cost per square foot for different cleaning types (hypothetical)
    cleaning_costs = {
        'basic': 2,
        'detailed': 5
    }

    # Calculate cleaning and preparation cost
    total_cost = area * cleaning_costs[cleaning_type]

    return total_cost


def calculate_handover_ceremony_cost(handover_type):
    # Base cost for different types of handover ceremonies (hypothetical)
    handover_costs = {
        'simple': 1000,
        'standard': 3000,
        'grand': 5000
    }

    # Calculate handover ceremony cost
    total_cost = handover_costs[handover_type]

    return total_cost


def calculate_inspections_handover_cost(area, inspection_types, repair_complexity, document_types, cleaning_type,
                                        handover_type):
    # Calculate costs for each component
    inspection_cost = calculate_inspection_cost(area, inspection_types)
    touchup_repair_cost = calculate_touchup_repair_cost(area, repair_complexity)
    documentation_certification_cost = calculate_documentation_certification_cost(document_types)
    cleaning_preparation_cost = calculate_cleaning_preparation_cost(area, cleaning_type)
    handover_ceremony_cost = calculate_handover_ceremony_cost(handover_type)

    # Total inspections and handover cost
    total_cost = (inspection_cost + touchup_repair_cost + documentation_certification_cost +
                  cleaning_preparation_cost + handover_ceremony_cost)

    return total_cost


def inspections_handover():
    print("Welcome to the Detailed Inspections and Handover Cost Estimator\n")

    # Get user input for project size (in square feet)
    area = float(input("Enter the project size in square feet: "))

    # Get user input for inspection types (structural/electrical/plumbing)
    inspection_types = input(
        "Enter the inspection types (separate by commas, e.g., structural,electrical,plumbing): ").lower().split(',')

    # Get user input for repair complexity (minor/moderate/major)
    repair_complexity = input("Enter the repair complexity (minor/moderate/major): ").lower()
    if repair_complexity not in ['minor', 'moderate', 'major']:
        print("Invalid repair complexity. Please enter 'minor', 'moderate', or 'major'.")
        return

    # Get user input for documentation types (occupancy_certificate/safety_certificate/energy_certificate)
    document_types = input(
        "Enter the documentation types (separate by commas, e.g., occupancy_certificate,safety_certificate): ").lower().split(
        ',')

    # Get user input for cleaning type (basic/detailed)
    cleaning_type = input("Enter the cleaning type (basic/detailed): ").lower()
    if cleaning_type not in ['basic', 'detailed']:
        print("Invalid cleaning type. Please enter 'basic' or 'detailed'.")
        return

    # Get user input for handover ceremony type (simple/standard/grand)
    handover_type = input("Enter the handover ceremony type (simple/standard/grand): ").lower()
    if handover_type not in ['simple', 'standard', 'grand']:
        print("Invalid handover ceremony type. Please enter 'simple', 'standard', or 'grand'.")
        return

    # Calculate the inspections and handover cost
    total_cost = calculate_inspections_handover_cost(area, inspection_types, repair_complexity, document_types,
                                                     cleaning_type, handover_type)

    # Display the estimated cost
    print(f"\nThe estimated cost for the inspections and handover phase is: INR {total_cost:,.2f}")
    return total_cost

if __name__ == "__main__":
    inspections_handover()
