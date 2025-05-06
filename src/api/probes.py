from fastapi import APIRouter, status

router = APIRouter()

@router.get(
    "/-/check-up",
    status_code=status.HTTP_200_OK,
    include_in_schema=False,
)
async def readiness():
    """
    This route can be used as check-up route, to verify if all the
    functionalities of the service are available or not. The purpose of this
    route should be to check the availability of all the dependencies of the
    service and reply with a check-up of the service. By default, the route will
    always response with an OK status and the 200 HTTP code as soon as the
    service is up.
    """

    return {"statusOk": True}


@router.get(
    "/-/ready",
    status_code=status.HTTP_200_OK,
    include_in_schema=False,
)
async def readiness():
    """
    This route can be used as a readinessProbe for Kubernetes. By default, the
    route will always response with an OK status and the 200 HTTP code as soon
    as the service is up.
    """

    return {"statusOk": True}



@router.get(
    "/-/healthz",
    status_code=status.HTTP_200_OK,
    include_in_schema=False,
)
async def liveness():
    """
    This route can be used as a probe for load balancers, status dashboards and
    as a helthinessProbe for Kubernetes. By default, the route will always
    response with an OK status and the 200 HTTP code as soon as the service is
    up.
    """

    return {"statusOk": True}
