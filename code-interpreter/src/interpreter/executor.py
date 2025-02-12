class Executor:
    def compile_code(self, code: str):
        try:
            compiled_code = compile(code, '<string>', 'exec')
            return compiled_code, None
        except SyntaxError as e:
            return None, e

    def execute_code(self, compiled_code):
        local_vars = {}
        try:
            exec(compiled_code, {}, local_vars)
            return local_vars, "Code executed with no warnings and errors."
        except Exception as e:
            return None, str(e)