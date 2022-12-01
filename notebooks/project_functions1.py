import pandas as pd
import datetime as dt
import seaborn as sns
from lifetimes.plotting import plot_period_transactions
import matplotlib.pyplot as plt
from lifetimes import BetaGeoFitter, GammaGammaFitter
from plotly.offline import  init_notebook_mode
palette = 'Set2'

def outliers(data, variable, q1 = 0.25, q3 = 0.75):
    """
    Remove outliers from dataset based on q1 and q2

        Parameters
    ----------
    data : pandas DataFrame
        dataframe to clean

    variable: column of pandas Dataframe
        which column to clean

    q1: int
        first quartile

    q2: int
        second quartile

    Returns
    -------
    pandas DataFrame
        Cleaned dataset
    """
    df = data.copy()
    quartile1 = df[variable].quantile(q1)
    quartile3 = df[variable].quantile(q3)
    iqr = quartile3 - quartile1

    up_limit = quartile3 + 1.5 * iqr
    low_limit = quartile1 - 1.5 * iqr
    df.loc[(df[variable] < low_limit), variable] = low_limit
    df.loc[(df[variable] > up_limit), variable] = up_limit

    return df


def load_and_process(data):
    """
    Remove cancelled Orders & Quantity from dataset, calculate Total Price, Replace Outliers

    Parameters
    ----------
    data : pandas DataFrame
        dataframe to clean

    Returns
    -------
    pandas DataFrame
        Cleaned dataset
"""
    df = data.copy()

    df = df.dropna()
    #Dealing with cancelled orders
    df = df[~df['InvoiceNo'].str.contains('C', na = False)]
    df = df[df['Quantity'] > 0]


    #Replacing Outliers
    outliers(df, "Quantity", q1 = 0.01, q3 = 0.99)
    outliers(df, "UnitPrice", q1 = 0.01, q3 = 0.99)

    #Calculating Total Price
    df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

    return df