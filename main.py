from app import create_app

app = create_app()


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}

# app.include_router(
#     admin.router,
#     prefix="/admin",
#     tags=["admin"],
#     deps=[Depends(get_token_header)],
#     responses={418: {"description": "I'm a teapot"}},
# )
