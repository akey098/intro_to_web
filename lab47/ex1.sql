-- Step 1: Create a new database
CREATE DATABASE my_app_db;

-- Step 2: Create a new user and grant permissions
CREATE USER my_app_user WITH PASSWORD 'securepassword';
GRANT ALL PRIVILEGES ON DATABASE my_app_db TO my_app_user;

-- (Optional: List databases and users to verify)
-- \l
-- \du

-- Step 3: Connect to the database (done from the terminal, not SQL)
-- \q  ← exit current session
-- Then from terminal:
-- psql -U my_app_user -d my_app_db

-- The following steps are done **after connecting** to my_app_db as my_app_user

-- Step 4: Create a table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Step 5: Insert data
INSERT INTO users (name, email) VALUES
('Alice Smith', 'alice@example.com'),
('Bob Jones', 'bob@example.com');

-- Step 5: Query data
SELECT * FROM users;
