# Function arguments: positional and default

def power(base, exponent=2):
    # Returns base raised to the exponent (default is 2)
    return base ** exponent

print(power(3))      # Uses default exponent
print(power(2, 3))   # Uses provided exponent
