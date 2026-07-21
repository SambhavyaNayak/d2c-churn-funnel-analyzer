CREATE TABLE users (
    user_id VARCHAR(20) PRIMARY KEY,
    signup_date DATE,
    acquisition_channel VARCHAR(50),
    country VARCHAR(50)
);

CREATE TABLE sessions (
    session_id VARCHAR(30) PRIMARY KEY,
    user_id VARCHAR(20),
    session_date DATE,
    device VARCHAR(20),
    session_duration INT,
    pages_visited INT
);

CREATE TABLE orders (
    order_id VARCHAR(20) PRIMARY KEY,
    user_id VARCHAR(20),
    order_date DATE,
    order_value NUMERIC(10,2),
    payment_method VARCHAR(20)
);

CREATE TABLE funnel_events (
    event_id SERIAL PRIMARY KEY,
    session_id VARCHAR(30),
    user_id VARCHAR(20),
    event_type VARCHAR(50),
    event_time TIMESTAMP
);