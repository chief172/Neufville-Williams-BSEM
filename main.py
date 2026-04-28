import asyncio
from typing import Dict

# Shared "database"
books: Dict[str, bool] = {
    "math_book": True,
    "science_book": True
}

# Simulate POST /borrow
async def borrow_book(user: str, book: str) -> str:
    print(f"{user} is trying to borrow {book}...")

    await asyncio.sleep(1)  # simulate delay

    if books.get(book):
        books[book] = False
        return f"{user} successfully borrowed {book}"
    else:
        return f"{book} is not available for {user}"

# Simulate POST /return
async def return_book(user: str, book: str) -> str:
    print(f"{user} is returning {book}...")

    await asyncio.sleep(1)  # simulate delay

    books[book] = True
    return f"{user} returned {book}"

# Main function to simulate multiple users
async def main() -> None:
    tasks = [
        borrow_book("Alice", "math_book"),
        borrow_book("Bob", "math_book"),   # conflict!
        return_book("Alice", "math_book"),
        borrow_book("Charlie", "math_book")
    ]

    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)
# Run
asyncio.run(main())