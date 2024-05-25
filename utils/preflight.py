"""
Performs basic preflight checks to give some quick metrics on the dataframe
you feed into the preflichtchecks main function.
"""

import pandas as pd

def count_outliers(q1, q3, series):
    """
        Counts the amount of outliers which are in a given column.
    """
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    series_reset = series.reset_index(drop=True)  # Reset index to avoid comparison issues
    return series_reset[(series_reset <= lower_bound) | (series_reset >= upper_bound)].count


def preflightchecks(df):
    """
        main function, should be called with a pandas dataframe and will perform all the checks.
        it returns a new dataframe with all the results of your checks.
    """
    checks_data = []
    for column in df.columns:
        data_type = df[column].dtype
        nan_count = df[column].isna().sum()
        unique_count = df[column].nunique()
        suited_as_primary_key = unique_count == len(df[column])
        mode = df[column].mode()[0]
        max_value = None
        min_value = None
        ranges = None
        average = None
        median = None
        stdev = None
        variance = None
        skewed = None
        kurtosis = None
        q25 = None
        q50 = None
        q75 = None
        lows_oob = None
        highs_oob = None
        if pd.api.types.is_numeric_dtype(df[column]):
            max_value = df[column].max()
            min_value = df[column].min()
            ranges = max_value - min_value
            average = df[column].mean()
            median = df[column].median()
            stdev = df[column].std()
            variance = df[column].var()
            skewed = df[column].skew()
            kurtosis = df[column].kurtosis()
            q25 = df[column].quantile([0.25])
            q50 = df[column].quantile([0.5])
            q75 = df[column].quantile([0.75])
            # lows_oob, highs_oob = (
            #     count_outliers(q25, q75, df[column])
            # )
        

        # Append the results to the checks_data list
        checks_data.append(
            {
                'Column Name': column, 
                'Data Type': data_type, 
                'NaN Count': nan_count, 
                'Unique Count': unique_count, 
                'suitable PK': suited_as_primary_key,
                'Max': max_value,
                'Min': min_value, 
                'Range': ranges,
                'Avg': average, 
                'Median': median, 
                'Mode': mode,
                'Standard Dev': stdev,
                'Variance': variance,
                'Skewedness': skewed, 
                'Kurtosis': kurtosis, 
                'Quant_25': q25, 
                'Quant_50': q50,
                'Quant_75': q75, 
                'Out of bound lows': lows_oob, 
                'Out of bound highs': highs_oob
                
            })

    # Create a new DataFrame from the checks_data list
    checks_df = pd.DataFrame(checks_data)

    return checks_df