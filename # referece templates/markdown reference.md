# Markdown Quick Reference

A simple reference for writing Markdown files (`.md`), especially useful for README files, project notes, study notes, and documentation.

---

## 1. Headings

Use `#` symbols to create headings.

```markdown
# Heading 1

## Heading 2

### Heading 3

#### Heading 4
```

The more `#` symbols you use, the smaller/lower-level the heading.

---

## 2. Paragraphs

Just type normally.

```markdown
This is a paragraph.

This is another paragraph.
```

Leave a blank line between paragraphs.

---

## 3. Bold and Italic

### Bold

```markdown
**This is bold**
```

Result:

**This is bold**

### Italic

```markdown
*This is italic*
```

Result:

*This is italic*

### Bold + Italic

```markdown
***This is bold and italic***
```

Result:

***This is bold and italic***

---

## 4. Lists

### Unordered List

Use `-`, `*`, or `+`.

```markdown
- Python
- Pandas
- NumPy
- Matplotlib
```

Result:

* Python
* Pandas
* NumPy
* Matplotlib

### Nested List

Indent the nested item.

```markdown
- Python
  - Variables
  - Functions
  - Loops
- Pandas
  - DataFrames
  - Series
```

### Ordered List

Use numbers.

```markdown
1. Learn Python
2. Learn Pandas
3. Analyze data
4. Build a project
```

---

## 5. Code

### Inline Code

Use one backtick.

```markdown
Use `print()` to display something.
```

Result:

Use `print()` to display something.

### Code Block

Use three backticks.

````markdown
```python
name = "Lincia"
print(name)
```
````

The `python` tells Markdown that the code is Python and enables syntax highlighting in many editors.

Other examples:

````markdown
```javascript
console.log("Hello");
```

```powershell
Get-Process
```

```bash
ls
```

```text
Plain text
```
````

---

## 6. Blockquotes

Use `>`.

```markdown
> This is a quote.
```

Result:

> This is a quote.

You can also create multiple lines:

```markdown
> This is line one.
> This is line two.
```

---

## 7. Links

Basic link:

```markdown
[Google](https://www.google.com)
```

Result:

[Google](https://www.google.com)

You can also write a link as a reference:

```markdown
[Python][python]

[python]: https://www.python.org
```

This is useful when you have many links.

---

## 8. Images

Basic image syntax:

```markdown
![Description of image](image-url)
```

Example:

```markdown
![Python logo](https://example.com/python.png)
```

The text inside `[]` is alternative text describing the image.

---

## 9. Horizontal Lines

Use three or more hyphens.

```markdown
---
```

Result:

---

## 10. Checkboxes / Task Lists

Useful for project and study checklists.

```markdown
- [x] Learn variables
- [x] Learn functions
- [ ] Learn dictionaries
- [ ] Learn Pandas
```

Result:

* [x] Learn variables
* [x] Learn functions
* [ ] Learn dictionaries
* [ ] Learn Pandas

---

## 11. Tables

Use `|` to separate columns and `---` to create the header separator.

```markdown
| Name | Age | Language |
|---|---:|---|
| Alice | 25 | Python |
| Bob | 30 | Java |
| Karen | 28 | C++ |
```

Result:

| Name  | Age | Language |
| ----- | --: | -------- |
| Alice |  25 | Python   |
| Bob   |  30 | Java     |
| Karen |  28 | C++      |

### Table Alignment

Left:

```markdown
| Name |
|:---|
| Alice |
```

Center:

```markdown
| Name |
|:---:|
| Alice |
```

Right:

```markdown
| Age |
|---:|
| 25 |
```

---

## 12. Strikethrough

Use two tildes.

```markdown
~~This is crossed out~~
```

Result:

~~This is crossed out~~

---

## 13. Escaping Markdown Characters

Sometimes you want Markdown characters to appear as normal text.

Use a backslash:

```markdown
\*This will not be italic\*
```

Result:

*This will not be italic*

Common characters you may need to escape:

```text
\   backslash
*   asterisk
_   underscore
#   hash
`   backtick
[   opening bracket
]   closing bracket
```

---

## 14. Special Characters / Symbols

You can generally paste Unicode symbols directly.

```markdown
✓ Completed
→ Next step
⚠ Warning
❌ Error
💡 Tip
```

---

## 15. HTML

Markdown usually supports some HTML.

```markdown
<details>
<summary>Click to expand</summary>

Hidden content goes here.

</details>
```

This can be useful for longer documentation, although support varies between Markdown platforms.

---

# Markdown Cheat Sheet

| What you want      | Markdown              |
| ------------------ | --------------------- |
| Heading            | `# Heading`           |
| Subheading         | `## Heading`          |
| Bold               | `**text**`            |
| Italic             | `*text*`              |
| Bold + italic      | `***text***`          |
| Inline code        | `` `code` ``          |
| Code block         | ` ```python ... ``` ` |
| Bullet point       | `- item`              |
| Numbered list      | `1. item`             |
| Checkbox           | `- [ ] task`          |
| Completed checkbox | `- [x] task`          |
| Link               | `[text](url)`         |
| Image              | `![alt](url)`         |
| Quote              | `> quote`             |
| Horizontal line    | `---`                 |
| Strikethrough      | `~~text~~`            |

---

# Useful Markdown Template for Python Projects

You can use this as a starting point for your Python project README or project notes.

````markdown
# Project Name

Short description of what the project does.

## Description

Explain the project in a few sentences.

## Features

- Feature 1
- Feature 2
- Feature 3

## Requirements

- Python 3.x
- pandas
- numpy

## Installation

```bash
pip install -r requirements.txt
````

## Usage

```python
python main.py
```

## Example

```text
Enter your name: Alice
Hello, Alice!
```

## What I Learned

* Functions
* Loops
* Dictionaries
* File handling

## Future Improvements

* [ ] Add a GUI
* [ ] Add error handling
* [ ] Add database support

## Author

Your Name

````

---

# Markdown Tips for VS Code

If you're writing Markdown in VS Code:

1. Create a file ending in `.md`.
2. Type your Markdown.
3. Press `Ctrl + Shift + V` to open the rendered Markdown preview.
4. Or press `Ctrl + K`, then `V` to open the preview beside your editor.

For example:

```text
my-project/
│
├── main.py
├── README.md
└── requirements.txt
````

Your `README.md` can document what `main.py` does, how to run it, and what you learned.

---

# The 10 Things to Memorize First

You don't need to memorize all of Markdown.

Start with these:

````markdown
# Heading

## Subheading

**bold**

*italic*

- bullet point

1. numbered item

`inline code`

```python
print("code block")
````

[link](https://example.com)

* [ ] task
* [x] completed task

```

Once you know those, you can write most everyday Markdown without looking anything up.
```

**One important tip:** don't try to memorize Markdown. Keep this file open while you're writing your Python projects. After you've used headings, lists, code blocks, tables, and checkboxes 20–30 times, you'll naturally remember most of it.
