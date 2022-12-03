import pandas as pd


def load_and_process(data):
    """
    Adding new columns to the data set for ease of use in analysis and convert date to appropriate format

        Parameters
    ----------
    data : pandas DataFrame

    Returns
    -------
    pandas DataFrame
        Cleaned dataset
    """

    df = data.copy()

    df['InvoiceDate'] = pd.to_datetime(df.InvoiceDate, format='%m/%d/%Y %H:%M')

    df["TotalCost"] = df["Quantity"] * df["UnitPrice"]

    return df
