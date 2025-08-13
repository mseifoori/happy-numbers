# Happy Numbers Project ⚡

This Python project contains a simple yet fascinating function to check whether a number is a happy number.
It’s a fun little math puzzle that loops through sums of squares of digits until the truth is revealed: happiness or eternal sadness (aka a loop).

## What is a happy number? 🤔

A happy number is a number that eventually reaches 1 when replaced by the sum of the squares of its digits repeatedly.

> Let’s see why 19 is happy:

```
- 1² + 9² = 82
- 8² + 2² = 68
- 6² + 8² = 100
- 1² + 0² + 0² = 1 ✅
```

We reached 1, so 19 is a happy!

> What about 15?

```
- 1² + 5² = 26
- 2² + 6² = 40
- 4² + 0² = 16
- 1² + 6² = 37
- 3² + 7² = 58
- 5² + 8² = 89
- 8² + 9² = 145
- 1² + 4² + 5² = 42
- 4² + 2² = 20
- 2² + 0² = 4
- 4² = 16
- 1² + 6² = 37
- …
```
As you can see, after 4, a loop starts and we can never reach 1. So 19 is not considered a happy number.

## Project Structure 📁

```
Happy_Numbers/
│
├── src/
│   ├── happpy_numbers.py
│
└── README.md
```

## Requirements 🛠️

- Python 3.7+
- A basic understanding of Python and its core concepts.

## 📃 License

This project is open-source and available under the MIT License.

## 💬 Contributing

Pull requests and suggestions are welcome! Feel free to open an issue to discuss improvements or report bugs.
