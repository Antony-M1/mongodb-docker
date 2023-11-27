# Commands

### Connect The CLI
username: `root`

passwor: `123`
```
docker exec -it mongo mongosh -u <username> -p <password> --authenticationDatabase admin
```
**Run the below commands in CLI and Play**

### List the all database
```
show dbs
```
or
In the MongoDB shell, `db` is an object that represents the current database context. It allows you to interact with the database, run queries, and perform various operations.
```
db.getMongo().getDBs()
```

### Create New Database
```
use <DATABASE_NAME>
```
example
```
use my-mongo
```
If already the DB exists it will switch the `DB` if not exists it will `Create` the DB.
After Running this command you can check in the `show dbs` command or in `Mongo Express` [localhost:8081](localhost:8081). if not there create the collection after try.

### Create The Collection
A collection is a grouping of MongoDB documents. Documents within a collection can have different fields. A collection is the equivalent of a table in a relational database system. A collection exists within a single database.
```
db.createCollection("product_list")
```
If the collection is created successfully, it will return `{ "ok" : 1 }`.

### List Collections in the Current Database
```
show collections
```
---
### CRUD Operations in Collections
*Note: Over Here I'm Using The `product_list` Collection*

**Add New Document**
```
db.product_list.insert({product_id:1, product_name:"Foot Ball", price:500})
```
**Get Document**
```
db.product_list.find({ product_name: 'Foot Ball' })
```
Type of Fetch:
* find
* findOne

**Update Documents**

Every Document Had `Unique` value `_id` in that field only the `Unique` value will be created. to get that you can check the Mongo Express.

![image](https://github.com/Antony-M1/mongodb-docker/assets/96291963/5f076943-4c3d-4569-a6bc-c190bfe2b79a)

```
db.product_list.updateOne(
   { _id: ObjectId('6564939c38e306b1860a50b1') },
   { $set: { price: 600 } }
)
```
Types of Update
* updateOne
* updateMany
* replaceOne
* findOneAndUpdate

**Delete Document**
```
db.product_list.deleteOne({ _id: ObjectId('6564939c38e306b1860a50b1') })
```
Types of Delete:
* deleteOne
* deleteMany
---

MongoDB is a NoSQL database that is known for its flexibility in handling various types of data. In MongoDB, data is stored in BSON (Binary JSON) format, which is a binary representation of JSON-like documents. MongoDB supports a variety of data types. Here are some of the primary data types supported by MongoDB:

1. **String:**
   - Holds UTF-8 character sequences.
   - Example: `"Hello, MongoDB"`

2. **Integer:**
   - Represents a 32-bit signed integer.
   - Example: `42`

3. **Double:**
   - Represents a 64-bit floating-point value.
   - Example: `3.14`

4. **Boolean:**
   - Represents `true` or `false`.
   - Example: `true`

5. **ObjectId:**
   - A 12-byte identifier typically employed as a primary key.
   - Example: `ObjectId("507f1f77bcf86cd799439011")`

6. **Date:**
   - Represents a point in time, typically expressed as the number of milliseconds since the Unix epoch.
   - Example: `ISODate("2023-04-10T12:00:00Z")`

7. **Array:**
   - Holds an ordered collection of values.
   - Example: `["apple", "orange", "banana"]`

8. **Embedded Document:**
   - Allows you to nest documents inside other documents.
   - Example: `{ name: "John", age: 30, address: { city: "New York", state: "NY" } }`

9. **Binary Data:**
   - Represents binary data, such as images or other types of files.
   - Example: `BinData(0, "aGVsbG8=")` (Base64-encoded string)

10. **Null:**
    - Represents a null or undefined value.
    - Example: `null`

11. **Regular Expression:**
    - Represents a regular expression for pattern matching.
    - Example: `/^mongodb/i`

12. **JavaScript Code:**
    - Represents JavaScript code.
    - Example: `function() { return "Hello, MongoDB!"; }`

These data types can be used to model a wide range of structures and relationships within MongoDB. It's important to note that MongoDB is schema-free, meaning that documents in the same collection can have different fields and structures. This flexibility is one of the key advantages of MongoDB for handling diverse and evolving data.
