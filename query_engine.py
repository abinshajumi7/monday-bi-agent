def pipeline_summary(df):

    total_deals = len(df)

    if "Value" in df.columns:
        total_value = df["Value"].fillna(0).astype(float).sum()
    else:
        total_value = 0

    return f"Total deals: {total_deals}, Total pipeline value: {total_value}"