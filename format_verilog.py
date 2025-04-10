import sublime
import sublime_plugin
import subprocess
import os

SETTINGS_FILE = 'FormatVerilog.sublime-settings'

def plugin_settings():
    """Load plugin settings."""
    return sublime.load_settings(SETTINGS_FILE)

def log_error(message):
    """Log an error message to the console."""
    print("FormatVerilog Error: {}".format(message))

def log_info(message):
    """Log an info message to the console."""
    # print("FormatVerilog Info: {}".format(message)) # Uncomment for debugging
    pass

class FormatVerilogOnSave(sublime_plugin.EventListener):
    """Listener to format Verilog files on save."""

    def on_pre_save(self, view):
        settings = plugin_settings()
        if not settings.get('enabled', True):
            log_info("Format on save is disabled in settings.")
            return

        # Check syntax for Sublime Text 3
        syntax_file_path = view.settings().get('syntax')
        if not syntax_file_path or 'verilog' not in syntax_file_path.lower():
            # Only apply to Verilog files
            log_info("Not a Verilog file, skipping format.")
            return

        executable_path = settings.get('verible_executable_path')
        if not executable_path:
            log_error("'verible_executable_path' not configured in FormatVerilog.sublime-settings.")
            sublime.status_message("FormatVerilog Error: Path not set")
            return

        # Expand ${packages} variable
        window = view.window()
        if not window:
            log_error("Could not get window object.")
            return
        expanded_path = sublime.expand_variables(executable_path, window.extract_variables())

        # Build command list with options from settings
        cmd = [expanded_path]

        # Helper function to add boolean flags ONLY if set by user
        def add_bool_flag(setting_name, flag_name):
            if settings.has(setting_name): # Check if the setting exists
                value = settings.get(setting_name)
                if isinstance(value, bool):
                    cmd.append('--{}=true'.format(flag_name) if value else '--{}=false'.format(flag_name))
                else:
                     log_error("Invalid type for setting '{}'. Expected boolean.".format(setting_name))

        # Helper function to add value flags (int, string) ONLY if set by user
        def add_value_flag(setting_name, flag_name, value_type):
             if settings.has(setting_name): # Check if the setting exists
                value = settings.get(setting_name)
                if isinstance(value, value_type):
                    cmd.append('--{}={}'.format(flag_name, value))
                else:
                     log_error("Invalid type for setting '{}'. Expected {}.".format(setting_name, value_type.__name__))

        # == Indentation and Spacing ==
        add_value_flag('verible_indentation_spaces', 'indentation_spaces', int)
        add_value_flag('verible_wrap_spaces', 'wrap_spaces', int)

        # == Line Wrapping ==
        add_value_flag('verible_column_limit', 'column_limit', int)
        add_bool_flag('verible_wrap_end_else_clauses', 'wrap_end_else_clauses')
        add_bool_flag('verible_try_wrap_long_lines', 'try_wrap_long_lines')
        add_value_flag('verible_line_break_penalty', 'line_break_penalty', int)
        add_value_flag('verible_over_column_limit_penalty', 'over_column_limit_penalty', int)

        # == Alignment ==
        add_value_flag('verible_assignment_statement_alignment', 'assignment_statement_alignment', str)
        add_value_flag('verible_case_items_alignment', 'case_items_alignment', str)
        add_value_flag('verible_class_member_variable_alignment', 'class_member_variable_alignment', str)
        add_value_flag('verible_distribution_items_alignment', 'distribution_items_alignment', str)
        add_value_flag('verible_enum_assignment_statement_alignment', 'enum_assignment_statement_alignment', str)
        add_value_flag('verible_formal_parameters_alignment', 'formal_parameters_alignment', str)
        add_value_flag('verible_formal_parameters_indentation', 'formal_parameters_indentation', str)
        add_value_flag('verible_module_net_variable_alignment', 'module_net_variable_alignment', str)
        add_value_flag('verible_named_parameter_alignment', 'named_parameter_alignment', str)
        add_value_flag('verible_named_parameter_indentation', 'named_parameter_indentation', str)
        add_value_flag('verible_named_port_alignment', 'named_port_alignment', str)
        add_value_flag('verible_named_port_indentation', 'named_port_indentation', str)
        add_value_flag('verible_port_declarations_alignment', 'port_declarations_alignment', str)
        add_value_flag('verible_port_declarations_indentation', 'port_declarations_indentation', str)
        add_bool_flag('verible_port_declarations_right_align_packed_dimensions', 'port_declarations_right_align_packed_dimensions')
        add_bool_flag('verible_port_declarations_right_align_unpacked_dimensions', 'port_declarations_right_align_unpacked_dimensions')
        add_value_flag('verible_struct_union_members_alignment', 'struct_union_members_alignment', str)

        # == Other Style Options ==
        add_bool_flag('verible_compact_indexing_and_selections', 'compact_indexing_and_selections')
        add_bool_flag('verible_expand_coverpoints', 'expand_coverpoints')
        add_bool_flag('verible_show_equally_optimal_wrappings', 'show_equally_optimal_wrappings')

        # Add the stdin argument
        cmd.append('-')

        # Get current content
        region = sublime.Region(0, view.size())
        original_content = view.substr(region)
        if not original_content.strip():
            log_info("Skipping empty file.")
            return

        try:
            log_info("Running verible command: {}".format(" ".join(cmd)))
            startupinfo = None
            if os.name == 'nt': # For Windows, hide the console window
                startupinfo = subprocess.STARTUPINFO()
                startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                startupinfo.wShowWindow = subprocess.SW_HIDE

            process = subprocess.Popen(
                cmd, # Use the constructed command list
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                startupinfo=startupinfo,
                shell=False
            )

            stdout, stderr = process.communicate(input=original_content.encode('utf-8'))

            if process.returncode == 0:
                # Decode output and normalize line endings to LF (\n)
                formatted_content = stdout.decode('utf-8').replace('\r\n', '\n')
                if formatted_content != original_content:
                    log_info("Applying formatting.")
                    # Replace content using a text command for undo support
                    view.run_command('replace_view_content_format_verilog', {'content': formatted_content})
                    sublime.status_message("Formatted with Verible")
                else:
                    log_info("No formatting changes needed.")
                    sublime.status_message("Verible: No changes")
            else:
                error_message = stderr.decode('utf-8').strip()
                log_error("verible-verilog-format failed (code {}): {}".format(process.returncode, error_message))
                sublime.status_message("Verible Error: {}".format(error_message[:100])) # Show brief error in status bar

        except FileNotFoundError:
            # This exception might still occur if path expansion fails or points to non-existent file
            log_error("Executable not found at '{}'. Check 'verible_executable_path' setting (expanded to: '{}').".format(executable_path, expanded_path))
            sublime.status_message("FormatVerilog Error: Verible not found")
        except Exception as e:
            log_error("Error running verible-verilog-format: {}".format(e))
            sublime.status_message("FormatVerilog Error: {}".format(e))

class ReplaceViewContentFormatVerilogCommand(sublime_plugin.TextCommand):
    """Helper command to replace view content, enabling undo."""
    def run(self, edit, content=''):
        self.view.replace(edit, sublime.Region(0, self.view.size()), content) 