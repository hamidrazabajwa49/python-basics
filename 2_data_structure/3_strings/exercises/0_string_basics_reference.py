# Creating Strings
s = "Hello"
s2 = 'World'
s3 = """Multiline
String"""

# Indexing & Slicing
s[0]      # First char
s[-1]     # Last char
s[1:4]    # Slice 'ell'
s[::-1]   # Reverse

# Case Conversion
s.lower()
s.upper()
s.title()
s.strip()  # Remove whitespace

# Searching & Replacing
s.find("e")
s.replace("l", "L")
s.count("l")

# Splitting & Joining
s.split()
"-".join(["a", "b"])

# Checks
s.isalpha()
s.isdigit()
"sub" in s

# Formatting
name = "Ali"
f"Hello {name}"
