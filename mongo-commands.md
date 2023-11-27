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
