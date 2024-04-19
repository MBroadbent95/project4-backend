import os

db_URI = os.getenv(
    "DATABASE_URL", "postgresql://postgres:Spartan117@localhost:4000/recipedb"
)
SECRET = os.getenv("SECRET", "smokeyrexchangedmyoil")

if db_URI.startswith("postgres://"):
    db_URI = db_URI.replace("postgres://", "postgresql://", 1)
