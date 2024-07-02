from pymongo import MongoClient

try:
  client = MongoClient("mongodb://localhost:27017/")
  db = client["your_database_name"]  
  collection = db["users"]

  # Data Insertion:
  # Insert a document into a collection named users with fields name, email, and age.
  new_user = {"name": "John Doe", "email": "john.doe@example.com", "age": 30}
  try:
    result = collection.insert_one(new_user)
    print("User inserted successfully:", result.inserted_id)
  except Exception as e:
    print("Error inserting user:", e)
  
  # Data Retrieval:
  # Write a query to retrieve all documents from the users collection where the age is greater than 25.
  try:
    for user in collection.find({"age": {"$gt": 25}}):
      print(user)
  except Exception as e:
    print("Error retrieving users:", e)
  
  # Data Update:
  # Write a query to update the email of the user with name &quot;Dan Daniel&quot; to dan.daniel@example.com.
  try:
    result = collection.update_one({"name": "Dan Daniel"}, {"$set": {"email": "dan.daniel@example.com"}})
    if result.matched_count == 0:
      print("No user found with name 'Dan Daniel'")
    else:
      print(f"Updated email for {result.matched_count}")
  except Exception as e:
    print("Error updating user:", e)
  
  # Data Deletion
  # Write a query to delete all documents from the users collection where the age is less than 18.
  try:
    result = collection.delete_many({"age": {"$lt": 18}})
    
    print(f"Deleted {result.deleted_count} documents")
  except Exception as e:
    print("Error deleting users:", e)
except Exception as e:
  print("Error connecting to MongoDB:", e)
  exit(1)
finally:
  if client:
    client.close()
