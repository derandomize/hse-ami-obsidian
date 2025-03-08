import re
import os
import glob
import argparse

def extract_newcommands(preamble_file):
    """Extract newcommand definitions from preamble.sty, one per line."""
    commands = {}
    
    with open(preamble_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line.startswith('\\newcommand{'):
                # We'll parse this line character by character to ensure correct handling of braces
                i = len('\\newcommand{')
                
                # Extract the command name (including the backslash)
                cmd_start = i
                brace_count = 1  # We're already inside the first opening brace
                
                while i < len(line) and brace_count > 0:
                    if line[i] == '{':
                        brace_count += 1
                    elif line[i] == '}':
                        brace_count -= 1
                    i += 1
                
                if brace_count != 0 or cmd_start + 1 >= i - 1:
                    print(f"Warning: Malformed command definition in line: {line}")
                    continue
                
                # Extract just the command name without the braces
                full_cmd = line[cmd_start:i-1]
                if not full_cmd.startswith('\\'):
                    print(f"Warning: Command doesn't start with backslash in line: {line}")
                    continue
                
                # Remove the backslash for our internal dictionary
                cmd = full_cmd[1:]
                
                # Check if it has arguments with [1]
                has_arg = False
                if i < len(line) and line[i:].startswith('[1]'):
                    has_arg = True
                    i += 3  # Skip the [1]
                
                # Find the replacement text (everything in the last set of braces)
                while i < len(line) and line[i] != '{':
                    i += 1
                
                if i >= len(line):
                    print(f"Warning: No replacement text found in line: {line}")
                    continue
                
                # Extract the replacement text with all nested braces
                i += 1  # Skip the opening brace
                replacement_start = i
                brace_count = 1
                
                while i < len(line) and brace_count > 0:
                    if line[i] == '{':
                        brace_count += 1
                    elif line[i] == '}':
                        brace_count -= 1
                    i += 1
                
                if brace_count != 0:
                    print(f"Warning: Unbalanced braces in replacement text in line: {line}")
                    continue
                
                replacement = line[replacement_start:i-1]
                
                commands[cmd] = {
                    'replacement': replacement,
                    'args': 1 if has_arg else 0
                }
                
                print(f"Parsed command: \\{cmd} -> {replacement}")
    
    return commands

def replace_commands_in_latex(latex_content, commands):
    """Replace commands in LaTeX content, without using regex for the search part."""
    result = []
    i = 0
    
    while i < len(latex_content):
        # Looking for a backslash
        if latex_content[i] == '\\':
            # Try to match a command
            matched = False
            for cmd, info in commands.items():
                # Check if this position has our command
                if i + len(cmd) + 1 <= len(latex_content) and latex_content[i+1:i+1+len(cmd)] == cmd:
                    # Ensure it's a complete command (followed by non-letter or end of string)
                    if i+1+len(cmd) == len(latex_content) or not latex_content[i+1+len(cmd)].isalpha():
                        if info['args'] == 0:
                            # Zero-argument command
                            result.append(info['replacement'])
                            i += 1 + len(cmd)
                            matched = True
                            break
                        elif info['args'] == 1 and i+1+len(cmd) < len(latex_content) and latex_content[i+1+len(cmd)] == '{':
                            # One-argument command, extract the argument
                            arg_start = i+1+len(cmd)+1
                            brace_count = 1
                            arg_end = arg_start
                            
                            while arg_end < len(latex_content) and brace_count > 0:
                                if latex_content[arg_end] == '{':
                                    brace_count += 1
                                elif latex_content[arg_end] == '}':
                                    brace_count -= 1
                                arg_end += 1
                            
                            if brace_count == 0:
                                arg = latex_content[arg_start:arg_end-1]
                                replaced = info['replacement'].replace('#1', arg)
                                result.append(replaced)
                                i = arg_end
                                matched = True
                                break
            
            if not matched:
                result.append(latex_content[i])
                i += 1
        else:
            result.append(latex_content[i])
            i += 1
    
    return ''.join(result)

def process_markdown_file(file_path, commands):
    """Process a markdown file to replace LaTeX commands."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find and process all math blocks
    result = []
    i = 0
    
    while i < len(content):
        # Look for math delimiters
        if content[i:i+2] == '$$':  # Block math
            # Find the end of this block
            end = content.find('$$', i+2)
            if end != -1:
                # Process the LaTeX content inside
                latex_content = content[i+2:end]
                processed_latex = replace_commands_in_latex(latex_content, commands)
                result.append('$$' + processed_latex + '$$')
                i = end + 2
            else:
                # No end delimiter found, add as is
                result.append(content[i])
                i += 1
        elif content[i] == '$' and (i == 0 or content[i-1] != '$') and i+1 < len(content) and content[i+1] != '$':
            # Inline math - make sure it's not part of a block delimiter
            # Find the end of this inline math
            end = i + 1
            while end < len(content):
                if content[end] == '$' and (end+1 == len(content) or content[end+1] != '$'):
                    break
                end += 1
            
            if end < len(content):
                # Process the LaTeX content inside
                latex_content = content[i+1:end]
                processed_latex = replace_commands_in_latex(latex_content, commands)
                result.append('$' + processed_latex + '$')
                i = end + 1
            else:
                # No end delimiter found, add as is
                result.append(content[i])
                i += 1
        else:
            # Regular text
            result.append(content[i])
            i += 1
    
    updated_content = ''.join(result)
    
    # Write the updated content back to the file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(updated_content)

def main():
    parser = argparse.ArgumentParser(description='Replace LaTeX commands in Markdown files')
    parser.add_argument('--preamble', default='preamble.sty', help='Path to preamble.sty file')
    parser.add_argument('--directory', default='.', help='Directory containing Markdown files')
    parser.add_argument('--dry-run', action='store_true', help='Print changes without modifying files')
    args = parser.parse_args()
    
    # Extract newcommand definitions
    commands = extract_newcommands(args.preamble)
    print(f"Extracted {len(commands)} commands from {args.preamble}")
    if args.dry_run:
        print(f"Commands: {commands}")
    
    # Process all markdown files
    markdown_files = glob.glob(os.path.join(args.directory, '**/*.md'), recursive=True)
    print(f"Found {len(markdown_files)} Markdown files to process")
    
    for file_path in markdown_files:
        try:
            if args.dry_run:
                print(f"Would process: {file_path}")
            else:
                process_markdown_file(file_path, commands)
                print(f"Processed: {file_path}")
        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")
            import traceback
            traceback.print_exc()

if __name__ == '__main__':
    main()
