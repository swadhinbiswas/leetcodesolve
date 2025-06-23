def tower_of_hanoi_array_simulation(n: int, source: list, auxiliary: list, target: list, move_count: list) -> None:
    if n == 0:
        return
    tower_of_hanoi_array_simulation(n - 1, source, target, auxiliary, move_count)
    if source:
        disk_to_move = source.pop()
        target.append(disk_to_move)
        move_count[0] += 1
        print(f"Move {move_count[0]}: Move disk {disk_to_move} from Source to Target")
        print(f"  Current state: Source={source}, Auxiliary={auxiliary}, Target={target}\n")
    else:
        print(f"Error: Source array is unexpectedly empty when trying to move disk {n}.")
        return
    tower_of_hanoi_array_simulation(n - 1, auxiliary, source, target, move_count)

if __name__ == "__main__":
    initial_array_A = [1, 2, 3, 4, 5]
    print(f"Original Array A: {initial_array_A}")
    source_peg_array = initial_array_A[::-1] # [5, 4, 3, 2, 1]
    auxiliary_peg_array = []
    target_peg_array = []

    num_elements_to_move = len(initial_array_A)
    total_moves = [0]
    print("\n--- Starting Tower of Hanoi Array Simulation ---")
    print(f"Initial Peg States:")
    print(f"  Source Peg (A): {source_peg_array}")
    print(f"  Auxiliary Peg (B): {auxiliary_peg_array}")
    print(f"  Target Peg (C): {target_peg_array}\n")

    tower_of_hanoi_array_simulation(num_elements_to_move, source_peg_array, auxiliary_peg_array, target_peg_array, total_moves)

    print("\n--- Simulation Complete! ---")
    print("\nFinal Peg States:")
    print(f"  Source Peg (A): {source_peg_array}")
    print(f"  Auxiliary Peg (B): {auxiliary_peg_array}")
    print(f"  Target Peg (C): {target_peg_array}")
    print(f"Total moves: {total_moves[0]}")
    print(f"Target Array (reversed to match original order if 1 is smallest): {target_peg_array[::-1]}")
