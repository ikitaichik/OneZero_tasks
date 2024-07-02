# Simple Item API with Flask
 This Flask app provides a basic API for managing items in memory.

**Features:**
- Stores items with name, description, and creation date.
- Offers CRUD operations (Create, Read, Update, Delete) via RESTful API endpoints.
- Validates input data using pydantic models.
- Logs CRUD operations for tracking.

**Installation::**
- Python 3.x 
- pip install pydantic


**Run the App:**
1. Save code as app.py.
2. Open a terminal in the same directory and run:
  ```bash
  python app.py
  ```

**API Endpoints:**

1. List All Items (GET /items):
    - Returns a JSON list of all items.
    - ```JSON
      [
        {
          "id": 0,
          "name": "Item 1",
          "description": "",
          "created_at": "2024-07-02T10:24:00+00:00"
        },
        {
          "id": 1,
          "name": "Another Item",
          "description": "This is a longer description",
          "created_at": "2024-07-02T10:24:01+00:00"
        }
      ]
      ```
2. Create a New Item (POST /items):
    - Create a new item with JSON data in the request body (name required, description optional).
    - Request Body (JSON):
      ```JSON
      {
        "name": "New Item Name"  # Required field
        "description": "Optional description"  # Optional field
      }
      ```
3. Get Item Details (GET /items/<id>):
    - Retrieve details of a specific item by its ID.
    - ```JSON
      {
        "id": 1,
        "name": "Another Item",
        "description": "This is a longer description",
        "created_at": "2024-07-02T10:24:01+00:00"
      }
      ```
4. Update Item (PUT /items/<id>):
    - Update an item's details with JSON data in the request body (optional fields).
    - Request Body (JSON):
      ```JSON
      {
        "name": "New Item Name"  # Required field
        "description": "Optional description"  # Optional field
      }
      ```
5. Delete Item (DELETE /items/<id>):
    - Delete a specific item by its ID.
    - Successful Response (204 No Content):
