def anagram_mappings(A, B) -> list[int]:
    locations = {}
    for i in range(len(B)):
        locations[B[i]] = i
    mapping = []
    for x in A:
        mapping.append(locations[x])
    return mapping


if __name__ == "__main__":
    A = [12, 28, 46, 32, 50]
    B = [50, 12, 32, 46, 28]
    print(anagram_mappings(A, B))  # [1, 4, 3, 2, 0]
