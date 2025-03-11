import pathway as pw

# Define the schema of your data (Optional)
class InputSchema(pw.Schema):
  value: int

# Connect to your data using connectors
input_table = pw.io.csv.read(
  "./input/",
  schema=InputSchema
)

#Define your operations on the data
filtered_table = input_table.filter(input_table.value>=0)
result_table = filtered_table.reduce(
  sum_value = pw.reducers.sum(filtered_table.value)
)

# Load your results to external systems
pw.io.jsonlines.write(result_table, "output.jsonl")

# Run the computation
pw.run()