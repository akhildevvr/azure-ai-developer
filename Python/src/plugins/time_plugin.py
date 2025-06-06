from datetime import datetime
from semantic_kernel.functions import kernel_function

class TimePlugin:
    @kernel_function
    def get_current_datetime(self) -> str:
        """Returns the current date and time as a string."""
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    @kernel_function
    def get_year(self, date_str: str) -> int:
        """Returns the year for a given date string (YYYY-MM-DD)."""
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        return dt.year

    @kernel_function
    def get_month(self, date_str: str) -> int:
        """Returns the month for a given date string (YYYY-MM-DD)."""
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        return dt.month
    @kernel_function
    def get_day_of_week(self, date_str: str) -> str:
        """Returns the day of the week for a given date string (YYYY-MM-DD)."""
        dt = datetime.strptime(date_str, "%Y-%m-%d")
        return dt.strftime("%A")