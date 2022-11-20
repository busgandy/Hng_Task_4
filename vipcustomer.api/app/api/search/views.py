from fastapi import APIRouter, HTTPException, Depends
from .schemas import SearchResponseSchema, SearchParamsSchema, SearchListSchema
from .services import SearchService
from typing import List

router = APIRouter()


@router.get("/", response_model=List[SearchResponseSchema])
async def search_vips(params: SearchParamsSchema = Depends()):

    try:
        print(params.name)
        search_service = SearchService()
        resp = await search_service.search(
            {
                "name": params.name,
                "gender": params.gender,
                "occupation": params.occupation,
                "age": params.age,
                "email": params.email,
            }
        )

        return resp

    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500,
            detail="An error occurred while validating VIP",
        )


@router.post("/search-many")
async def search_vip_list(params: SearchListSchema):
    try:
        data = [i.__dict__ for i in params.data]
        search_service = SearchService()
        resp = await search_service.search(data)
        return resp

    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=500,
            detail="An error occurred while validating VIP",
        )
