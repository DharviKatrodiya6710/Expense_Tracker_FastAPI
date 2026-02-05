
DB_USER = "postgres"
DB_PASSWORD = "dharvi"        
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "Expense_Tracker_System"

DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

SECRET_KEY = "SUPER_SECRET_KEY_CHANGE_ME"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60
