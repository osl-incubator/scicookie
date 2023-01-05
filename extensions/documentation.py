from jinja2.ext import Extension


class DocFormatExtension(Extension):
    """Simple jinja2 extension for cookiecutter test purposes."""

    tags = {'docs_format'}


    def __init__(self, environment):
        super().__init__(environment)

        """
        dir(environment)
        ['__annotations__', '__class__', '__delattr__', '__dict__', '__dir__', 
        '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', 
        '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', 
        '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', 
        '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_compile', 
        '_filter_test_common', '_generate', '_load_template', '_parse', 
        '_read_extensions', '_tokenize', 'add_extension', 'auto_reload', 'autoescape', 
        'block_end_string', 'block_start_string', 'bytecode_cache', 'cache', 'call_filter', 
        'call_test', 'code_generator_class', 'comment_end_string', 'comment_start_string', 
        'compile', 'compile_expression', 'compile_templates', 'context_class', 'datetime_format', 
        'extend', 'filters', 'finalize', 'from_string', 'get_or_select_template', 'get_template', 
        'getattr', 'getitem', 'globals', 'handle_exception', 'iter_extensions', 'join_path', 
        'keep_trailing_newline', 'lex', 'lexer', 'line_comment_prefix', 'line_statement_prefix', 
        'linked_to', 'list_templates', 'loader', 'lstrip_blocks', 'make_globals', 'newline_sequence', 
        'optimized', 'overlay', 'overlayed', 'parse', 'policies', 'preprocess', 'sandboxed', 'select_template', 
        'shared', 'template_class', 'tests', 'trim_blocks', 'undefined', 'variable_end_string', 'variable_start_string']

        """

        while True:
            print("\nPlease select documentation mode")
            choice = str(input('[1] Markdown\n[2] reStructuredText\n'))
            
            if "1" in choice:
                ans = "md"
                break
            elif "2" in choice:
                ans = "rst"
                break
            else:
                print("Please select one of the options above.")
                continue

        
        environment.globals.update(docs_format = ans)
        print(environment.globals)


if __name__ == "__main__":
    print('Extensions module imported')
    DocFormatExtension()
