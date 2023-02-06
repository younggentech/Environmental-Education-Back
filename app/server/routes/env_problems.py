import bson
from fastapi import APIRouter, Body, HTTPException
from fastapi.encoders import jsonable_encoder

from app.server.database import (
    retrieve_problem,
    delete_problem,
    add_problem,
    retrieve_problems,
    update_problem,
)
from app.server.models.env_problems import (
    ErrorResponseModel,
    ResponseModel,
    ProblemSchema,
    UpdateProblemModel,
)

router = APIRouter()


@router.post("/", response_description="Problem data added into the database")
async def add_environmental_problem_data(problem: ProblemSchema = Body(...)):
    problem = jsonable_encoder(problem)
    new_problem = await add_problem(problem)
    return ResponseModel(new_problem, "Success")


@router.get("/", response_description="Retrieve all problems from the database")
async def get_environmental_problems():
    problems = await retrieve_problems()
    if problems:
        return ResponseModel(problems, "Success")
    return ResponseModel(problems, "Empty")


@router.get("/{problem_id}", response_description="Retrieve a problem based on it's ID")
async def get_environmental_problem(problem_id: str):
    try:
        problem = await retrieve_problem(problem_id)
    except bson.errors.InvalidId:
        raise HTTPException(status_code=400, detail="ID must be a 12-byte input or a 24-character hex string")
        # return ErrorResponseModel("Bad Request", 400, "ID must be a 12-byte input or a 24-character hex string")
    if problem:
        return ResponseModel(problem, "Success")
    raise HTTPException(404, "Not found")


@router.put("/{problem_id}", response_description="Update a problem by its ID")
async def update_environmental_problem(problem_id: str, req: UpdateProblemModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_problem = await update_problem(problem_id, req)
    if updated_problem:
        return ResponseModel(
            "Problem with ID: {} name update is successful".format(problem_id),
            "Success",
        )
    raise HTTPException(404, "Problem not found")


@router.delete("/{problem_id}", response_description="Problem data deleted from the database")
async def delete_environmental_problem(problem_id: str):
    deleted_problem = await delete_problem(problem_id)
    if deleted_problem:
        return ResponseModel(
            "Poblem with ID: {} removed".format(problem_id), "Success"
        )
    raise HTTPException(404, f"Not found")
