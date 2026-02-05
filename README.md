# Flask + SQLite Interview Exercise

## Setup Instructions

### 1. Install UV Package Manager

This project uses [UV](https://docs.astral.sh/uv/) for packaging and dependency management. Install UV by following the [official installation guide](https://docs.astral.sh/uv/).

### 2. Install Project Dependencies

After cloning the repository, install all required dependencies:

```bash
uv sync
```

### 3. Start the Development Server

Run the Flask application with:

```bash
uv run python -m python_interview.main run
```

## Project Overview

You'll be working with a simple Flask application that uses a SQLite database. This setup mirrors patterns we use in our internal tools.

**Important notes:**

- The database resets to a clean state each time the app starts (for testing convenience)
- Database table schemas are defined in `schema.sql`
- Initial sample data is loaded from `seed.sql` on startup

## Exercise Guidelines

- **Internet usage:** You may freely use online resources and documentation
- **AI tools:** Please do not use AI chatbots or coding assistants during this exercise

______________________________________________________________________

## Tasks

### Task 1: Test Existing API Endpoints

**Goal:** Familiarize yourself with the application by interacting with the existing `/users` endpoint. Note that
this step will be useful for subsequent tasks, so make sure to save the request for later use.

**Steps:**

1. Start the application (see setup instructions above)

1. Send a `GET` request to `/users` to view all existing users

   - Use your preferred tool: `curl`, Postman, or a Python script with `requests`
   - Review the response to understand the user data structure

1. Send a `POST` request to `/users` to create a new user

   - Include appropriate user information in the request body

4.Send another `GET` request to `/users` to verify your new user was successfully added

### Task 2: Design a License Table Schema

**Goal:** Extend the database schema by adding a new `license` table.

**Requirements:**

Update `schema.sql` to include a `license` table with the following:

- A license key field (unique text string, maximum 128 characters)
- Additional attributes you think would be useful for tracking issued licenses

**Consider:** What information would be valuable to store about a license? Think about relationships to users, expiration, status, etc.

### Task 3: Implement License creation Endpoint

**Goal:** Create a new API endpoint that generates and stores a license for a specific user.

**Requirements:**

1. Implement a new endpoint: `POST /users/<int:user_id>/licenses`

   - Add this to `routes/licenses.py`
   - Register the route with the Flask app

1. Use the provided `generate_license_key()` function (already in the file) to create the license key

1. Return a JSON response containing:

   - The generated license key
   - The user ID

### Task 4: Implement endpoint for listing Licenses of a given user

**Goal:** Create a new API endpoint that lists all licenses of a given user.

**Requirements:**

1. Implement a new endpoint: `GET /users/<int:user_id>/licenses`

   - Add this to `routes/licenses.py`
   - Register the route with the Flask app

1. Use the provided `generate_license_key()` function (already in the file) to create the license key

1. Return a JSON response containing list of licenses of the given user.

### Task 5: Error Handling

**Goal:** Add error handling to all `POST` methods.

**Requirements:**

Implement error handling that provides clear, informative messages to help users understand what went wrong. Consider scenarios where database queries might fail and handle them appropriately.

### Task 6: Third-Party API Integration

**Goal:** Integrate a random user generator API to populate test data.

**Requirements:**

1. Implement a new endpoint: `POST /users/randomuser`

   - Add this to `routes/users.py`
   - Register the route with the Flask app

1. Use the [Random User API](https://randomuser.me/api/) to generate a random user, parse the response, and insert it into the database. Return the inserted user as a JSON response.

1. Verify that the random user was successfully added to the database by sending a GET request to `/users`.

### Task 7: Testing

**Goal:** Write a simple test with `pytest` for the `/users/randomuser` endpoint in `tests/`. Think about what code you want to test.

You can run the test as follows:

```bash
uv run pytest
```

______________________________________________________________________

## Need Help?

If you have questions about the requirements or encounter technical issues, please don't hesitate to ask!
