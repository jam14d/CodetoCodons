import streamlit as st

st.set_page_config(page_title="STABILITY MATRIX", layout="wide")

st.title("STABILITY MATRIX")

st.write("Welcome to Stability Matrix, an advanced bioinformatics terminal where you master Object-Oriented Programming (OOP) while analyzing DNA sequences.")

st.markdown("""## SYSTEM BOOT: CLASS DESIGN OVERVIEW
### What should be provided when creating a class?
- Parameters in `__init__` should be things the user will know when creating an object.
- Example: `sequence` is an input the user will provide.

### What attributes should be derived inside the class?
- These are calculated from provided data but not required as parameters.
- Example: `gc_content` is derived after calling a method.

### What should be stored for later use?
- Define attributes inside `__init__` to make them available throughout the class.
""")

st.markdown("""
## STEP 1: CLASS DEFINITION
- Define functions inside the class using `def`
- Think about what your class needs when you create `__init__` (like a DNA sequence).
- Use `self` to store attributes that belong to the object.
""")
user_class_code = st.text_area("Write your class definition and `__init__` method:")

st.markdown("""
## STEP 2: COUNT CYTOSINE BASES
- Create a method called `count_cytosine`.
- This function should count the number of 'C' bases in the sequence.
- Use `.count('C')` to count occurrences.
""")
user_count_code = st.text_area("Write your `count_cytosine` function:")

st.markdown("""
## STEP 3: COUNT GUANINE BASES
- Create a method called `count_guanine`.
- This function should count the number of 'G' bases in the sequence.
- Use `.count('G')` to count occurrences.
""")
user_guanine_code = st.text_area("Write your `count_guanine` function:")

st.markdown("""
## STEP 4: COMPUTE GC CONTENT
- Create a function `compute_gc_percentage(self)`. 
- Count the number of 'G' and 'C' bases.
- Divide their sum by the total length of the sequence.
- Multiply by 100 to get the percentage.
""")
user_gc_code = st.text_area("Write your `compute_gc_percentage` function:")

st.markdown("""
## STEP 5: DISPLAY RESULTS
- Print the calculated GC content in a user-friendly way.
- Use `print(f"GC Content: {gc_content:.2f}%")` for formatted output.
""")
user_display_code = st.text_area("Write your display function:")

solution_code = '''
class DNAAnalyzer:
    def __init__(self, sequence):
        self.sequence = sequence.upper()
    
    def count_cytosine(self):
        return self.sequence.count('C')
    
    def count_guanine(self):
        return self.sequence.count('G')
    
    def compute_gc_percentage(self):
        g_count = self.count_guanine()
        c_count = self.count_cytosine()
        total_length = len(self.sequence)
        if total_length == 0:
            return 0
        return ((g_count + c_count) / total_length) * 100
'''

st.download_button("Download Solution Code", solution_code, file_name="oop_gc_analysis_solution.txt", mime="text/plain")
