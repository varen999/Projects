import numpy as np

def spectral_radius(A):
    eigenvalues = np.linalg.eigvals(A)
    return max(abs(eigenvalues))



def path_graph(n):
    A = np.zeros((n,n))
    for i in range(n-1):
        A[i][i+1] = 1
        A[i+1][i] = 1
    return A


def cycle_graph(n):
    A = np.zeros((n,n))
    for i in range(n-1):
        A[i][i+1] = 1
        A[i+1][i] = 1
    A[0][n-1] = 1
    A[n-1][0] = 1
    return A


def complete_graph(n):
    A = np.ones((n,n)) - np.eye(n)
    return A


def custom_graph():
    n = int(input("Enter number of vertices: "))
    A = np.zeros((n,n))

    m = int(input("Enter number of edges: "))

    print("Enter edges (u v):")
    for i in range(m):
        u,v = map(int,input().split())
        A[u][v] = 1
        A[v][u] = 1

    return A



print("Select Graph Type")
print("1. Path Graph (Pn)")
print("2. Cycle Graph (Cn)")
print("3. Complete Graph (Kn)")
print("4. Custom Graph")

choice = int(input("Enter choice: "))


if choice == 1:
    n = int(input("Enter n for Path Graph Pn: "))
    A = path_graph(n)

elif choice == 2:
    n = int(input("Enter n for Cycle Graph Cn: "))
    A = cycle_graph(n)

elif choice == 3:
    n = int(input("Enter n for Complete Graph Kn: "))
    A = complete_graph(n)

elif choice == 4:
    A = custom_graph()

else:
    print("Invalid choice")
    exit()


print("\nAdjacency Matrix:")
print(A)

rho_before = spectral_radius(A)

print("\nSpectral Radius:",rho_before)



while True:

    print("\nChoose Operation")
    print("1. Add Edge")
    print("2. Remove Edge")
    print("3. Exit")

    op = int(input("Enter choice: "))

    if op == 1:

        u,v = map(int,input("Enter edge to add (u v): ").split())

        A[u][v] = 1
        A[v][u] = 1

        rho = spectral_radius(A)

        print("\nUpdated Adjacency Matrix:")
        print(A)

        print("New Spectral Radius:",rho)


    elif op == 2:

        u,v = map(int,input("Enter edge to remove (u v): ").split())

        A[u][v] = 0
        A[v][u] = 0

        rho = spectral_radius(A)

        print("\nUpdated Adjacency Matrix:")
        print(A)

        print("New Spectral Radius:",rho)


    elif op == 3:
        print("Program Ended")
        break

    else:
        print("Invalid option")