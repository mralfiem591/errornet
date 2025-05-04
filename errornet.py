import sys
import os
import traceback
from rich.console import Console

class ErrorNet:
    """ErrorNet: Error reporting of the future."""
    def __init__(self, print_title: bool = False, report_to: str | bool = False, error_log: bool = True):
        """Initialize the ErrorNet class.
        
        Args:
            print_title (bool): Whether to print the title of ErrorNet.
            report_to (str | bool): The URL to report errors to. If False, no URL is provided.
            error_log (bool): Whether to log errors to a file.
        """
        self.console = Console()
        if print_title:
            self.console.print("ErrorNet: Error reporting of the future.\n", style="bold blue")
        self.report_to = report_to
        self.error_log = error_log

    def handle_exception(self, exc_type, exc_value, exc_traceback):
        """Custom exception handler.
        Use with `sys.excepthook` to handle uncaught exceptions."""
        if issubclass(exc_type, KeyboardInterrupt):
            # Allow Ctrl+C to exit the program without restarting
            sys.__excepthook__(exc_type, exc_value, exc_traceback)
            return

        if self.error_log:
            if os.path.exists(os.path.join(os.path.dirname(__file__), "error_log.txt")):
                # If the error log file already exists, delete it before creating a new one
                os.remove(os.path.join(os.path.dirname(__file__), "error_log.txt"))
            # Log the error details
            with open(os.path.join(os.path.dirname(__file__), "error_log.txt"), "a") as log_file:
                log_file.write("Uncaught exception:\n\n")
                traceback.print_exception(exc_type, exc_value, exc_traceback, file=log_file)
                if self.report_to:
                    log_file.write(f"\nPlease report this error to the developers of the program, at {self.report_to}.")
                else:
                    log_file.write("\nPlease report this error to the developers of the program.")
                log_file.write("\n\n\nHandled by ErrorNet: Error reporting of the future.")

        self.console.print(f"An error occurred: {exc_value}.", style="bold red")
        if self.error_log:
            self.console.print(f"The error has been logged to '{os.path.join(os.path.dirname(__file__), 'error_log.txt')}'.", style="yellow")
        if self.report_to:
            self.console.print(f"Please report this error to the developers of the program, at {self.report_to}.", style="yellow")
        else:
            self.console.print("Please report this error to the developers of the program.", style="yellow")