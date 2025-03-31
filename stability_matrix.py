import streamlit as st
import random
import time

# Futuristic Science Lab Theme with Enhanced Aesthetics
st.set_page_config(page_title="STABILITY MATRIX", page_icon="🔬", layout="wide")

def set_theme():
    st.markdown(
        """
        <style>
            html, body, [class*="st"] {
                background-color: #101820;
                color: #A8DADC;
                font-family: 'Orbitron', sans-serif;
            }
            * > [data-testid=stHeaderActionElements] {
                display: none;
            }
            .big-title-glow {
                font-size: 50px;
                font-weight: bold;
                text-align: center;
                color: #ffcc66;
                text-shadow: 0 0 50px #ff9966, 0 0 50px #ffcc66, 0 0 50px #ff6633;
                animation: flicker-big 1.5s infinite alternate;
            }
            .title-glow {
                font-size: 20px;
                font-weight: bold;
                text-align: center;
                color: #88c0d0;
                text-shadow: 0 0 10px #88c0d0, 0 0 15px #6fa3bf, 0 0 20px #5790af;
                animation: flicker 1.5s infinite alternate;
            }
            @keyframes flicker-big {
                from { opacity: 1; }
                to { opacity: 0.7; }
            }
            @keyframes flicker {
                from { opacity: 1; }
                to { opacity: 0.7; }
            }
            .stButton > button {
                background: linear-gradient(135deg, #16A085, #2ECC71);
                color: white;
                font-weight: bold;
                border-radius: 10px;
                border: none;
                font-size: 16px;
                transition: all 0.3s ease-in-out;
                box-shadow: 0px 4px 10px rgba(46, 204, 113, 0.5);
            }
            .stButton > button:hover {
                background: linear-gradient(135deg, #1ABC9C, #27AE60);
                transform: scale(1.05);
                box-shadow: 0px 6px 15px rgba(46, 204, 113, 0.7);
            }
            .data-box {
                border: 2px solid #16A085;
                padding: 15px;
                border-radius: 10px;
                text-align: center;
                font-size: 18px;
                background-color: rgba(22, 160, 133, 0.2);
            }
            .accent-text {
                color: #E67E22;
                font-weight: bold;
            }
            .highlight {
                color: #F39C12;
                font-weight: bold;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

set_theme()

st.markdown("<div class='big-title-glow'>STABILITY MATRIX</div>", unsafe_allow_html=True)

st.write("Welcome to **Stability Matrix**, an advanced bioinformatics terminal where you master **Object-Oriented Programming (OOP)** while analyzing DNA sequences. This system is used in top-secret genetic research facilities worldwide.")

st.markdown("""## <span class='accent-text'>SYSTEM BOOT: CLASS DESIGN OVERVIEW</span>
### What should be provided when creating a class?
- Parameters in `__init__` should be things the user will know when creating an object.
- Example: `sequence` is an input the user will provide.

### What attributes should be derived inside the class?
- These are calculated from provided data but not required as parameters.
- Example: `gc_content` is derived after calling a method.

### What should be stored for later use?
- Define attributes inside `__init__` to make them available throughout the class.
""", unsafe_allow_html=True)

st.markdown("""
## <span class='highlight'>STEP 1: CLASS DEFINITION</span>
- Define functions inside the class using `def`
- Think about what your class needs when you create `__init__` (like a DNA sequence).
- Use `self` to store attributes that belong to the object.
""", unsafe_allow_html=True)
user_class_code = st.text_area("Write your class definition and `__init__` method:")

st.markdown("""
## <span class='highlight'>STEP 2: COUNT CYTOSINE BASES</span>
- Create a method called `count_cytosine`.
- This function should count the number of 'C' bases in the sequence.
- Use `.count('C')` to count occurrences.
""", unsafe_allow_html=True)
user_count_code = st.text_area("Write your `count_cytosine` function:")

st.markdown("""
## <span class='highlight'>STEP 3: COUNT GUANINE BASES</span>
- Create a method called `count_guanine`.
- This function should count the number of 'G' bases in the sequence.
- Use `.count('G')` to count occurrences.
""", unsafe_allow_html=True)
user_guanine_code = st.text_area("Write your `count_guanine` function:")

st.markdown("""
## <span class='highlight'>STEP 4: COMPUTE GC CONTENT</span>
- Create a function `compute_gc_percentage(self)`. 
- Count the number of 'G' and 'C' bases.
- Divide their sum by the total length of the sequence.
- Multiply by 100 to get the percentage.
""", unsafe_allow_html=True)
user_gc_code = st.text_area("Write your `compute_gc_percentage` function:")

st.markdown("""
## <span class='highlight'>STEP 5: DISPLAY RESULTS</span>
- Print the calculated GC content in a user-friendly way.
- Use `print(f"GC Content: {gc_content:.2f}%")` for formatted output.
""", unsafe_allow_html=True)
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
