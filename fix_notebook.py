import json

file_path = "tutorial_QUBO.ipynb"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

target = '''        "shots = 5000  # Number of samples used\\n",
        "dev = qp.device(\\"default.qubit\\")\\n",
        "\\n",
        "\\n",
        "@qp.set_shots(shots)\\n",
        "@qp.qnode(dev)\\n",'''

replacement = '''        "shots = 5000  # Number of samples used\\n",
        "dev = qp.device(\\"default.qubit\\", shots=shots)\\n",
        "\\n",
        "\\n",
        "@qp.qnode(dev)\\n",'''

if target in content:
    content = content.replace(target, replacement)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Notebook updated successfully.")
else:
    print("Target string not found.")
