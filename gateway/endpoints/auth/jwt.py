from dataclasses import asdict

from fastapi import Depends
from fastapi.responses import JSONResponse
from fastapi_versioning import version
from dependency_injector.wiring import Provide, inject

from auth_grpc_typed import IAuthStub, RefreshTokensRequest
from config.di import Container
from schemas import JWTTokensSchema, RefreshTokensSchema
from utils.routing import CustomAPIRouter


router = CustomAPIRouter(prefix="/auth/jwt")


@router.post(
    "/refresh/",
    response_model=JWTTokensSchema,
    status_code=200,
)
@version(1)
@inject
async def refresh(
    schema: RefreshTokensSchema,
    auth_grpc: IAuthStub = Depends(Provide[Container.auth_grpc]),
):
    response = await auth_grpc.jwt_refresh(
        request=RefreshTokensRequest(refresh=schema.refresh)
    )
    return JSONResponse(
        asdict(JWTTokensSchema(access=response.access, refresh=response.refresh))
    )
