-- Retrieve all users who have placed an order
SELECT DISTINCT id, name, email
FROM users
INNER JOIN orders ON users.id = orders.user_id;

-- Retrieve the total number of orders placed by each user
SELECT id, name, email, COUNT(orders.id) AS total_orders
FROM users
LEFT JOIN orders ON users.id = orders.user_id
GROUP BY id, name, email;

-- Find the top 5 products ordered by quantity
SELECT product_name, SUM(quantity) AS total_quantity
FROM orders
GROUP BY product_name
ORDER BY total_quantity DESC
LIMIT 5;

-- Find users who have not placed any orders
SELECT id, name, email
FROM users
LEFT JOIN orders ON id = user_id
WHERE user_id IS NULL;
