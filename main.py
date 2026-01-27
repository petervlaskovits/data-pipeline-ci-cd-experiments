def clean_column(column: list[str]) -> tuple[list[float], list[str], list[str]]:
    """
    Cleans a column consisting of the hourly salary, and extracts currency, wage, and the salary information into a tuple.
    """
    currency = ["USD" if row[0] == "$" else None for row in column]
    wage = [float(row.strip("$/hr").strip("per hour")) for row in column]
    salary_info = ["hourly" if row[row.find("h")::] == "hr" or "hour" else None for row in column]
    return (wage, currency, salary_info)