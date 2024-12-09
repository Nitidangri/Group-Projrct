import pandas as pd
import sqlite3

data = pd.read_csv('../data_collection/cleaned_gym_data.csv')
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS gym_data (
    Age INTEGER,
    Gender TEXT,
    Weight_kg REAL,
    Height_m REAL,
    Max_BPM INTEGER,
    Avg_BPM INTEGER,
    Resting_BPM INTEGER,
    Session_Duration_hours REAL,
    Calories_Burned INTEGER,
    Workout_Type TEXT,
    Fat_Percentage REAL,
    Water_Intake_liters REAL,
    Workout_Frequency_days_per_week INTEGER,
    Experience_Level INTEGER,
    BMI REAL
)
''')
data.to_sql('gym_data', conn, if_exists='replace', index=False)

print("Database created and data inserted successfully!")

conn.close()