import json
import matplotlib.pyplot as plt
import mplcursors   

data = """
71 ms  Delete                                   499 calls
86 ms  Message                                  774 calls
92 ms  ProcessFrameworkReferences                10 calls
94 ms  ResolveComReference                        1 calls
107 ms  WriteLinesToFile                         350 calls
122 ms  ResolvePackageAssets                      19 calls
132 ms  GetReferenceNearestTargetFrameworkTask   435 calls
132 ms  Hash                                     346 calls
156 ms  GenerateResource                          16 calls
190 ms  AssignTargetPath                         1799 calls
207 ms  GenerateBindingRedirects                  37 calls
247 ms  Touch                                    192 calls
274 ms  CreateItem                                15 calls
276 ms  GenerateDepsFile                           3 calls
301 ms  RemoveDuplicates                         512 calls
351 ms  ResolvePackageFileConflicts              256 calls
411 ms  AssignProjectConfiguration               256 calls
448 ms  ReadLinesFromFile                        256 calls
596 ms  FindUnderPath                            1280 calls
691 ms  BundlerMinifier.BundlerBuildTask           2 calls
1465 ms  RtCli                                      1 calls
3115 ms  CallTarget                               752 calls
12461 ms  VsTsc                                    6 calls
16455 ms  Copy                                     810 calls
20887 ms  Fsc                                      14 calls
24789 ms  ResolveAssemblyReference               256 calls
71946 ms  Csc                                    180 calls
125498 ms  Exec                                   152 calls
323213 ms  AspNetCompiler                           4 calls
952764 ms  MSBuild                                1647 calls
"""
lines = data.strip().split('\n')
parsed_data = []

for line in lines:
    parts = line.split()
    duration = int(parts[0])
    calls = int(parts[-2])
    # Capture task name by excluding the first number and last two items
    task = " ".join(parts[2:-2])
    parsed_data.append({"Task": task, "Duration (ms)": duration, "Calls": calls})

json_data = json.dumps(parsed_data, indent=2)
parsed_data = json.loads(json_data)

tasks = [entry['Task'] for entry in parsed_data]
durations = [entry['Duration (ms)'] for entry in parsed_data]

# Plotting
plt.figure(figsize=(12, 8))
scatter = plt.scatter(durations, tasks, c='blue')

# Adding interactive cursor
cursor = mplcursors.cursor(scatter, hover=True)
cursor.connect("add", lambda sel: sel.annotation.set_text(f'Duration: {durations[sel.index]} ms'))

# Customize the annotation (tooltip) appearance
def customize_annotation(sel):
    sel.annotation.get_bbox_patch().set_facecolor('lightblue')  # Set background color
    sel.annotation.get_bbox_patch().set_edgecolor('black')      # Set border color
    sel.annotation.get_bbox_patch().set_boxstyle("round,pad=0.3")  # Optional: rounded corners

cursor.connect("add", customize_annotation)

plt.xlabel('Duration (ms)')
plt.ylabel('Task')
plt.title('Build Task Durations')
plt.grid(True)
plt.tight_layout()
plt.show()