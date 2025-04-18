import streamlit as st

def app():

    # Title Section
    st.markdown("""
    <div style="text-align: center;">
    <h1 class="typewriter">
        STABILITY MATRIX<span class="cursor">|</span>
    </h1>
</div>


<style>
@keyframes typing {
  from { width: 0 }
  to { width: 100% }
}
@keyframes blink {
  0%, 100% { opacity: 1 }
  50% { opacity: 0 }
}
.typewriter {
  font-size: 90px;
  color: #00ffea;
  text-shadow: 0px 0px 15px #00FFAA, 0px 0px 25px #00FFD1;
  letter-spacing: 8px;
  overflow: hidden;
  white-space: nowrap;
  border-right: .05em solid #00FFAA1;
  width: 0;
  animation: typing 2s steps(30, end) forwards;
  display: inline-block;
}
.cursor {
  animation: blink 1s infinite;
  color: #00FFD1;
}
</style>

    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)  # Adds spacing before the next section

    # New GC Content Introduction Section
    st.markdown("""
        <div style="background-color: #0e0e0e; padding: 20px; border-radius: 10px; color: #00ffea; 
                    font-family: 'Orbitron', monospace; text-align: left; font-size: 12px; line-height: 1.5;
                    box-shadow: 0 0 15px #00ffea, 0 0 25px #00ffaa; max-width: 900px; margin: auto; padding: 20px;">
            <h4>How Can We Measure DNA Stability?</h4>
            
GC content—the proportion of guanine (G) and cytosine (C) bases in a DNA sequence—plays a critical role in DNA stability. 
Higher GC content enhances stability due to the stronger triple hydrogen bonding between G and C pairs, making the DNA more resistant to denaturation.
        
In this module, you will analyze GC content programmatically using Python and Object-Oriented Programming (OOP).

Define the Class and Initialize Data
- Use the `__init__` method to set up the class with a DNA sequence.
- Ensure the sequence is stored in uppercase for consistency.

Compute Important DNA Properties
- Write functions to count the occurrences of specific nucleotides.
- Calculate the GC content percentage to analyze DNA stability.

Implement Output and Display
- Create methods to return useful information about the DNA sequence.
- Format the output clearly for easy interpretation.

Use the text boxes below to write your code for each step.   
Once finished, download the solution to compare with your implementation.
        
        
        
    """, unsafe_allow_html=True)


    st.markdown("<br>", unsafe_allow_html=True)  # Adds spacing before the next section

    # # Closing statement in the same styled div
    # st.markdown("""
    #     <div style="background-color: #0e0e0e; padding: 20px; border-radius: 10px; color: #00ffea; 
    #                 font-family: 'Orbitron', monospace; text-align: left; 
    #                 box-shadow: 0 0 15px #00ffea, 0 0 25px #00ffaa; max-width: 900px; margin: auto; padding: 20px;">
    #         <p>In this module, you will analyze GC content programmatically using Python and Object-Oriented Programming (OOP).</p>
    #     </div>
    # """, unsafe_allow_html=True)

    # # st.markdown("<br><br>", unsafe_allow_html=True)  # Adds spacing before the next section

    # Step Instructions
#     st.markdown("""
#     <div style="background-color: #0e0e0e; padding: 20px;
#             color: #00ffea; font-family: 'Orbitron', monospace; text-align: left; font-size: 14px; line-height: 1.5;
#             box-shadow: 0 0 5px #009e91:, 0 0 25px #009e91:; 
#             border: 1px solid #009e91:; max-width: 900px; margin: auto;">

# <p>In this module, you will analyze GC content programmatically using Python and Object-Oriented Programming (OOP).</p>

# ##### Define the Class and Initialize Data
# - Use the `__init__` method to set up the class with a DNA sequence.
# - Ensure the sequence is stored in uppercase for consistency.

# ##### Compute Important DNA Properties
# - Write functions to count the occurrences of specific nucleotides.
# - Calculate the GC content percentage to analyze DNA stability.

# ##### Implement Output and Display
# - Create methods to return useful information about the DNA sequence.
# - Format the output clearly for easy interpretation.

# Use the text boxes below to write your code for each step.   
# Once finished, download the solution to compare with your implementation.

  
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)  # Adds spacing before Step 1


    # # Instructions Section
    # st.markdown("""
    # **This module will guide you through building a class in Python to analyze DNA sequences.**
    
    # ### Step 1: Define the Class and Initialize Data
    # - Use the `__init__` method to set up the class with a DNA sequence.
    # - Ensure the sequence is stored in uppercase for consistency.

    # ### Step 2: Compute Important DNA Properties
    # - Write functions to count the occurrences of specific nucleotides.
    # - Calculate the GC content percentage to analyze DNA stability.

    # ### Step 3: Implement Output and Display
    # - Create methods to return useful information about the DNA sequence.
    # - Format the output clearly for easy interpretation.

    # **Use the text boxes below to write your code for each step. Once finished, download the solution to compare with your implementation.**
    # """)
    # User Code Inputs
    st.markdown("""
    ### STEP 1: CLASS DEFINITION
    - Define functions inside the class using `def`
    - Think about what your class needs when you create `__init__` (like a DNA sequence).
    - Use `self` to store attributes that belong to the object.
    """)
    user_class_code = st.text_area("Write your class definition and `__init__` method:")

    st.markdown("""
    ### STEP 2: COUNT CYTOSINE BASES
    - Create a method called `count_cytosine`.
    - This function should count the number of 'C' bases in the sequence.
    - Use `.count('C')` to count occurrences.
    """)
    user_count_code = st.text_area("Write your `count_cytosine` function:")

    st.markdown("""
    ### STEP 3: COUNT GUANINE BASES
    - Create a method called `count_guanine`.
    - This function should count the number of 'G' bases in the sequence.
    - Use `.count('G')` to count occurrences.
    """)
    user_guanine_code = st.text_area("Write your `count_guanine` function:")

    st.markdown("""
    ### STEP 4: COMPUTE GC CONTENT
    - Create a function `compute_gc_percentage(self)`. 
    - Count the number of 'G' and 'C' bases.
    - Divide their sum by the total length of the sequence.
    - Multiply by 100 to get the percentage.
    """)
    user_gc_code = st.text_area("Write your `compute_gc_percentage` function:")

    st.markdown("""
    ### STEP 5: DISPLAY RESULTS
    - Print the calculated GC content in a user-friendly way.
    - Use `print(f"GC Content: {gc_content:.2f}%")` for formatted output.
    """)
    user_display_code = st.text_area("Write your display function:")

    # Solution Code Download
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

if __name__ == "__main__":
    app()
