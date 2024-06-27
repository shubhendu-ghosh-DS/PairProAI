
import streamlit as st
from generate_code import generate_code



def main():
    st.markdown(
    """
    <p style="color: #00dba8;font-size: 70px;font-family: arial; text-align:center; margin-bottom: 0px;"><b>PairProAI</b></p>""", unsafe_allow_html=True)
    st.markdown("""<p style="color: #00dba8;font-size: 30px;font-family: sans-serif; text-align:center; margin-bottom: 50px;">Your AI-Powered Pair Programmer</p>""", unsafe_allow_html=True)
    
    
    # Layout with two columns
    col1, col2 = st.columns([3, 1])

    with col1:
        # Input code from the user
        user_code = st.text_area("Paste your code here:", height=300)
        
        # Additional input for error message if "Debug Your Code" is selected
        error_message = ""
        if st.session_state.get("option") == "Debug Your Code":
            error_message = st.text_area("Paste your error message here:", height=100)
    
    with col2:
        # Select an option
        option = st.selectbox("Choose an option:", [
            "Code Translation",
            "Code Improvements",
            "Simplify Code",
            "Write Test Cases",
            "Improve Efficiency",
            "Debug Your Code"
        ], key="option")
        
        # Additional select box for target language if "Code Translation" is selected
        if option == "Code Translation":
            target_language = st.selectbox("Select target language:", [
                "Python",
                "Java",
                "JavaScript",
                "C++",
                "C#",
                "Ruby",
                "PHP",
                "Swift",
                "Go",
                "TypeScript"
            ])
        else:
            target_language = None
    
    # Button to generate the solution
    button_color = "#4CAF50"  # Green color
    button_style = f"background-color: {button_color}; color: white;"

    if st.button("Generate Solution"):
        if user_code:
            generated_code, explanation = generate_code(user_code, option, target_language, error_message)
            
            # Display the generated code and explanation
            st.subheader("Generated Code")
            st.code(generated_code, language='python')
            
            st.subheader("Explanation")
            st.markdown(explanation)
        else:
            st.warning("Please paste your code in the text area above.")
    

if __name__ == "__main__":
    main()