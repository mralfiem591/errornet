# ErrorNet

**ErrorNet** is a Python-based error-handling utility designed to simplify error reporting and logging in your Python applications. With ErrorNet, you can capture uncaught exceptions, log detailed error information, and provide users with clear instructions for reporting issues.

---

## Features

- **Custom Exception Handling**: Automatically captures uncaught exceptions and processes them.
- **Error Logging**: Logs detailed error information, including stack traces, to a file (`error_log.txt`).
- **Rich Console Output**: Uses the `rich` library to display error messages in a visually appealing format.
- **Developer Reporting**: Optionally includes a developer contact or reporting address in the error log and console output.
- **Graceful Exit**: Allows `KeyboardInterrupt` (e.g., Ctrl+C) to exit the program without triggering the error handler.

---

## Installation

1. Clone or download the repository containing `ErrorNet`.
2. Ensure you have Python 3.10 or later installed (for type hinting compatibility).
3. Install the required dependency:

```bash
pip install rich
```

---

## Usage

### Basic Setup

To use ErrorNet in your project, import it and set it up as the global exception handler:

```python
from errornet import ErrorNet
import sys

# Initialize ErrorNet
error_handler = ErrorNet(print_title=True, report_to="GitHub: mralfiem591/errornet", error_log=True)

# Set the custom exception handler
sys.excepthook = error_handler.handle_exception
```

### Parameters

When initializing the `ErrorNet` class, you can customize its behavior with the following parameters:

| Parameter      | Type          | Default Value | Description                                                                 |
|----------------|---------------|---------------|-----------------------------------------------------------------------------|
| `print_title`  | `bool`        | `False`       | If `True`, prints a title banner when initialized.                         |
| `report_to`    | `str` or `bool` | `False`       | A string specifying the developer's contact (e.g., email). If `False`, no contact is included. |
| `error_log`    | `bool`        | `True`        | If `True`, logs error details to `error_log.txt`.                          |

---

### Example

Here’s an example of how to use ErrorNet in a script:

```python
# example.py
from errornet import ErrorNet
import sys

# Initialize ErrorNet

error_handler = ErrorNet(print_title=True, report_to="support@example.com", error_log=True)

# Set the custom exception handler

sys.excepthook = error_handler.handle_exception

# Simulate an error

def main():
    print("Running the script...")
    raise ValueError("Something went wrong!")

if __name__ == "__main__":
    main()
```

When an uncaught exception occurs, ErrorNet will:

1. Log the error details to `error_log.txt`.
2. Display the error message in the console with rich formatting.
3. Provide instructions for reporting the error to the developer.

---

## Output

### Console Output

When an error occurs, the console will display something like this:

```plaintext
An error occurred: Something went wrong!
The error has been logged to 'path/to/error_log.txt'.
Please report this error to the developers of the program, at <support@example.com>.
```

### Error Log (`error_log.txt`)

The error log will contain detailed information about the exception:

```plaintext
Uncaught exception:

Traceback (most recent call last):
  File "example.py", line 10, in <module>
    raise ValueError("Something went wrong!")
ValueError: Something went wrong!

Please report this error to the developers of the program, at support@example.com.

Handled by ErrorNet: Error reporting of the future.
```

---

## Notes

- **Error Log Overwriting**: If an error log already exists, it will be deleted and replaced with the latest error details.
- **KeyboardInterrupt Handling**: Pressing `Ctrl+C` will exit the program without triggering the error handler.
- **Rich Library**: Ensure the `rich` library is installed for enhanced console output.

---

## Future Enhancements

- Add support for sending error reports via email or HTTP requests.
- Implement a retry mechanism for restarting the script after an error.
- Provide more customization options for error log formatting.

---

## License

This project is open-source and available under the MIT License.

---

## Acknowledgments

ErrorNet uses the [Rich](https://github.com/Textualize/rich) library for beautiful console output.
