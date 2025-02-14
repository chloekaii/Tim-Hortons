

if __name__ == '__main__':
    with open("input.txt", "r") as file:
        K, L = map(int, file.readline().split())
        n = int(file.readline().strip())
        H = list(map(int, file.readline().split()))

    selected_locations = []
    current_position = 0
    i = 0

    while current_position < K:
        while i < n and H[i] <= current_position + L:
            i += 1

        current_position = H[i-1]
        selected_locations.append(H[i-1])

    with open("output.txt", "w") as file:
        file.write(" ".join(map(str, selected_locations)))

