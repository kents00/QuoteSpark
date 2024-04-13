# QuoteSpark

![home](https://github.com/kents00/QuoteSpark/assets/69900896/2f4bf3b0-52b1-4b8f-bdfa-10736a5800ba)

QuoteSpark is a powerful tool for generating motivational quotes, offering an extensive collection of inspiring words from influential figures across different eras. With its vast database, QuoteSpark ensures that you can always find the perfect quote to uplift and motivate yourself or others.

### Installation

```bash
// Clone the repository
git clone https://github.com/kents00/QuoteSpark.git

// installing requirements
pip install -r requirements.txt

//run into your local machine
flask --app app run
```

The application will be accessible at **`http://127.0.0.1:5000/`** in your web browser.

### API

This project provide a simple API for getting quotes and accessing motivational content.

**api/quotes**:

- **GET**: Returns a list of all quotes available in the database.
- Usage: **`GET /api/quotes`**
- Example response:

    ```json
    [
    {"quote": "Quote 1", "author": "Author 1"},
    {"quote": "Quote 2", "author": "Author 2"}
    ]
    ```


**/api/random**:

- **GET**: Returns a randomly selected quote from the database.
- Usage: **`GET /api/random`**
- Example response:

    ```json
    {"quote": "Random Quote", "author": "Random Author"}
    ```


**/api/author/<author>**:

- **GET**: Returns a list of quotes by the specified author.
- Usage: **`GET /api/author/Dalai Lama`**
- Example response:

    ```json
    [
    {"quote": "Quote 1", "author": "Author 1"},
    {"quote": "Quote 2", "author": "Author 2"}
    ]
    ```
