# 📄 SOW Analyzer (GenAI - Open Source MVP)

A lightweight GenAI-based application that analyzes SOW (Statement of
Work) documents and automatically identifies and flags potential issues
using a local open-source LLM.

------------------------------------------------------------------------

##  Overview

This project demonstrates how Generative AI can be used to review SOW
documents and detect:

-   Logical inconsistencies\
-   Missing or incomplete information\
-   Incorrect values (dates, pricing, resource mismatch)\
-   Contractual risks and unclear terms

The solution runs entirely locally using open-source models (via
Ollama), avoiding external API dependencies.

------------------------------------------------------------------------

##  Key Features

-   Upload SOW PDF documents\
-   Extract and process document content\
-   Analyze using local LLM (Mistral / LLaMA)\
-   Automatically flag issues with severity\
-   Structured output with explanation\
-   Lightweight MVP (optimized for small documents)

------------------------------------------------------------------------

##  Architecture

User Upload PDF → PDF Extraction → LLM Analysis → Output Display

------------------------------------------------------------------------

##  Tech Stack

-   Python\
-   Streamlit\
-   pdfplumber\
-   Ollama\
-   Mistral / LLaMA

------------------------------------------------------------------------

##  Installation

``` bash
git clone https://github.com/your-username/sow-analyzer.git
cd sow-analyzer
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
ollama pull mistral
streamlit run app.py
```

------------------------------------------------------------------------

##  MVP Scope

-   Max 10 pages\
-   Single document\
-   No embeddings

------------------------------------------------------------------------

##  Author

GenAI MVP project for SOW validation.
