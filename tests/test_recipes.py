import json

from app import app, db

from tests.lib import login, setup


def test_gets_recipes():

    client = app.test_client()

    response = client.get("/api/recipes")

    print(response.json)

    assert len(response.json) == 2
    assert response.status_code == 200
    assert response.json[0]["name"] == "Thai Green Curry"


def test_create_recipe():

    client = app.test_client()

    token = login(client)

    recipe_data = {
        "name": "Thai yellow Curry",
        "serving": "3 servings",
        "prep_time": "25 mins",
        "total_time": "40 mins",
        "cal_serv": 500,
        "ingredients": "lots of ingredients",
        "directions_instructions": "Step uno - Make the food",
        "user_id": 1,
    }

    request_headers = {"Authorization": f"Bearer {token}"}

    response = client.post(
        "/api/recipes",
        data=json.dumps(recipe_data),
        content_type="application/json",
        headers=request_headers,
    )
    print(response.json)


def test_delete_recipe():

    client = app.test_client()

    token = login(client)

    recipe_data = {
        "name": "Thai yellow Curry",
        "serving": "3 servings",
        "prep_time": "25 mins",
        "total_time": "40 mins",
        "cal_serv": 500,
        "ingredients": "lots of ingredients",
        "directions_instructions": "Step uno - Make the food",
    }

    request_headers = {"Authorization": f"Bearer {token}"}

    response = client.post(
        "/api/recipes",
        data=json.dumps(recipe_data),
        content_type="application/json",
        headers=request_headers,
    )
    assert response.status_code == 200

    recipe_id = response.json["id"]

    response = client.delete(
        f"/api/recipes/{recipe_id}",
        headers=request_headers,
    )
    assert response.status_code == 200

    response = client.get(f"/api/recipes/{recipe_id}")
    assert response.status_code == 404


def test_put_recipe():
    client = app.test_client()

    token = login(client)

    recipe_data = {
        "name": "Thai yellow Curry",
        "serving": "3 servings",
        "prep_time": "25 mins",
        "total_time": "40 mins",
        "cal_serv": 500,
        "ingredients": "lots of ingredients",
        "directions_instructions": "Step uno - Make the food",
    }

    request_headers = {"Authorization": f"Bearer {token}"}

    response = client.post(
        "/api/recipes",
        data=json.dumps(recipe_data),
        content_type="application/json",
        headers=request_headers,
    )
    assert response.status_code == 200

    recipe_id = response.json["id"]

    updated_recipe_data = {
        "name": "Thai blue Curry",
        "serving": "2 servings",
        "prep_time": "30 mins",
        "total_time": "45 mins",
        "cal_serv": 600,
        "ingredients": "tons of ingredients",
        "directions_instructions": "just Make the food",
        "user_id": 1,
    }
    response = client.put(
        f"/api/recipes/{recipe_id}",
        data=json.dumps(updated_recipe_data),
        content_type="application/json",
        headers=request_headers,
    )
    assert response.status_code == 200

    response = client.get(f"/api/recipes/{recipe_id}")
    assert response.status_code == 200
    crisp = response.json
    assert crisp["name"] == updated_recipe_data["name"]
    assert crisp["prep_time"] == updated_recipe_data["prep_time"]
    assert (
        crisp["directions_instructions"]
        == updated_recipe_data["directions_instructions"]
    )
