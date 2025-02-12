def main():
    import sys
    from interpreter.executor import Executor
    from interpreter.error_parser import ErrorParser

    executor = Executor()
    error_parser = ErrorParser()

    # Get code from command line arguments
    if len(sys.argv) < 2:
        print("Please provide the code to execute.")
        return

    code = sys.argv[1]

    # Execute the code
    output, error = executor.execute(code)

    if error:
        # Parse the error and provide a user-friendly message
        friendly_message = error_parser.parse(error)
        print(friendly_message)
    else:
        print(output)
        print("Code executed with no warnings and errors.")

if __name__ == "__main__":
    main()