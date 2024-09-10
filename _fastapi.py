import uvicorn
from fastapi import FastAPI
from typing import List
from pymongo import MongoClient
import strawberry
from strawberry.asgi import GraphQL

mongo_uri = "mongodb://root:123@localhost:27017/?retryWrites=true&w=majority"
client = MongoClient(mongo_uri)

# Connecting db
db = client.sample_mflix

# Connecting to specific collection
collection = db.movies

# data = collection.find_one()

# print(data)

app = FastAPI()

@strawberry.type
class Movie:
    id: str
    title: str
    plot: str


# Query class for fetching data
@strawberry.type
class Query:
    @strawberry.field
    def movies(self) -> List[Movie]:
        movies = []
        for movie_data in collection.find():
            if len(movies) == 25:
                break
            movie = Movie(id=movie_data["_id"], title=movie_data["title"], plot=movie_data["plot"])
            movies.append(movie)
        return movies

    @strawberry.field
    def movie(self, id: str) -> Movie:
        movie_data = collection.find_one({"_id": id})
        if movie_data:
            return Movie(id=movie_data["_id"], title=movie_data["title"], plot=movie_data["plot"])
        else:
            return None
        

# Mutation for write operations
@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_movie(self, id: str, title: str, plot: str) -> Movie:
        movie = {"_id": id, "title": title, "plot": plot}
        collection.insert_one(movie)
        return Movie(title=movie["title"], plot=movie["plot"])

    @strawberry.mutation
    def update_movie(self, id: int, title: str, plot: str) -> Movie:
        collection.update_one({"id": id}, {"$set": {"title": title}}, {"$set": {"plot": plot}})
        updated_movie = collection.find_one({"id": id})
        return Movie(id=updated_movie["id"], title=updated_movie["title"], plot=updated_movie["plot"])

    @strawberry.mutation
    def delete_movie(self, id: int) -> Movie:
        deleted_movie = collection.find_one_and_delete({"id": id})
        return Movie(id=deleted_movie["id"], name=deleted_movie["title"])


schema = strawberry.Schema(query=Query, mutation=Mutation)

app.mount("/graphql", GraphQL(schema, debug=True))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)