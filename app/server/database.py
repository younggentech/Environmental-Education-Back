from bson.objectid import ObjectId
import motor.motor_asyncio
import dotenv
import os

dotenv.load_dotenv()

MONGO_DETAILS = os.environ["DB_PROD"]

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
database = client.default_db
problems_collection = database.get_collection("env_problems")


def env_problems_helper(problem) -> dict:
    return {
        "id": str(problem["_id"]),
        "heading": problem["heading"],
        "text": problem["text"],
        "img": problem["img"],
    }


# Retrieve all problems present in the database
async def retrieve_problems():
    problems = []
    async for problem in problems_collection.find():
        problems.append(env_problems_helper(problem))
    return problems


# Add a new problem into to the database
async def add_problem(problem_data: dict) -> dict:
    problem = await problems_collection.insert_one(problem_data)
    new_problem = await problems_collection.find_one({"_id": problem.inserted_id})
    return env_problems_helper(new_problem)


# Retrieve a problem with a matching ID
async def retrieve_problem(_id: str) -> dict:
    problem = await problems_collection.find_one({"_id": ObjectId(_id)})
    if problem:
        return env_problems_helper(problem)


# Update a problem with a matching ID
async def update_problem(_id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    problem = await problems_collection.find_one({"_id": ObjectId(_id)})
    if problem:
        updated_student = await problems_collection.update_one(
            {"_id": ObjectId(_id)}, {"$set": data}
        )
        if updated_student:
            return True
        return False


# Delete a student from the database
async def delete_problem(_id: str):
    problem = await problems_collection.find_one({"_id": ObjectId(_id)})
    if problem:
        await problems_collection.delete_one({"_id": ObjectId(_id)})
        return True
