import math

def k_means_clustering(points: list[tuple[float, ...]], k: int, initial_centroids: list[tuple[float, ...]], max_iterations: int) -> list[tuple[float, ...]]:

    def distance(a, b):
        squared_distance = 0

        for dimension in range(len(a)):
            squared_distance += (a[dimension] - b[dimension]) ** 2

        return math.sqrt(squared_distance)

    for iteration in range(max_iterations):

        clusters = [[] for _ in range(k)]

        for point_index in range(len(points)):
            min_distance = 999999

            for centroid_index in range(len(initial_centroids)):
                current_distance = distance(
                    points[point_index],
                    initial_centroids[centroid_index]
                )

                if current_distance < min_distance:
                    min_distance = current_distance
                    closest_cluster = centroid_index

            clusters[closest_cluster].append(points[point_index])

        new_centroids = []

        for cluster_index in range(len(clusters)):

            if len(clusters[cluster_index]) == 0:
                new_centroids.append(initial_centroids[cluster_index])

            else:
                sums = [0] * len(clusters[cluster_index][0])

                for point_index in range(len(clusters[cluster_index])):
                    for dimension in range(len(clusters[cluster_index][point_index])):
                        sums[dimension] += clusters[cluster_index][point_index][dimension]

                centroid = []

                for dimension in range(len(sums)):
                    centroid.append(
                        sums[dimension] / len(clusters[cluster_index])
                    )

                new_centroids.append(tuple(centroid))

        if new_centroids == initial_centroids:
            final_centroids = new_centroids
            break

        else:
            initial_centroids = new_centroids

    final_centroids = initial_centroids

    return final_centroids