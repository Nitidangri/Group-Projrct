# Gym Dataset Web Application

This project presents a Gym Workout Dataset and allows users to interact with the data through a simple web interface built using **Flask**. The dataset contains various health-related metrics from individuals' workout sessions, which can be used for analysis and visualization.

## Features

- **Home Page**: Displays the title, and allows users to navigate to the "About" and "Data" pages.
- **About Page**: Provides details about the dataset, including variable definitions and more context.
- **Data Page**: Displays the dataset in a table format, allowing users to explore various metrics related to workouts.
- **Responsive Design**: Optimized for both desktop and mobile devices.

## Technologies Used

- **Python**: Backend language used for building the Flask web application.
- **Flask**: Micro web framework used for developing the application.
- **SQLite**: Database used to store the gym dataset.
- **HTML/CSS**: Used for structuring and styling the front-end pages.
- **Jinja2**: Template engine used by Flask to render dynamic data in the HTML pages.

## Dataset Overview

This dataset contains valuable information about gym workouts, helping you track and analyze various health-related metrics.

### Variables:
- **Age**: Age of the individual
- **Gender**: Gender of the individual
- **Weight (kg)**: Weight of the individual in kilograms
- **Height (m)**: Height of the individual in meters
- **Max_BPM**: Maximum beats per minute reached during the workout
- **Avg_BPM**: Average beats per minute during the workout
- **Resting_BPM**: Resting beats per minute
- **Session_Duration (hours)**: Duration of the workout session in hours
- **Calories_Burned**: Number of calories burned during the session
- **Workout_Type**: Type of workout (Strength, Cardio, etc.)
- **Fat_Percentage**: Body fat percentage of the individual
- **Water_Intake (liters)**: Amount of water consumed (in liters)
- **Workout_Frequency (days/week)**: Frequency of workouts per week
- **Experience_Level**: Experience level of the individual (Beginner, Intermediate, Advanced)
- **BMI**: Body Mass Index of the individual

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <project-folder>
