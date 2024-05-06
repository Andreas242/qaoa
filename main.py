stations = ['S1', 'S2', 'S3', 'S4']
trains = ['T1', 'T2', 'T3']
tracks = {
    ('S1', 'S2'): 10,
    ('S2', 'S3'): 7,
    ('S3', 'S4'): 9,
    ('S2', 'S1'): 10,
    ('S3', 'S2'): 7,
    ('S4', 'S3'): 9
}

def calculate_travel_time(train_schedule):
    """Calculate the total travel time for a given train schedule."""
    total_time = 0
    for i in range(len(train_schedule) - 1):
        start, end = train_schedule[i], train_schedule[i+1]
        travel_time = tracks.get((start, end))
        if travel_time is None:
            print(f"No direct track exists from {start} to {end}.")
            return float('inf')  # Returns infinite time if path is invalid
        total_time += travel_time
    return total_time

def cost_function(schedule):
    """Calculate the total cost based on travel time and conflicts."""
    total_time = 0
    conflicts = 0
    all_routes = []

    for train, path in schedule.items():
        # Calculate total travel time for each train
        travel_time = calculate_travel_time(path)
        if travel_time == float('inf'):  # Skip conflict checking if path is invalid
            continue
        total_time += travel_time
        all_routes.append((train, path))

    # Detect conflicts
    for i in range(len(all_routes)):
        for j in range(i + 1, len(all_routes)):
            train_i, path_i = all_routes[i]
            train_j, path_j = all_routes[j]
            # Check for overlapping routes
            common_sections = set(zip(path_i, path_i[1:])) & set(zip(path_j, path_j[1:]))
            if common_sections:
                conflicts += len(common_sections)
                print(f"Conflict detected between {train_i} and {train_j} on sections: {common_sections}")

    large_penalty = 100
    print(f"Total conflicts: {conflicts}")
    return total_time + conflicts * large_penalty

sample_schedule = {
    'T1': ['S1', 'S2', 'S3', 'S4'],
    'T2': ['S4', 'S3', 'S2'],
}

cost = cost_function(sample_schedule)
print(f"Total cost for the sample schedule: {cost}")
