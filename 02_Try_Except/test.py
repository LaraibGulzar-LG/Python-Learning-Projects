


# 7. File reading with error handling
def read_file_safely(filename):
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "File nahi mili!"
    except PermissionError:
        return "Permission nahi hai!"
    except Exception as e:
        return f"Koi error: {e}"

print(read_file_safely('students.csv'))  # Existing file
print(read_file_safely('fake.txt'))     # Non-existing

# 8. JSON parsing with error handling
import json
def parse_json_safely(json_string):
    try:
        return json.loads(json_string)
    except json.JSONDecodeError:
        return "Invalid JSON!"

print(parse_json_safely('{"name": "Ali"}'))  # Valid
print(parse_json_safely('{name: Ali}'))      # Invalid

# 9. List index error
my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError:
    print("Index out of range!")

# 10. Comprehensive error handling for all previous code
def process_log_safely(log_line):
    try:
        if not log_line:
            return "Empty log!"
        parts = log_line.split(':')
        if len(parts) < 2:
            return "Invalid log format!"
        return parts[0].strip()
    except Exception as e:
        return f"Processing error: {e}"

print(process_log_safely("User001: ERROR"))
print(process_log_safely(""))  # Empty