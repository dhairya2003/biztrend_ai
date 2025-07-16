def generate_summary(df):
    total_sales = df["Sales"].sum()
    avg_sales = df["Sales"].mean()
    max_sale = df["Sales"].max()
    min_sale = df["Sales"].min()
    return {
        "Total Sales": f"₹{total_sales:.2f}",
        "Average Sales": f"₹{avg_sales:.2f}",
        "Max Sale": f"₹{max_sale:.2f}",
        "Min Sale": f"₹{min_sale:.2f}",
    }
