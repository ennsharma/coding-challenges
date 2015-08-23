size = int(input())
if (size > 0):
	print("  /\\")
	for _ in range(size):
		print("  ||")
	print(" /||\\")
	print("/:||:\\")
	for _ in range(size - 1):
		print("|:||:|")
	print("|/||\\|")
	print("  **")
	print("  **")
