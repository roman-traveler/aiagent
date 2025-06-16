from functions.get_files_info import get_files_info, get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def test():
    # Additional test cases for run_python_file

    print("Running 'main.py' in 'calculator':")
    result = run_python_file("calculator", "main.py")
    print(result)

    print("Running 'tests.py' in 'calculator':")
    result = run_python_file("calculator", "tests.py")
    print(result)

    print("Running '../main.py' in 'calculator' (should error):")
    result = run_python_file("calculator", "../main.py")
    print(result)

    print("Running 'nonexistent.py' in 'calculator' (should error):")
    result = run_python_file("calculator", "nonexistent.py")
    print(result)


if __name__ == "__main__":
    test()