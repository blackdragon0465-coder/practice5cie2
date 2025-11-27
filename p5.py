import sys

if len(sys.argv) == 3:
    script_name = sys.argv[0]
    initial_balance = float(sys.argv[1])
    deposit_amount = float(sys.argv[2])
    print("User provided input values:")
else:
    script_name = sys.argv[0]
    initial_balance = 1000.0
    deposit_amount = 250.0
    print("No input given — using default values:")

updated_balance = initial_balance + deposit_amount

print("\n--- Bank Account Balance ---")
print("Script Name:", script_name)
print("Initial Balance:", initial_balance)
print("Deposit Amount:", deposit_amount)
print("Updated Balance:", updated_balance)
