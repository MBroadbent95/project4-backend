import json
import pytest
from app import app, db
from models.user import UserModel
from models.recipe import RecipeModel

# ! Import your models to seed in your fixture


@pytest.fixture(autouse=True)
def setup():
    with app.app_context():
        try:

            db.create_all()

            user = UserModel(
                username="Nick", email="nick@nicky.com", password="nick123"
            )

            db.session.add(user)
            db.session.commit()

            recipes_list = [
                RecipeModel(
                    name="Thai Green Curry",
                    serving="4 servings",
                    prep_time="20 mins",
                    total_time="35 mins",
                    cal_serv=400,
                    ingredients="a bunch of ingredients",
                    directions_instructions="Step 1 - Make the food",
                    user_id=1,
                ),
                RecipeModel(
                    name="Thai Red Curry",
                    serving="3 servings",
                    prep_time="15 mins",
                    total_time="30 mins",
                    cal_serv=350,
                    ingredients="a bunch of other ingredients",
                    directions_instructions="Step 1 - Start making the food",
                    user_id=1,
                ),
            ]

            db.session.add_all(recipes_list)
            db.session.commit()

            yield

            db.drop_all()

        except Exception as e:
            print("There was an error.")
            print(e)


def login(client):

    login_data = {
        "email": "nick@nicky.com",
        "password": "nick123",
    }
    print(login_data)
    response = client.post(
        "/api/login", data=json.dumps(login_data), content_type="application/json"
    )
    print("Response Status Code:", response.status_code)
    # Print response JSON
    return response.json["token"]
