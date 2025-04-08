from data_loader import load_and_filter_clinvar

df = load_and_filter_clinvar("/Users/jamieannemortel/Downloads/variant_summary.txt")
print(df.head(5))
