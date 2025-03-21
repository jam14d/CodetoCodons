import json
import svgwrite
import cv2
import numpy as np

# Function to generate a simple DNA strand with base pairs
def generate_dna_sequence():
    return ["A-T", "C-G", "G-C", "T-A", "A-T", "G-C", "C-G", "T-A"]

# Function to introduce a mutation
def introduce_mutation(sequence, index, new_base):
    original_sequence = sequence[:]
    original_pair = sequence[index]
    original_base, pair_base = original_pair.split('-')
    mutated_pair = f"{new_base}-{pair_base}"
    sequence[index] = mutated_pair
    return original_sequence, sequence, {"original": original_pair, "mutated": mutated_pair, "position": index}

# Function to generate SVG for DNA visualization
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

# Function to generate JSON representation
def create_json(original_sequence, mutated_sequence, mutation_info):
    data = {
        "original_sequence": original_sequence,
        "mutated_sequence": mutated_sequence,
        "mutation": mutation_info
    }
    with open("dna_mutation.json", "w") as f:
        json.dump(data, f, indent=4)

# Function to visualize the mutation using OpenCV
def visualize_dna(original_sequence, mutated_sequence, mutation_info):
    img = np.ones((600, 500, 3), dtype=np.uint8) * 255
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    y = 60
    cv2.putText(img, "Original DNA:", (50, y - 10), font, 0.6, (0, 0, 0), 2, cv2.LINE_AA)
    for i, pair in enumerate(original_sequence):
        cv2.putText(img, pair, (50, y), font, 0.6, (0, 0, 0), 2, cv2.LINE_AA)
        y += 25
    
    y += 40  # Space between original and mutated
    cv2.putText(img, "Mutated DNA:", (50, y - 10), font, 0.6, (0, 0, 0), 2, cv2.LINE_AA)
    for i, pair in enumerate(mutated_sequence):
        color = (0, 0, 255) if i == mutation_info['position'] else (0, 0, 0)
        cv2.putText(img, pair, (50, y), font, 0.6, color, 2, cv2.LINE_AA)
        y += 25
    
    cv2.imshow("DNA Mutation Visualization", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Main execution
dna_sequence = generate_dna_sequence()
original_sequence, mutated_sequence, mutation_info = introduce_mutation(dna_sequence, 3, "G")
create_svg(original_sequence, mutated_sequence, mutation_info)
create_json(original_sequence, mutated_sequence, mutation_info)
visualize_dna(original_sequence, mutated_sequence, mutation_info)

print("DNA mutation visualization created!")