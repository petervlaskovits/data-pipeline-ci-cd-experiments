import pandas as pd

test_column_1 = pd.Series([
    "$10/hr",
    "$15 per hour",
    "$12/hr"
])

def clean_column(column: pd.Series) -> pd.DataFrame:
    """
    Cleans a Series consisting of the hourly salary, then uses feature engineering to add relevant features into a DataFrame.
    """
    temp_column = column
    # Regex Patterns
    hr_pattern = r"\$\d+\/hr" # "$10/hr"
    per_hour_pattern = r"\$\d+ per hour" # "$10 per hour"

    hr = (
        temp_column.str
        .contains(hr_pattern, regex=True)
    )

    per_hour = (
        test_column_1.str
        .contains(per_hour_pattern, regex=True)
    )

    currency = temp_column.str.get(0)
    currency = currency.replace("$", "USD").rename("Currency")

    salary_info = test_column_1.replace(
    regex=[
        hr_pattern, # Match cases where the string is like "$10/hr"
        per_hour_pattern # Match cases where the string is like "$10 per hour"
    ], 
    value="Hourly")

    temp_column = temp_column.str.strip("$")
    temp_column[hr == True] = temp_column.str.strip("/hr")

    temp_column[per_hour == True] = temp_column.str.strip("per hour")
    temp_column = temp_column.astype("int64")

    new_df = pd.DataFrame({
        "original_data": column,
        "salary": temp_column,
        "currency": currency,
        "salary_info": salary_info,
        "annual_salary_pretax": temp_column * 8 * 5 * 4 * 12
    })

    return new_df