import weaviate
from weaviate.auth import AuthApiKey

client = weaviate.connect_to_local(auth_credentials=AuthApiKey("user-a-key"))
try:
    print("is_ready:", client.is_ready())  # Should print: `True`

    # data insert
    questions = client.collections.get("JeopardyQuestion")
    new_uuid = questions.data.insert(
        properties={
            "question": "This is the capital of Australia."
        },
        references={  # For adding cross-references
            "hasCategory": "target_uuid"
        }
    )
    print("new_uuid:", new_uuid)

    # query
    response = questions.query.bm25(
        query="animal",
        limit=2
    )
    for o in response.objects:
        print(o.properties)  # Object properties
finally:
    client.close()  # Free up resources
