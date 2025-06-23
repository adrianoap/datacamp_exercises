
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def prepare_smartphone_data(file_path):
    """
    To prepare the smartphone data for visualization, a number
    of transformations will be applied after reading in the raw DataFrame
    to memory, including:
        - reducing the number of columns to only those needed for
        later analysis
        - removing records without a battery_capacity value
        - divide the price column by 100 to find the dollar amount

    :param file_path: the file path where the raw smartphone data is stored
    :return: a cleaned dataset having had the operations above applied to it
    """

    if os.path.exists(file_path):
        print("path exists!")
        raw_data = pd.read_csv(file_path)
        print(raw_data.head())  # TODO: Remove after checking out dataset
    else:
        raise Exception(f"File containing smartphone data not found at "
                        "path {file_path}")

    feature_set = [
        "brand_name",
        "os",
        "price",
        "avg_rating",
        "processor_speed",
        "battery_capacity",
        "screen_size"
    ]
    trimmed_data = raw_data.loc[:, feature_set]

    # Remove records without a battery_capacity value
    reduced_data = trimmed_data.dropna(subset=["battery_capacity", "os"])

    # Divide the price column by 100 to find the dollar amount
    reduced_data["price"] = reduced_data["price"] / 100

    return reduced_data


# Call the function
cleaned_data = prepare_smartphone_data("./data/smartphones.csv")

print(cleaned_data)
