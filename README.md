# Text to Brainfuck Translator

<img src="assets/503825bd3c59fbf4fc8ee2496d15c4ae.jpg" width=300>

## Description

**Text to Brainfuck Translator** is a Python-based translator that converts arbitrary text input into optimized Brainfuck code. This project was created to validate my understanding of ASCII encoding and Brainfuck, and to refine my Python programming skills. The goal of this tool is to generate the most compact Brainfuck code possible for any given string.

## Features

- **Optimized Brainfuck Translation:** Converts input text into Brainfuck code with minimal space usage.
- **Case Conversion:** Supports uppercase and lowercase text conversions.
- **Flexible Input:** Handles various input formats and provides options for text case manipulation.

## Technologies

- **Programming Language:** Python
- **Libraries Used:** Standard library modules (`math`, `array`)

## Usage

To run the project, ensure Python is installed and properly set up in your PATH. Follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Ci3l/TextToBrainfuckTranslator.git
   ```
2. Navigate into the project directory:
   ```bash
   cd TextToBrainfuckTranslator
   ```
3. Run the translator:
   ```bash
   python MindBlower.py
   ```
### Command Line Options
You can modify the input text for case conversion by using the following options:
* **'!uppercase [your text]'** to convert the text to uppercase before translation.
* **'!lowercase [your text]'** to convert the text to lowercase before translation.

### Function Syntax
```python
MindBlower(input, uppercase=False, lowercase=False)
```
* **'input'**: The text to be converted to Brainfuck code.
* **'uppercase'** (optional): Set to True to convert input to uppercase.
* **'lowercase'** (optional): Set to True to convert input to lowercase.

### Demo
You can try out the Mind Blower translator live at [JDoodle](https://www.jdoodle.com/iembed/v0/ean). Provide your text in _Stdin Inputs_ and see the optimized Brainfuck code generated in real-time.

### Related Projects
[Brainfuck2Ascii](https://github.com/Ci3l/BrainfuckToASCII): A basic Brainfuck compiler that translates Brainfuck code into ASCII text.

### Contributing
If you’d like to contribute, please follow these guidelines:

* Fork the repository
* Create a new branch (**git checkout -b feature/YourFeature**)
* Commit your changes (**git commit -am 'Add new feature'**)
* Push to the branch (**git push origin feature/YourFeature**)
* Open a pull request

### License
This project is licensed under the EPL 2.0 License - see the LICENSE file for details.


