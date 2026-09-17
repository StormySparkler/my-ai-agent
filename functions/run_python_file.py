import os
import subprocess


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, file_path))
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
    result_list = []

    try:
        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        elif not os.path.isfile(target_dir):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        elif not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_dir]
        if args:
            command.extend(args)

        result = subprocess.run(
            command,
            cwd = working_dir_abs,
            capture_output = True,
            text = True,
            timeout = 30
        )
        if result.returncode != 0:
            result_list.append(f"Process exited with code {result.returncode}")
        if not result.stdout and not result.stderr:
            result_list.append("No output produced")

        if result.stdout:
            result_list.append(f"STDOUT: {result.stdout}")
        if result.stderr:
            result_list.append(f"STDERR: {result.stderr}")

        return "\n".join(result_list)

    except Exception as e:
        return f"Error: executing Python file: {e}"