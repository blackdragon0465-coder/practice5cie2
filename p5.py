import sys

if len(sys.argv) == 3:
    script_name = sys.argv[0]
    initialbalance = float(sys.argv[1])
    depositamount = float(sys.argv[2])
    print("User provided input values:")
else:
    script_name = sys.argv[0]
    initialbalance = 1000.0
    depositamount = 250.0
    print("No input given — using default values:")

updatedbalance = initialbalance + depositamount

print("\n--- Bank Account Balance ---")
print("Script Name:", script_name)
print("Initial Balance:", initialbalance)
print("Deposit Amount:", depositamount)
print("Updated Balance:", updatedbalance)
