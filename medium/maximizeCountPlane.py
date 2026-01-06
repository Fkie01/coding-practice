def maximizeCountPlaceStop(A, B):
    planes = [init / speed for init, speed in zip(A, B)]
    sorted_plane = sorted(planes)[::-1]
    num_plane = 0
    time = 0
    while sorted_plane:
        plane = sorted_plane[-1]
        if plane - time > 0:
            sorted_plane.pop()
            time += 1
            num_plane += 1
        else:
            sorted_plane.pop()
    return num_plane


A = [1, 3, 5, 4, 8]
B = [1, 2, 2, 1, 2]
print(maximizeCountPlaceStop(A, B))  # 4
A = [2, 8, 2, 3, 1]
B = [1, 4, 2, 2, 2]
print(maximizeCountPlaceStop(A, B))  # 2
