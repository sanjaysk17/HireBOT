from fastapi.middleware.cors import CORSMiddleware

def setup_cors(app):
    """Enable CORS for all origins."""
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
