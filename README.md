---

# Add Two Numbers API

This Flask-based API is designed to perform addition of two numbers using OpenAI's GPT-3.5 model. It accepts two numbers as input and utilizes the chat capabilities of GPT-3.5 to compute the addition result.

## Getting Started

To run this API locally, follow these steps:

### Prerequisites

- Python 3.x
- OpenAI Python package
- Flask
- [OpenAI API Key](https://platform.openai.com/account/api-keys)

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Adinyk03/add_2_no.git
   cd add_2_no
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:

   Replace `"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"` in `app.py` with your actual API key.

### Usage

1. Run the Flask application:

   ```bash
   python app.py
   ```

2. Send a POST request to the `/add` endpoint with JSON data containing `num1` and `num2` keys, representing the two numbers you want to add.

   Example:

   ```bash
   curl -X POST -H "Content-Type: application/json" -d '{"num1": 5, "num2": 10}' http://localhost:5099/add
   ```

## API Endpoints

### `POST /add`

- **Description:** Adds two numbers using GPT-3.5
- **Request Body:**
  ```json
  {
    "num1": 5,
    "num2": 10
  }
  ```
- **Response:**
  ```json
  {
    "result": 15
  }
  ```

## Caveats and Notes

- The API expects valid integer inputs for `num1` and `num2`.
- If invalid inputs are provided, an error message will be returned.
- The addition operation is performed using GPT-3.5 and might not always produce accurate results.


## License

This project is licensed under the [MIT License](LICENSE).

---
