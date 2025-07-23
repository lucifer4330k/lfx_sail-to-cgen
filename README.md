# YAML/JSON to S-Expression Converter

This project converts structured configuration files written in either **YAML** or **JSON** into **LISP-style S-expressions**. This is particularly useful for tools and platforms that consume LISP-like syntax, such as the [Sail language](https://github.com/rems-project/sail) or other DSLs used in formal verification, hardware modeling, or compiler design.

---

## 🔍 Project Overview

Many modern tools still rely on LISP-style input formats. To bridge the gap between human-readable formats like YAML/JSON and such legacy tools, this converter parses and flattens nested JSON/YAML data into S-expression format, while preserving structure and key-value associations.

---

## 📁 Project Structure

```
.
├── sample.json          # Sample JSON input file
├── sample3.yaml         # Sample YAML input file
├── json_to_lisp.py      # Python script for conversion
└── README.md            # This file
```

---

## ⚙️ Prerequisites

- Python 3.8+
- `pyyaml` package (for YAML support)

Install dependencies:
```bash
pip install pyyaml
```

---

## ▶️ How to Run

### 1. Convert JSON to S-Expression
```bash
python json_to_lisp.py sample.json
```

### 2. Convert YAML to S-Expression
```bash
python json_to_lisp.py sample3.yaml
```

The output will be printed on the console in valid LISP format.

---

## 🧠 Example Output

```lisp
(yaml:projectName "ExampleApp")
(yaml:version "2.1.3")
(yaml:author (yaml:name "Example Author") (yaml:email "support@exampleapp.com"))
...
```

---

## 🎯 Use Case & Relevance to LFX Mentorship

This project demonstrates the ability to:
- Translate between modern config formats and legacy symbolic expressions
- Handle complex nested data structures and arrays
- Write clean and extensible code for language-agnostic transformations

It is highly relevant to projects that involve:
- Language tooling and compilers
- Formal modeling (e.g., RISC-V Sail specifications)
- YAML → DSL transformations for backend and dev tools

---

## 📬 Submitting to LFX Mentorship

To submit this project as part of your **LFX Mentorship Proposal**:

1. Fork this repository
2. Push your code and this README
3. Submit the GitHub repo link in your LFX application under "Project Proposal"
4. Optionally, describe:
   - What improvements you plan (e.g., reverse conversion, GUI tool, etc.)
   - Why this domain interests you (e.g., tooling, language design)

---

## 🙋‍♂️ Author

**Debanjan Maji**  
Email: [YourEmail@example.com]  
GitHub: [https://github.com/your-username]  
