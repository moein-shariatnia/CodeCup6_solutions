import pandas as pd

df = pd.read_csv("supermarket.csv")

nunique_products = df['Product'].nunique()
df['Date'] = pd.to_datetime(df['Date'], format="%Y-%m-%d")

purchase_per_day = df.groupby([df['Date'].dt.date])['Product'].count().mean()
purchase_per_day = round(purchase_per_day, 2)

least_4_products = df['Product'].value_counts().index[-4:].tolist()


tmp = df.groupby([df['Date'].dt.date, df['Customer Id']])['Product'].unique().reset_index()
tmp = tmp.reset_index()
tmp['Date'] = pd.to_datetime(tmp['Date'], format="%Y-%m-%d")

tmp = tmp[tmp['Date'].dt.year >= 2020].reset_index(drop=True)
top_5_customers = tmp['Customer Id'].value_counts().index[:5].tolist()


dow = df.groupby([df['Date'].dt.dayofweek])["Product"].count().sort_values().index[-1]
mapping = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday"
}
most_sale_dow = mapping[dow]


baskets = df.groupby([df['Date'].dt.date, df['Customer Id']])['Product'].unique().reset_index()
pro2support = {}
for pro in df['Product'].unique():
    support = baskets['Product'].map(lambda x: pro in x).sum() / len(baskets)
    pro2support[pro] = support

sorted_products = sorted(pro2support.keys(), key=lambda x: pro2support[x], reverse=True)
top_5_products = sorted_products[:5]


with open("/content/output.txt", "w") as file:
    file.write(f"{nunique_products}\n")
    file.write(f"{purchase_per_day}\n")
    file.write(f"{','.join(least_4_products)}\n")
    file.write(f"{','.join(top_5_customers)}\n")
    file.write(f"{most_sale_dow}\n")
    file.write(f"{','.join(top_5_products)}\n")
    file.write("-1")






