import time
def returnToHome():
    print("Returning to home in", end=" ", flush=True)
    for i in range(3, 0, -1):
        print(f"{i}", end=" ", flush=True)
        time.sleep(1)
    print("\n")