# Photon IDE developed by SkyDevelopment

from contentReader import CodeFile

class PhotonList:
    def __init__(self, values):
        self.values = values # A list of values

    def length(self):
        return len(self.values) # Return the length of the list

    def get(self, index):
        return self.values[index] # Return the element at the given index

    def set(self, index, value):
        self.values[index] = value # Set the element at the given index to the given value

    def add(self, value):
        self.values.append(value) # Append the value to the end of the list

    def pop(self):
        return self.values.pop() # Remove and return the last element of the list

    def insert(self, index, value):
        self.values.insert(index, value) # Insert the value at the given index

    def remove(self, index):
        self.values.pop(index) # Remove and return the element at the given index

    def sort(self, order):
        if order == "asc":
            self.values.sort() # Sort the list in ascending order
        elif order == "desc":
            self.values.sort(reverse=True) # Sort the list in descending order

    def reverse(self):
        self.values.reverse() # Reverse the order of the list

    def __contains__(self, value):
        return value in self.values # Return True if the value is in the list, False otherwise

    def __str__(self):
        return str(self.values) # Return a string representation of the list

class PhotonClassic:
    def __init__(self):
        self.variables = {}  # Dictionary to store variables and their types

    def execute_line(self, line):
        # Handling variable declarations
        if any(line.startswith(var_type) for var_type in ["const ", "let ", "var ", "secure "]):
            declaration, value = line.split(' = ')
            var_type, var_name = declaration.split()
            value = value.strip('";')

            # Handling value types
            if value.isdigit():
                value = int(value)  # Convert to number if it's a digit
            elif value in ["True", "False"]:
                value = value == "True"  # Convert to boolean if it's True or False
            elif value.startswith("[") and value.endswith("]"): # Check if value is a list
                value = PhotonList(eval(value)) # Convert to a PhotonList object
            # Add other type conversions if necessary

            # Store the variable with its type and value
            self.variables[var_name] = {"type": var_type, "value": value}

        # Handling console commands
        elif line.startswith("console.display"):
            tokens = line.split('console.display')
            content = tokens[1].strip("();\" ")
            
            # Check if content is a variable
            if content in self.variables:
                print(self.variables[content]["value"])  # Display the value of the variable
            else:
                print(content)  # Otherwise, print the content directly

        # Handling list methods
        elif any(line.startswith(var_name + ".") for var_name in self.variables): # Check if line starts with a variable name followed by a dot
            var_name, method = line.split(".") # Split the line by the dot
            method_name, args = method.split("(") # Split the method by the opening parenthesis
            args = args.strip(");") # Remove the closing parenthesis and the semicolon from the arguments
            args = args.split(",") # Split the arguments by the comma
            args = [arg.strip() for arg in args] # Remove any whitespace from the arguments
            args = [eval(arg) if arg.isdigit() else arg.strip('"') for arg in args] # Convert any numeric arguments to numbers and any string arguments to strings
            var_value = self.variables[var_name]["value"] # Get the value of the variable
            if isinstance(var_value, PhotonList): # Check if the value is a PhotonList object
                if method_name == "length": # Check if the method name is length
                    print(var_value.length()) # Print the length of the list
                elif method_name == "get": # Check if the method name is get
                    index = args[0] # Get the index argument
                    print(var_value.get(index)) # Print the element at the given index
                elif method_name == "set": # Check if the method name is set
                    index, value = args # Get the index and value arguments
                    var_value.set(index, value) # Set the element at the given index to the given value
                elif method_name == "add": # Check if the method name is append
                    value = args[0] # Get the value argument
                    var_value.add(value) # Append the value to the end of the list
                elif method_name == "pop": # Check if the method name is pop
                    print(var_value.pop()) # Remove and print the last element of the list
                elif method_name == "insert": # Check if the method name is insert
                    index, value = args # Get the index and value arguments
                    var_value.insert(index, value) # Insert the value at the given index
                elif method_name == "remove": # Check if the method name is remove
                    index = args[0] # Get the index argument
                    var_value.remove(index) # Remove and return the element at the given index
                elif method_name == "sort": # Check if the method name is sort
                    order = args[0] # Get the order argument
                    var_value.sort(order) # Sort the list in the given order
                elif method_name == "reverse": # Check if the method name is reverse
                    var_value.reverse() # Reverse the order of the list
                # Add other list methods if necessary

    def execute_code(self):
        for file_name, lines in CodeFile.items():
            print(f"From {file_name} : ")
            for line in lines:
                self.execute_line(line.strip())  # Call execute_line method for each line

if __name__ == "__main__":
    print(r"""
  ___   _   _    ___   _____   ___    _   _
 | _ \ | |_| |  / _ \ |_   _| /   \  | \ | |
 |  _/ |  _  | | |_| |  | |  | |_| | | |\| |
 |_|   |_| |_|  \___/   |_|   \___/  |_| \_| . py
 Developed by SkyDevelopement
=============================================================================
    """)
    classic = PhotonClassic()  # Create an instance of the PhotonClassic class
    classic.execute_code()  # Call execute_code method on the instance
    print("""
=============================================================================
    """)
