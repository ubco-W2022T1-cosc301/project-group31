import pandas as pd


def load_and_process(data):
    """
    Adding new columns to the data set for ease of use in analysis

        Parameters
    ----------
    data : pandas DataFrame

    Returns
    -------
    pandas DataFrame
        Cleaned dataset
    """

    df = data.copy()
    # transform InvoiceDate into date time format
    df['InvoiceDate'] = pd.to_datetime(df.InvoiceDate, format='%m/%d/%Y %H:%M')

    # create column Total cost of order
    df["TotalCost"] = df["Quantity"] * df["UnitPrice"]
    """
    df.insert(loc=2, column='year_month', value=df['InvoiceDate'].map(lambda x: 100*x.year + x.month))
    df.insert(loc=3, column='month', value=df.InvoiceDate.dt.month)
    # +1 to make Monday=1.....until Sunday=7
    df.insert(loc=4, column='day', value=(df.InvoiceDate.dt.dayofweek)+1)
    df.insert(loc=5, column='hour', value=df.InvoiceDate.dt.hour)
    """
    return df
