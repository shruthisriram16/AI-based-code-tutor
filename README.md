# Code Tutor (Deterministic DSA Reviewer)

## Overview

Code Tutor is a deterministic programming tutor and DSA code reviewer
built using: - OpenAI API - Streamlit - Structured JSON schema
enforcement

The system analyzes student-submitted code and produces a stable,
structured, and educational review.\
The same input always produces the same output (deterministic behavior
enforced).

------------------------------------------------------------------------

## Key Features

-   Deterministic analysis (temperature = 0)
-   Strict JSON schema enforcement
-   Structured error categorization:
    -   syntax
    -   runtime
    -   logic
    -   edge_case
    -   style
-   High-level fix strategies (no rewritten code)
-   Learning suggestions
-   Time & space complexity analysis
-   Confidence scoring

------------------------------------------------------------------------

## Architecture

### 1. OpenAI Review Engine

The `review_code()` function:

-   Sends:
    -   code
    -   optional problem statement
    -   optional language
-   Uses a strict system prompt enforcing:
    -   Exact JSON schema
    -   Canonical error ordering
    -   Deterministic output
    -   No extra explanations
    -   No rewritten solutions

Model used:

    gpt-4o-mini

Temperature:

    0 (deterministic)

------------------------------------------------------------------------

### 2. Streamlit UI

Two-panel layout:

Left Panel: - Problem statement input - Language selector - Code input -
Review button

Right Panel: - Code explanation - Correctness status - Errors list - Fix
strategy - Learning suggestions - Complexity analysis - Confidence level

Session state is used to persist review results.

------------------------------------------------------------------------

## JSON Output Schema

The model returns exactly:

    {
      "code_explanation": "string",
      "is_correct": true,
      "errors": [
        {
          "type": "syntax|runtime|logic|edge_case|style",
          "summary": "string",
          "location": "string or null",
          "cause": "string"
        }
      ],
      "fix_strategy": ["string"],
      "suggestions": ["string"],
      "complexity": {
        "current": { "time": "string", "space": "string" },
        "target": { "time": "string", "space": "string" },
        "confidence": "high|medium|low",
        "notes": "string or null"
      }
    }

------------------------------------------------------------------------

## Determinism Enforcement

The system enforces:

-   Stable wording across runs
-   Stable error ordering
-   Locked interpretation strategy
-   No randomness
-   No rotated suggestions
-   No additional commentary outside JSON

This ensures reproducibility for identical inputs.

------------------------------------------------------------------------

## Complexity Reporting

The system reports:

-   Current time complexity
-   Current space complexity
-   Target complexity (if improvements possible)
-   Confidence level
-   Notes (only if medium/low confidence)

------------------------------------------------------------------------

## Running the Project

### 1. Create Virtual Environment

    python -m venv venv

Activate (PowerShell):

    .\venv\Scripts\Activate.ps1

### 2. Install Dependencies

    pip install openai streamlit

### 3. Run Application

    streamlit run streamlit_codetutor_v1.py

------------------------------------------------------------------------

## Project Structure

    code_tutor/
    │
    ├── streamlit_codetutor_v1.py
    ├── review_engine.py (review_code logic)
    ├── requirements.txt
    └── README.md

------------------------------------------------------------------------

## Educational Philosophy

This system is designed to:

-   Encourage structured thinking
-   Separate correctness from style
-   Promote edge-case awareness
-   Reinforce complexity analysis
-   Avoid over-dependence on full solutions

It acts as a strict tutor rather than a code generator.

------------------------------------------------------------------------

## Future Improvements

-   Add execution sandbox for runtime testing
-   Add diff-style feedback view
-   Add multi-language complexity inference
-   Add test case simulation mode
-   Add plagiarism detection module

------------------------------------------------------------------------

## Author

Shruthi Sriram\
Deterministic Code Review System -- 2025
