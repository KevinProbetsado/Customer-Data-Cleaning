# 📞 Customer Call List — Data Cleaning Project

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![pandas](https://img.shields.io/badge/pandas-Data%20Cleaning-green?style=flat-square&logo=pandas)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)

## 📌 Overview

A real-world data cleaning project using **Python** and **pandas** to prepare a raw customer call list for a sales team. The raw dataset contained inconsistencies, missing values, poorly formatted phone numbers, and customers who opted out of contact — all of which were cleaned and standardized.

---

## 🔍 Problem

The raw dataset had several issues that made it unusable for a sales team:

- Duplicate customer records
- Inconsistent phone number formats (e.g. `(123) 456-7890`, `123.456.7890`)
- Missing and empty phone numbers
- Last names with unwanted characters (`123`, `.`, `/`, `_`)
- Addresses stored in a single column instead of separate fields
- `Yes`/`No` values inconsistently written across columns
- Customers who opted out of contact still included in the list

---

## ✅ Solution

Cleaned the dataset using Python and pandas with the following steps:

| Step | Action |
|------|--------|
| 1 | Removed duplicate rows |
| 2 | Dropped irrelevant columns |
| 3 | Stripped unwanted characters from last names |
| 4 | Removed all non-digit characters from phone numbers using regex |
| 5 | Reformatted phone numbers to `XXX-XXX-XXXX` |
| 6 | Split combined address into `Street Address`, `State`, `Zip Code` |
| 7 | Standardized `Yes`/`No` → `Y`/`N` across columns |
| 8 | Removed customers marked as `Do Not Contact` |
| 9 | Removed rows with missing phone numbers |
| 10 | Reset the DataFrame index |

---

## 🛠️ Tools & Libraries

- **Python 3**
- **pandas**

---

## 📁 Project Structure

```
Customer-Data-Cleaning/
├── customer_cleaning.py       # Main cleaning script
├── Customer Call List.xlsx    # Raw input dataset (sample/practice data)
└── README.md
```

---

## ▶️ How to Run

1. Clone this repository:
   ```bash
   git clone https://github.com/KevinProbetsado/Customer-Data-Cleaning.git
   ```

2. Install dependencies:
   ```bash
   pip install pandas openpyxl
   ```

3. Run the script:
   ```bash
   python customer_cleaning.py
   ```

> ⚠️ **Note:** The dataset used here is a sample practice file. Never upload real customer data to public repositories.

---

## 💡 Key Concepts Demonstrated

- Data cleaning with `pandas`
- Regex for string pattern matching
- Handling `NaN` vs empty strings
- Boolean filtering instead of loops for performance
- `reset_index()` after row removal
- Real-world data wrangling workflow

---

## 👤 Author

**Kevin Probetsado**  
📎 [GitHub Profile](https://github.com/KevinProbetsado)
