def calculate_finish_cost(area, finish_type):
    # Base cost per square foot for different interior finishes (hypothetical)
    finish_costs = {
        'basic': 100,
        'standard': 200,
        'premium': 300
    }

    # Calculate base cost
    base_cost = area * finish_costs[finish_type]

    return base_cost


def calculate_room_costs(rooms, room_costs):
    # Calculate cost for each room type
    total_cost = 0
    for room_type, count in rooms.items():
        total_cost += count * room_costs[room_type]
    return total_cost


def calculate_flooring_cost(area, flooring_type):
    # Base cost per square foot for different flooring types (hypothetical)
    flooring_costs = {
        'tile': 50,
        'wood': 100,
        'carpet': 75
    }

    # Calculate flooring cost
    total_cost = area * flooring_costs[flooring_type]

    return total_cost


def calculate_painting_cost(area, paint_quality):
    # Base cost per square foot for different paint qualities (hypothetical)
    paint_costs = {
        'basic': 10,
        'standard': 20,
        'premium': 30
    }

    # Calculate painting cost
    total_cost = area * paint_costs[paint_quality]

    return total_cost


def calculate_lighting_electrical_cost(area, lighting_type):
    # Base cost per square foot for different lighting types (hypothetical)
    lighting_costs = {
        'basic': 20,
        'standard': 40,
        'premium': 60
    }

    # Calculate lighting and electrical cost
    total_cost = area * lighting_costs[lighting_type]

    return total_cost


def calculate_plumbing_cost(area, plumbing_quality):
    # Base cost per square foot for different plumbing qualities (hypothetical)
    plumbing_costs = {
        'basic': 50,
        'standard': 100,
        'premium': 150
    }

    # Calculate plumbing cost
    total_cost = area * plumbing_costs[plumbing_quality]

    return total_cost


def calculate_additional_features_cost(additional_features):
    # Calculate total cost for additional features
    total_cost = sum(additional_features.values())

    return total_cost


def calculate_interior_work_cost(area, finish_type, rooms, room_costs, flooring_type, paint_quality, lighting_type,
                                 plumbing_quality, additional_features):
    # Calculate costs for each component
    finish_cost = calculate_finish_cost(area, finish_type)
    room_costs_total = calculate_room_costs(rooms, room_costs)
    flooring_cost = calculate_flooring_cost(area, flooring_type)
    painting_cost = calculate_painting_cost(area, paint_quality)
    lighting_electrical_cost = calculate_lighting_electrical_cost(area, lighting_type)
    plumbing_cost = calculate_plumbing_cost(area, plumbing_quality)
    additional_features_cost = calculate_additional_features_cost(additional_features)

    # Total interior work cost
    total_cost = (finish_cost + room_costs_total + flooring_cost + painting_cost +
                  lighting_electrical_cost + plumbing_cost + additional_features_cost)

    return total_cost


def interior_work():
    print("Welcome to the Detailed Interior Work Cost Estimator\n")

    # Get user input for project size (in square feet)
    area = float(input("Enter the project size in square feet: "))

    # Get user input for interior finish type (basic/standard/premium)
    finish_type = input("Enter the interior finish type (basic/standard/premium): ").lower()
    if finish_type not in ['basic', 'standard', 'premium']:
        print("Invalid interior finish type. Please enter 'basic', 'standard', or 'premium'.")
        return

    # Get user input for number of rooms
    rooms = {}
    room_types = ['bedroom', 'bathroom', 'kitchen', 'living room', 'dining room']
    room_costs = {
        'bedroom': 10000,
        'bathroom': 15000,
        'kitchen': 30000,
        'living room': 20000,
        'dining room': 18000
    }
    for room_type in room_types:
        count = int(input(f"Enter the number of {room_type}s: "))
        rooms[room_type] = count

    # Get user input for flooring type (tile/wood/carpet)
    flooring_type = input("Enter the flooring type (tile/wood/carpet): ").lower()
    if flooring_type not in ['tile', 'wood', 'carpet']:
        print("Invalid flooring type. Please enter 'tile', 'wood', or 'carpet'.")
        return

    # Get user input for paint quality (basic/standard/premium)
    paint_quality = input("Enter the paint quality (basic/standard/premium): ").lower()
    if paint_quality not in ['basic', 'standard', 'premium']:
        print("Invalid paint quality. Please enter 'basic', 'standard', or 'premium'.")
        return

    # Get user input for lighting type (basic/standard/premium)
    lighting_type = input("Enter the lighting type (basic/standard/premium): ").lower()
    if lighting_type not in ['basic', 'standard', 'premium']:
        print("Invalid lighting type. Please enter 'basic', 'standard', or 'premium'.")
        return

    # Get user input for plumbing quality (basic/standard/premium)
    plumbing_quality = input("Enter the plumbing quality (basic/standard/premium): ").lower()
    if plumbing_quality not in ['basic', 'standard', 'premium']:
        print("Invalid plumbing quality. Please enter 'basic', 'standard', or 'premium'.")
        return

    # Get user input for additional features
    additional_features = {}
    while True:
        feature = input("Enter an additional feature (or 'done' to finish): ").lower()
        if feature == 'done':
            break
        cost = float(input(f"Enter the cost for {feature}: "))
        additional_features[feature] = cost

    # Calculate the interior work cost
    total_cost = calculate_interior_work_cost(area, finish_type, rooms, room_costs, flooring_type, paint_quality,
                                              lighting_type, plumbing_quality, additional_features)

    # Display the estimated cost
    print(f"\nThe estimated cost for the interior work is: INR {total_cost:,.2f}")


if __name__ == "__main__":
    interior_work()
