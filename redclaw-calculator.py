import json

def calculate_capacity(square_meters, depth):
    space_per_crayfish = 0.1  
    depth_factor = 2 

    total_space = square_meters * depth * depth_factor
    capacity = int(total_space / space_per_crayfish)
    return capacity

def save_capacity_to_json(dam_size, depth, capacity):
    data = {
        'DamSizeSquareMeters': dam_size,
        'Depth': depth,
        'Capacity': capacity
    }

    with open('redclaw_capacity.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)
    print("Capacity information saved to redclaw_capacity.json")

def main():
    print("Welcome to the Redclaw Crayfish Capacity Calculator!")

    dam_size = float(input("Enter the dam size in square meters: "))
    depth = float(input("Enter the depth of the dam in meters: "))

    capacity = calculate_capacity(dam_size, depth)

    print(f"\nEstimated Redclaw Crayfish Capacity: {capacity} crayfish")

    save_capacity_to_json(dam_size, depth, capacity)

if __name__ == "__main__":
    main()
