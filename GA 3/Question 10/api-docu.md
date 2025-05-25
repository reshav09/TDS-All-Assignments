Sure! Here's the requested Markdown file with the full documentation for the FastAPI service you just described.

---

### `api_documentation.md`

```markdown
# FastAPI Query Parsing Service Documentation

This FastAPI service parses various types of natural language queries, extracts relevant parameters, and executes the corresponding action. It supports queries related to:

- Ticket status
- Meeting scheduling
- Expense balance
- Performance bonuses
- Office issue reports

## Endpoints

### `/execute`
This endpoint receives a query and attempts to parse it using different functions for various types of queries. If a match is found, it returns the parsed parameters as a JSON response.

#### Method: `GET`

##### Query Parameters:
- `q` (required): The query string that needs to be parsed.

Example of a query:
```

GET /execute?q=schedule meeting for 2023-05-30 at 10:00 in Room A

````

#### Response:
- **Success**: If a query is successfully parsed, a JSON object will be returned with the corresponding parameters.

Example:
```json
{
  "name": "schedule_meeting",
  "arguments": "{\"date\": \"2023-05-30\", \"time\": \"10:00\", \"meeting_room\": \"Room A\"}"
}
````

* **Failure**: If no parser matches the query, an error message is returned.

Example:

```json
{
  "error": "Could not parse query"
}
```

#### Error Codes:

* **400 Bad Request**: The query parameter `q` is missing or invalid.
* **500 Internal Server Error**: If there is an issue during the parsing process.

## Query Types

### 1. **Ticket Status Query**:

* **Description**: Retrieves the status of a specific ticket based on its ID.
* **Example Query**: `What is the status of ticket 12345?`
* **Parsed Result**:

  ```json
  {
    "name": "get_ticket_status",
    "arguments": "{\"ticket_id\": 12345}"
  }
  ```

### 2. **Meeting Scheduling Query**:

* **Description**: Schedules a meeting with a specific date, time, and room.
* **Example Query**: `Schedule meeting for 2023-05-30 at 10:00 in Room A`
* **Parsed Result**:

  ```json
  {
    "name": "schedule_meeting",
    "arguments": "{\"date\": \"2023-05-30\", \"time\": \"10:00\", \"meeting_room\": \"Room A\"}"
  }
  ```

### 3. **Expense Balance Query**:

* **Description**: Retrieves the expense balance for a specific employee.
* **Example Query**: `What is the expense balance for employee 5678?`
* **Parsed Result**:

  ```json
  {
    "name": "get_expense_balance",
    "arguments": "{\"employee_id\": 5678}"
  }
  ```

### 4. **Performance Bonus Query**:

* **Description**: Retrieves the performance bonus for a specific employee in a given year.
* **Example Query**: `What is the bonus for employee 1234 in 2025?`
* **Parsed Result**:

  ```json
  {
    "name": "calculate_performance_bonus",
    "arguments": "{\"employee_id\": 1234, \"current_year\": 2025}"
  }
  ```

### 5. **Office Issue Report Query**:

* **Description**: Reports an office issue in a specific department.
* **Example Query**: `Report issue 202 in the HR dept`
* **Parsed Result**:

  ```json
  {
    "name": "report_office_issue",
    "arguments": "{\"issue_code\": 202, \"department\": \"HR\"}"
  }
  ```

## Setup and Run Instructions

### Prerequisites:

1. Install Python 3.7+.
2. Install the following dependencies:

   ```bash
   pip install fastapi uvicorn
   ```

### Running the Server:

1. Save the provided Python code to a file (e.g., `app.py`).
2. Run the FastAPI app using `uvicorn`:

   ```bash
   uvicorn app:app --reload --host 127.0.0.1 --port 8000
   ```

### Testing the API:

You can test the API by sending queries to the `/execute` endpoint. Here’s an example using `curl`:

```bash
curl -X 'GET' 'http://127.0.0.1:8000/execute?q=schedule meeting for 2023-05-30 at 10:00 in Room A'
```

### Example Responses:

* **Success**:

  ```json
  {
    "name": "schedule_meeting",
    "arguments": "{\"date\": \"2023-05-30\", \"time\": \"10:00\", \"meeting_room\": \"Room A\"}"
  }
  ```

* **Failure**:

  ```json
  {
    "error": "Could not parse query"
  }
  ```

## Logging

The application is configured to log detailed information about the queries received, including the request headers and the parsed results. This helps to trace the execution flow.

---

### Key Points in the Markdown:
- **API Overview**: The markdown starts by describing the core purpose of the service.
- **Endpoint Details**: Provides a full description of the `/execute` endpoint, the query parameter, and example responses.
- **Query Types**: Lists and explains the types of queries the API can parse (ticket status, meeting scheduling, etc.).
- **Setup Instructions**: Describes how to install dependencies, run the FastAPI app, and test it with `curl`.
- **Logging**: Mentions that logging is enabled to trace queries and responses.

