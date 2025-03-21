### 1. **Generating a DNA Sequence**
A simple **DNA strand** is created with base pairs:
```python
def generate_dna_sequence():
    return ["A-T", "C-G", "G-C", "T-A", "A-T", "G-C", "C-G", "T-A"]
```
- This function returns a **list of strings**, where each string represents a base pair.
- The format follows the Watson-Crick base pairing rule: `A-T` and `C-G`.

### 2. **Introducing a Mutation**
The `introduce_mutation()` function modifies a single base in the sequence while keeping the complementary pair.

#### **Function Breakdown:**
```python
def introduce_mutation(sequence, index, new_base):
    original_sequence = sequence[:]
    original_pair = sequence[index]
    original_base, pair_base = original_pair.split('-')
    mutated_pair = f"{new_base}-{pair_base}"
    sequence[index] = mutated_pair
    return original_sequence, sequence, {"original": original_pair, "mutated": mutated_pair, "position": index}
```
- **Takes**: A DNA sequence, a mutation index, and the new base.
- **Splits** the original base pair (`A-T` → `A` and `T`).
- **Replaces** the base at the specified index while keeping the complementary base unchanged.
- **Returns**:
  1. The **original sequence** (before mutation).
  2. The **mutated sequence** (after mutation).
  3. A **dictionary** storing mutation details.

#### **Example Output:**
```python
{
    "original": "T-A",
    "mutated": "G-A",
    "position": 3
}
```

---

### 3. **Creating an SVG File**
The `create_svg()` function uses **svgwrite** to generate a **scalable vector graphics (SVG) file** for DNA visualization.

#### **Function Breakdown:**
```python
def create_svg(original_sequence, mutated_sequence, mutation_info):
    dwg = svgwrite.Drawing("dna_mutation.svg", profile='tiny', size=(500, 500))
    
    x, y = 50, 60
    dwg.add(dwg.text("Original DNA:", insert=(x, y - 20), fill="black", font_size="12px"))
    for i, pair in enumerate(original_sequence):
        dwg.add(dwg.text(pair, insert=(x, y), fill="black", font_size="12px"))
        y += 20
    
    y += 40  # Space between original and mutated
    dwg.add(dwg.text("Mutated DNA:", insert=(x, y - 20), fill="black", font_size="12px"))
    for i, pair in enumerate(mutated_sequence):
        color = "red" if i == mutation_info['position'] else "black"
        dwg.add(dwg.text(pair, insert=(x, y), fill=color, font_size="12px"))
        y += 20
    
    dwg.save()
```

- **Uses `svgwrite.Drawing`** to create a 500x500 pixel canvas.
- **Adds text elements** for DNA sequences.
- **Mutations are colored red** for easy identification.
- **Output File:** `dna_mutation.svg`.

#### **Why SVG?**
- **Scalable** without losing quality.
- **Editable** using software like Inkscape or a web browser.

---

### 4. **Storing Data in JSON**
The `create_json()` function saves mutation data in a structured format.

#### **Function Breakdown:**
```python
def create_json(original_sequence, mutated_sequence, mutation_info):
    data = {
        "original_sequence": original_sequence,
        "mutated_sequence": mutated_sequence,
        "mutation": mutation_info
    }
    with open("dna_mutation.json", "w") as f:
        json.dump(data, f, indent=4)
```
- **Creates a dictionary** containing the sequences and mutation details.
- **Writes the data to a JSON file** (`dna_mutation.json`).
- **Uses `json.dump()`** to store the information in an easy-to-read format.

#### **Example JSON Output:**
```json
{
    "original_sequence": ["A-T", "C-G", "G-C", "T-A", "A-T", "G-C", "C-G", "T-A"],
    "mutated_sequence": ["A-T", "C-G", "G-C", "G-A", "A-T", "G-C", "C-G", "T-A"],
    "mutation": {
        "original": "T-A",
        "mutated": "G-A",
        "position": 3
    }
}
```

---

### 5. **Visualizing DNA with OpenCV**
The `visualize_dna()` function uses OpenCV to display the sequences in a pop-up window.

#### **Key Features:**
- Displays **original and mutated sequences**.
- **Mutated base is shown in red**.
- Uses a **600x500 pixel canvas**.

#### **Code Snippet:**
```python
def visualize_dna(original_sequence, mutated_sequence, mutation_info):
    img = np.ones((600, 500, 3), dtype=np.uint8) * 255
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    y = 60
    cv2.putText(img, "Original DNA:", (50, y - 10), font, 0.6, (0, 0, 0), 2, cv2.LINE_AA)
    for i, pair in enumerate(original_sequence):
        cv2.putText(img, pair, (50, y), font, 0.6, (0, 0, 0), 2, cv2.LINE_AA)
        y += 25
    
    y += 40
    cv2.putText(img, "Mutated DNA:", (50, y - 10), font, 0.6, (0, 0, 0), 2, cv2.LINE_AA)
    for i, pair in enumerate(mutated_sequence):
        color = (0, 0, 255) if i == mutation_info['position'] else (0, 0, 0)
        cv2.putText(img, pair, (50, y), font, 0.6, color, 2, cv2.LINE_AA)
        y += 25
    
    cv2.imshow("DNA Mutation Visualization", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
```

---

## **Final Thoughts**
This script provides:
- **Editable visual output (SVG)** for DNA sequences.
- **Structured storage (JSON)** for mutation tracking.
- **Real-time visualization (OpenCV)** for easy interpretation.

🚀 Modify this script to include more mutations, additional annotations, or alternative storage formats!

