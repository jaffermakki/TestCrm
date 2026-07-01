@router.post(
    "/login",
    response_model=TokenResponse,
)
async def login(

    request: LoginRequest,

    db: AsyncSession = Depends(get_db),

):

    service = AuthenticationService(

        UserRepository(db)

    )

    return await service.login(

        request.email,

        request.password,

    )
