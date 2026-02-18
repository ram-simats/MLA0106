import itertools

def solve_cryptarithm():
    letters = ('S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y')
    digits = range(10)

    # Generate all possible digit permutations
    for perm in itertools.permutations(digits, len(letters)):
        s, e, n, d, m, o, r, y = perm

        # Leading letters cannot be zero
        if s == 0 or m == 0:
            continue

        # Convert words to numbers
        send = 1000*s + 100*e + 10*n + d
        more = 1000*m + 100*o + 10*r + e
        money = 10000*m + 1000*o + 100*n + 10*e + y

        # Check if equation holds
        if send + more == money:
            print("Solution Found:")
            print(f"S={s}, E={e}, N={n}, D={d}, M={m}, O={o}, R={r}, Y={y}")
            print(f"{send} + {more} = {money}")
            return

    print("No solution found.")

# Run the program
if __name__ == "__main__":
    solve_cryptarithm()
