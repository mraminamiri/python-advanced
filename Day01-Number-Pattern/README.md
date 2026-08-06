
# Day 01 - Number Pattern

## 📌 Description

This project prints an incremental number pattern using nested `for` loops in Python.

The number of rows is provided by the user.

## 💻 Example

**Input**

```text
Enter number of rows: 5
```

**Output**

```text
1
12
123
1234
12345
```

---

## 🧠 Concepts Covered

- Nested `for` loops
- User input
- `range()`
- `print(end="")`
- Pattern printing

---

## 🚀 How to Run

```bash
python number_pattern.py
```

---

## 📂 Project Structure

```
Day-01-Number-Pattern/
│
├── number_pattern.py
└── README.md
```

---

## 👨‍💻 Code

```python
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
```

---

## 🎯 Learning Goal

Practice nested loops and pattern generation in Python.

---

⭐ If you find this project useful, feel free to star the repository.
