"""
hello.py - Very Simple Single File Application
"""

def get_greeting(name: str = "World") -> str:
    """Return a friendly greeting."""
    if not name:
        name = "World"
    return f"Hello, {name}!"

def calculate_square(n: int) -> int:
    """Return square of a number."""
    return n * n

def main():
    greeting = get_greeting("DevOps")
    print(greeting)
    print(f"Sample calculation: 5 squared is {calculate_square(5)}")

if __name__ == "__main__":
    main()
