def format_success_message(output):
    return f"Output: {output}\nCode executed with no warnings and errors."

def format_error_message(error, line_number):
    return f"You missed a semicolon at line {line_number}." if "missing semicolon" in error else f"Error: {error}"