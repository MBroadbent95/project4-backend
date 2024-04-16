from app import app, db
from models.recipe import RecipeModel
from models.comment import CommentModel
from models.user import UserModel

with app.app_context():

    try:
        print("Connected to our database")

        db.drop_all()

        db.create_all()

        nick = UserModel(
            username="nick",
            email="nick@nick.com",
            password="meditate",
        )
        db.session.add(nick)
        db.session.commit()

        thai_green_curry = RecipeModel(
            name="Thai Green Curry",
            cuisine="Thai",
            serving="4 servings",
            prep_time="20 mins",
            total_time="35 mins",
            cal_serv=400,
            ingredients="a bunch of ingredients",
            directions_instructions="Step 1 - Make the food",
            image_url="https://i.imgur.com/mdkcaBa.jpg",
            user_id=nick.id,
        )

        db.session.add(thai_green_curry)
        db.session.commit()

        comment = CommentModel(
            content="Amazing taste.", recipe_id=thai_green_curry.id, user_id=nick.id
        )
        comment.save()

        print("Seeding some data")

    except Exception as e:
        print(e)
