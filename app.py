import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score

st.set_page_config(page_title="AI Student Performance Predictor", page_icon="🎓", layout="wide")

DATA_PATH = Path(__file__).parent / "data" / "student_performance.csv"
FEATURES = ["study_hours", "attendance_percent", "previous_score", "sleep_hours", "assignments_completed"]
TARGET = "final_score"

@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

@st.cache_resource
def train_model():
    data = load_data()
    X = data[FEATURES]
    y = data[TARGET]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    model = RandomForestRegressor(n_estimators=150, random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    return model, mean_absolute_error(y_test, predictions), r2_score(y_test, predictions), data

st.title("🎓 AI Student Performance Predictor")
st.write(
    "A beginner-friendly machine-learning project that estimates a student's "
    "possible final score from study habits and academic indicators."
)
st.info(
    "Learning demo: the included dataset is synthetic (computer-generated), not real student records. "
    "Predictions are illustrative and must not be used for high-stakes academic decisions."
)

model, mae, r2, data = train_model()

with st.sidebar:
    st.header("Enter student details")
    study_hours = st.slider("Study hours per day", 0.0, 12.0, 3.0, 0.5)
    attendance = st.slider("Attendance (%)", 0, 100, 80)
    previous_score = st.slider("Previous exam score", 0, 100, 65)
    sleep_hours = st.slider("Sleep hours per night", 0.0, 12.0, 7.0, 0.5)
    assignments = st.slider("Assignments completed (out of 10)", 0, 10, 7)
    predict = st.button("Predict score", type="primary", use_container_width=True)

left, right = st.columns([1, 1])
with left:
    st.subheader("Predicted result")
    if predict:
        input_data = pd.DataFrame([{
            "study_hours": study_hours,
            "attendance_percent": attendance,
            "previous_score": previous_score,
            "sleep_hours": sleep_hours,
            "assignments_completed": assignments
        }])
        prediction = float(model.predict(input_data)[0])
        prediction = max(0, min(100, prediction))
        st.metric("Estimated final score", f"{prediction:.1f} / 100")
        if prediction >= 75:
            st.success("The model estimates a strong result. Keep up the consistent habits!")
        elif prediction >= 50:
            st.warning("The model estimates a moderate result. Regular revision may help.")
        else:
            st.error("The model estimates a lower result. Consider a study plan and ask an instructor for support.")
    else:
        st.write("Adjust the values in the sidebar and click **Predict score**.")

with right:
    st.subheader("Model evaluation")
    c1, c2 = st.columns(2)
    c1.metric("Mean absolute error", f"{mae:.2f} points")
    c2.metric("R² score", f"{r2:.2f}")
    st.caption("Metrics are calculated on a held-out test split of the synthetic dataset.")

st.divider()
st.subheader("Explore the demo dataset")
st.dataframe(data.head(10), use_container_width=True)
st.caption(f"Dataset size: {len(data)} generated examples.")

st.subheader("Which inputs matter most to this model?")
importance = pd.Series(model.feature_importances_, index=FEATURES).sort_values()
fig, ax = plt.subplots(figsize=(8, 4))
importance.plot(kind="barh", ax=ax)
ax.set_xlabel("Relative feature importance")
ax.set_ylabel("")
ax.set_title("Random Forest feature importance")
st.pyplot(fig)
plt.close(fig)

st.markdown("---")
st.markdown("Built as an introductory B.Tech AI/ML project using Python, pandas, scikit-learn, and Streamlit.")
