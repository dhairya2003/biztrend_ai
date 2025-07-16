import matplotlib.pyplot as plt
import pandas as pd

def plot_monthly_sales(df):
    df['Date'] = pd.to_datetime(df['Date'])
    monthly = df.groupby(df['Date'].dt.to_period("M")).sum(numeric_only=True)
    monthly.index = monthly.index.astype(str)
    
    fig, ax = plt.subplots()
    monthly["Sales"].plot(kind='line', marker='o', ax=ax)
    ax.set_title("Monthly Sales Trend")
    ax.set_ylabel("Sales (₹)")
    ax.set_xlabel("Month")
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig
