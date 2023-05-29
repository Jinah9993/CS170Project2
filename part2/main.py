import math

def nearest_neighbor_classifier(data, point, feature_subset):
    nearest_neighbor = None
    shortest_distance = float('inf')

    for i, instance in enumerate(data):
        if i == point:
            continue

        distance = 0
        for j in feature_subset:
            distance += pow((instance[j] - data[point][j]), 2)

        distance = math.sqrt(distance)

        if distance < shortest_distance:
            nearest_neighbor = i
            shortest_distance = distance

    return nearest_neighbor


def leave_one_out_validator(data, feature_subset):
    num_correct = 0.0
    num_instances = len(data)

    for i in range(num_instances):
        neighbor = nearest_neighbor_classifier(data, i, feature_subset)

        if data[neighbor][0] == data[i][0]:
            num_correct += 1

    accuracy = (num_correct / num_instances) * 100

    return accuracy


def normalize_data(instances):
    num_instances = len(instances)
    num_features = len(instances[0]) - 1
    normalized_instances = [row[:] for row in instances]

    mean = []
    std = []

    for i in range(num_features):
        mean.append((sum(row[i+1] for row in instances)) / num_instances)
        std.append(math.sqrt((sum(pow((row[i+1] - mean[i]), 2) for row in instances)) / num_instances))

    for i in range(num_instances):
        for j in range(num_features):
            normalized_instances[i][j+1] = (instances[i][j+1] - mean[j]) / std[j]

    return normalized_instances