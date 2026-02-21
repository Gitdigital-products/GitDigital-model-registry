storage = StorageManager()

@app.get("/models/{name}/{version}/upload-link")
def get_upload_link(name: str, version: str):
    """Get a one-time link to upload the model artifact."""
    upload_data = storage.generate_upload_url(name, version)
    if not upload_data:
        raise HTTPException(status_code=500, detail="Could not generate upload link")
    return upload_data
