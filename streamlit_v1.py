import streamlit as st
from streamlit_codetutor_v1 import review_code
import json

st.set_page_config(page_title="Code Tutor", layout="wide")

st.title("Code Tutor (DSA Reviewer)")

col_left, col_right = st.columns(2)

# ---------------- LEFT PANEL (INPUT) ----------------
with col_left:
    problem = st.text_area(
        "Problem statement",
        height=200
    )

    language = st.selectbox(
        "Language",
        ["auto", "cpp", "python", "java"]
    )

    code = st.text_area(
        "Paste your code here",
        height=700,
        placeholder="Enter C++, Python, or Java code..."
    )

    if st.button("Review Code"):
        raw_output = review_code(code, problem, language)
        st.session_state["review"] = json.loads(raw_output)

review = st.session_state.get("review")

# ---------------- RIGHT PANEL (OUTPUT) ----------------
with col_right:
    if not review:
        st.info("Submit code to see the review")
    else:
        # -------- Code Explanation --------
        if review.get("code_explanation"):
            st.subheader("Code Explanation")
            st.write(review["code_explanation"])

        # -------- Code Correctness --------
        st.subheader("Code Correctness")
        if review.get("is_correct"):
            st.success("The code is correct")
        else:
            st.error("The code has issues")

        # -------- Errors --------
        st.subheader(" Errors")
        errors = review.get("errors", [])

        if errors:
            for i, err in enumerate(errors, 1):
                st.markdown(f"""
- **Error {i}: {err['summary']}**
  - **Type:** {err['type']}
  - **Location:** {err['location']}
  - **Cause:** {err['cause']}
""")
        else:
            st.success("No errors found")

        # -------- How to Improve --------
        st.subheader(" How to Improve")
        fix_steps = review.get("fix_strategy", [])

        if fix_steps:
            for i, step in enumerate(fix_steps, 1):
                st.markdown(f"- **Step {i}:** {step}")
        else:
            st.write("No fixes needed")

        # -------- Learning Suggestions --------
        st.subheader(" Learning Suggestions")
        suggestions = review.get("suggestions", [])

        if suggestions:
            for i, suggestion in enumerate(suggestions, 1):
                st.markdown(f"- **Suggestion {i}:** {suggestion}")
        else:
            st.write("No suggestions available")

        # -------- Complexity Analysis --------
        st.subheader(" Complexity Analysis")
        complexity = review.get("complexity", {})
        current = complexity.get("current", {})
        target = complexity.get("target", {})
        confidence = complexity.get("confidence", "unknown")
        notes = complexity.get("notes")

        col_time, col_space = st.columns(2)

        with col_time:
            st.markdown("**Time Complexity**")
            st.markdown(f"- Current: `{current.get('time', 'unknown')}`")
            st.markdown(f"- Target: `{target.get('time', 'unknown')}`")

        with col_space:
            st.markdown("**Space Complexity**")
            st.markdown(f"- Current: `{current.get('space', 'unknown')}`")
            st.markdown(f"- Target: `{target.get('space', 'unknown')}`")

        # -------- Confidence --------
        st.subheader(" Confidence")
        if confidence == "high":
            st.success("High confidence in the analysis")
        elif confidence == "medium":
            st.warning("Medium confidence — assumptions may exist")
        else:
            st.error("Low confidence — problem intent is unclear")

        if notes:
            st.info(notes)
