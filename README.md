# ai-student-performance-predictor
An AI-based student performance prediction system using Python and Machine Learning.
🎓 AI Student Performance Predictor

An Artificial Intelligence and Machine Learning Project

Developed by: Aayush Kumar
Course: B.Tech — First Year

---

📌 About the Project

The AI Student Performance Predictor is a beginner-friendly Artificial Intelligence and Machine Learning project designed to estimate a student's possible final examination score based on various academic and lifestyle factors.

The project uses a Random Forest Regression model to analyze information such as daily study hours, attendance percentage, previous examination scores, sleep duration, and assignment completion.

The application provides a simple, interactive web interface where users can enter their details and receive an estimated score.

This project demonstrates the practical application of Python, Machine Learning, data analysis, and web application development.

🎯 Project Objectives

- Understand the fundamentals of Artificial Intelligence and Machine Learning.
- Build a predictive model using Python.
- Learn how to prepare and process datasets.
- Apply regression techniques to estimate numerical values.
- Evaluate a machine learning model using performance metrics.
- Develop an interactive web application using Streamlit.
- Learn how to organize and publish a software project on GitHub.

✨ Features

- 🤖 AI-Based Prediction: Estimates a student's possible final examination score.
- 📚 Study Analysis: Uses daily study hours as an input.
- 📊 Attendance Analysis: Considers attendance percentage.
- 📝 Academic Performance: Includes previous examination scores.
- 😴 Sleep Duration: Considers sleep hours as an input feature.
- ✅ Assignment Tracking: Includes completed assignments.
- 📈 Model Evaluation: Displays Mean Absolute Error and R² score.
- 📉 Feature Importance: Visualizes the relative importance of model inputs.
- 💻 Interactive Interface: Provides an easy-to-use web application.
- 📂 Dataset Preview: Allows users to explore sample dataset records.

🛠️ Technologies Used

Technology| Purpose
Python| Main programming language
Pandas| Dataset handling and data analysis
Scikit-learn| Machine Learning model training and evaluation
Random Forest Regression| Predicting numerical examination scores
Streamlit| Building the interactive web application
Matplotlib| Creating data visualizations
Git and GitHub| Version control and project hosting

🧠 How the Project Works

The application follows these steps:

1. Data Collection: Loads a sample dataset containing student-related information.
2. Data Processing: Separates input features from the target score.
3. Data Splitting: Divides the dataset into training and testing sets.
4. Model Training: Trains a Random Forest Regression model using the training data.
5. Model Evaluation: Evaluates predictions using Mean Absolute Error and R².
6. User Input: Accepts student information through interactive sliders.
7. Score Prediction: Uses the trained model to estimate a possible final score.
8. Visualization: Displays the dataset and feature-importance chart.

📊 Input Features

The model uses the following input variables:

Feature| Description
Study Hours| Average number of hours spent studying per day
Attendance Percentage| Percentage of classes attended
Previous Score| Score obtained in a previous examination
Sleep Hours| Average number of hours slept per night
Assignments Completed| Number of assignments completed out of 10

Output: An estimated final examination score on a scale of 0 to 100.

📁 Project Structure

ai-student-performance-predictor/
│
├── app.py
│   └── Main Streamlit application and prediction logic
│
├── data/
│   └── student_performance.csv
│       └── Sample dataset used to train the model
│
├── requirements.txt
│   └── Required Python libraries
│
├── README.md
│   └── Project documentation
│
├── LICENSE
│   └── MIT License
│
└── .gitignore
    └── Files excluded from version control

⚙️ Installation and Setup

Follow these steps to run the project on your computer.

Prerequisites

Install the following:

- Python 3.10 or newer
- pip package installer
- A web browser

Step 1: Clone the Repository

Replace "YOUR-USERNAME" with your GitHub username.

git clone https://github.com/YOUR-USERNAME/ai-student-performance-predictor.git

Step 2: Open the Project Directory

cd ai-student-performance-predictor

Step 3: Create a Virtual Environment (Recommended)

Windows:

python -m venv .venv
.venv\Scripts\activate

Linux or macOS:

python3 -m venv .venv
source .venv/bin/activate

Step 4: Install Dependencies

pip install -r requirements.txt

Step 5: Run the Application

streamlit run app.py

The application should open in your default web browser.

If it does not open automatically, follow the local address displayed in your terminal.

📈 Model Evaluation

The project evaluates its model using two metrics.

1. Mean Absolute Error (MAE)

MAE measures the average absolute difference between the actual scores and the model's predicted scores. A lower value generally indicates smaller prediction errors.

2. R² Score

R² measures how well the model explains variation in the target values. Its interpretation depends on the dataset and evaluation setup; a higher value can indicate a better fit.

The application calculates both metrics using a held-out test dataset.

Important: These metrics reflect performance on the generated demonstration dataset. They do not establish real-world predictive accuracy.

📂 Dataset Information

The project includes a CSV dataset named "student_performance.csv".

- Contains 250 synthetic examples.
- Includes study habits and academic input features.
- Uses a generated final score as the prediction target.
- Is intended for educational and demonstration purposes.

The dataset does not contain actual student records.

⚠️ Limitations and Responsible Use

- The dataset is synthetic and does not represent real students.
- The model learns simplified patterns from generated data.
- Predictions may differ significantly from actual examination results.
- Factors such as teaching quality, health, motivation, and exam difficulty are not fully represented.
- Feature importance does not prove that a feature causes better academic performance.

This project is intended for educational purposes only. Its predictions should not be used to grade, rank, admit, or penalize students.

🚀 Future Improvements

Possible extensions include:

- Comparing Random Forest with Linear Regression and Decision Tree models.
- Adding cross-validation and more detailed model evaluation.
- Creating additional interactive charts.
- Using an appropriate, properly licensed, anonymized real-world dataset.
- Improving the application's interface and accessibility.
- Deploying the application online.
- Adding automated tests and a separate model-training script.

🎓 Learning Outcomes

Through this project, I aim to develop practical knowledge of:

- Python programming.
- Supervised Machine Learning.
- Regression algorithms.
- Dataset preparation and analysis.
- Model training and testing.
- Machine Learning evaluation metrics.
- Data visualization.
- Web application development.
- GitHub repository management.

👨‍💻 Author

Aayush Kumar

B.Tech — First Year

This project was developed as an introductory exploration of Artificial Intelligence, Machine Learning, and Python-based application development.

📜 License

This project is distributed under the MIT License. See the "LICENSE" file for details.

---

⭐ If you find this project useful for learning, consider giving the repository a star!

Built with Python and a passion for learning Artificial Intelligence.
