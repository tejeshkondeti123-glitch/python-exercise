
# Log File Reader Program

print("===================================")
print("        LOG FILE READER")
print("===================================")

# Open the log file
filename = "sample_log"

try:
    with open(filename, "r") as file:
        logs = file.readlines()

    info = 0
    warning = 0
    error = 0

    print("\nLog File Contents:")
    print("----------------------------")

    for line in logs:
        print(line.strip())

        if "INFO" in line:
            info += 1
        elif "WARNING" in line:
            warning += 1
        elif "ERROR" in line:
            error += 1

    print("\n========== LOG SUMMARY ==========")
    print("Total Log Entries:", len(logs))
    print("INFO Messages:", info)
    print("WARNING Messages:", warning)
    print("ERROR Messages:", error)

except FileNotFoundError:
    print("Error: Log file not found!")

print("===================================")


# output
# ===================================
#         LOG FILE READER
# ===================================
# Error: Log file not found!
# ===================================
# PS C:\python uploads> 