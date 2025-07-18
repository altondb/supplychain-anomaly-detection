# Load and prepare data
df = load_and_prepare_data('../data/realistic_kraljic_dataset.csv')

print(f"Data shape after preparation: {df.shape}")
print("\nColumns: ")
print([col for col in df.columns if col not in pd.read_csv('../data/realistic_kraljic_dataset.csv').columns][:10])
