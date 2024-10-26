# NOTE i had to run mass replace \ with \\ on paths. 
import json
import matplotlib.pyplot as plt
import mplcursors   

data = """
 Your msbuild 'PerformanceSummary' output
"""

# Initialize an empty list to hold parsed data
parsed_data = []

# Split the data into lines
lines = data.strip().split('\n')

# Iterate over each line
for line in lines:
    # Strip leading/trailing whitespace and split by whitespace
    parts = line.strip().split()
    
    # Check if line starts with a time in ms followed by C:\ directory
    if len(parts) >= 4 and parts[1] == 'ms' and parts[2].startswith('C:\\'):
        duration = int(parts[0])  # First part is the duration in ms
        path = parts[2]  # Path starts from the 3rd part
        calls = int(parts[-2])  # Last number before 'calls'
        proj = path.split('\\')[-1]  # Get the last part after splitting by '\'
         
        # Add parsed data to the list
        parsed_data.append({
            "Duration (ms)": duration,
            "Path": path,
            "Calls": calls,
            "Project":proj
        })

# Convert parsed data to JSON
json_data = json.dumps(parsed_data, indent=2)

# Print JSON data
# print(json_data)

json_data = json.dumps(parsed_data, indent=2)
#All data
# parsed_data = json.loads(json_data)

# Slice the last 50 entries
parsed_data = parsed_data[-50:]


tasks = [entry['Project'] for entry in parsed_data]
durations = [entry['Duration (ms)'] for entry in parsed_data]

# Plotting
plt.figure(figsize=(12, 8))
scatter = plt.scatter(durations, tasks, c='blue')

# Adding interactive cursor
cursor = mplcursors.cursor(scatter, hover=True)
cursor.connect("add", lambda sel: sel.annotation.set_text(f'Duration: {durations[sel.index]} ms\nCalls: {parsed_data[sel.index]["Calls"]}'))

# Customize the annotation (tooltip) appearance
def customize_annotation(sel):
    sel.annotation.get_bbox_patch().set_facecolor('lightblue')  # Set background color
    sel.annotation.get_bbox_patch().set_edgecolor('black')      # Set border color
    sel.annotation.get_bbox_patch().set_boxstyle("round,pad=0.3")  # Optional: rounded corners

cursor.connect("add", customize_annotation)

plt.xlabel('Duration (ms)')
plt.ylabel('Project')
plt.title('Build Task Durations')
plt.grid(True)
plt.tight_layout()
plt.show()


