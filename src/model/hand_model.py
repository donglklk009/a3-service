from entity.request import HandReq
from entity.response import Response


def process(req: HandReq) -> Response:
    return Response(
        code=0,
        message="OK",
        data=req
    )
