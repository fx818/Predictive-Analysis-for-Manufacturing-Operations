# Generate synthetic data similar to the earlier example
num_rows = 100
machine_ids = [f'M{i}' for i in range(1, 11)]
temperature = np.random.uniform(30, 100, num_rows)
run_time = np.random.uniform(0, 12, num_rows)
downtime_flag = np.random.choice([0, 1], num_rows, p=[0.9, 0.1])
machine_ids_col = np.random.choice(machine_ids, num_rows)

# Create the DataFrame
data = pd.DataFrame({
    'Machine_ID': machine_ids_col,
    'Temperature': temperature,
    'Run_Time': run_time,
    'Downtime_Flag': downtime_flag
})

# Save to CSV
csv_path = "manufacturing_data.csv"
data.to_csv(csv_path, index=False)
csv_path
