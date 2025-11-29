def model_document(model_id, name, owner, tags, version):
    return {
        "model_id": model_id,
        "name": name,
        "owner": owner,
        "tags": tags,
        "version": version
    }
