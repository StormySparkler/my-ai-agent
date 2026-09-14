import os


def get_files_info(working_directory: str, directory: str = ".") -> str:

    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    
    try:
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        elif not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        lines = []
        names = os.listdir(target_dir)

        for name in names:
            full_path = os.path.join(target_dir, name)
            line = f"- {name}: file_size={os.path.getsize(full_path)} bytes, is_dir={os.path.isdir(full_path)}"
            lines.append(line)
        return "\n".join(lines)
    
    except Exception as e:
        return f"Error: {e}"