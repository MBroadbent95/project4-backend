import os

db_URI = os.getenv(
    "DATABASE_URL",
    "postgresql://recipedb_lrqc_user:jx4mYbhpVgNV7xnpMzJ4rCkBhhUghLVm@dpg-cvda56an91rc73deiseg-a.frankfurt-postgres.render.com/recipedb_lrqc",
)
SECRET = os.getenv("SECRET", "smokeyrexchangedmyoil")

if db_URI.startswith("postgres://"):
    db_URI = db_URI.replace("postgres://", "postgresql://", 1)
