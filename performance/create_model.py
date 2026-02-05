import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib

# Create a realistic model where previous scores are the main predictor
# with study habits providing incremental improvements or declines
np.random.seed(42)
n_samples = 2000

# Generate synthetic data
data = {
    'hours_studied': np.random.randint(1, 10, n_samples),
    'previous_scores': np.random.randint(40, 100, n_samples),
    'extracurricular': np.random.randint(0, 2, n_samples),
    'sleep_hours': np.random.randint(4, 10, n_samples),
    'sample_papers': np.random.randint(0, 10, n_samples),
}

# Create performance index where previous scores are the baseline
# and current habits provide +/- adjustments
performance_index = []

for i in range(n_samples):
    base_score = data['previous_scores'][i]
    
    # Calculate improvement/decline based on current habits
    # Good habits can improve by up to +10 points
    # Poor habits can decline by up to -10 points
    
    # Study hours contribution (-5 to +5)
    study_effect = (data['hours_studied'][i] - 5) * 0.8
    
    # Sleep contribution (-3 to +3)
    optimal_sleep = 7
    sleep_effect = -abs(data['sleep_hours'][i] - optimal_sleep) * 0.5
    
    # Sample papers contribution (0 to +4)
    papers_effect = data['sample_papers'][i] * 0.4
    
    # Extracurricular contribution (0 to +2)
    extra_effect = data['extracurricular'][i] * 2
    
    # Total adjustment
    adjustment = study_effect + sleep_effect + papers_effect + extra_effect
    
    # Add some randomness
    noise = np.random.normal(0, 2)
    
    # Calculate final score
    final_score = base_score + adjustment + noise
    
    # Clip to 0-100 range
    final_score = np.clip(final_score, 0, 100)
    
    performance_index.append(final_score)

df = pd.DataFrame(data)
df['performance_index'] = performance_index

# Train the model
X = df[['hours_studied', 'previous_scores', 'extracurricular', 'sleep_hours', 'sample_papers']]
y = df['performance_index']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42, max_depth=15)
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'model.pkl')
print("Model created and saved as model.pkl")
print(f"Model score: {model.score(X_test, y_test):.4f}")

# Test predictions with realistic scenarios
test_cases = [
    ([8, 96, 0, 6, 5], "High achiever maintaining good habits"),
    ([8, 85, 1, 7, 5], "Good student with balanced routine"),
    ([5, 70, 0, 6, 3], "Average student"),
    ([2, 50, 0, 4, 1], "Struggling student"),
    ([10, 90, 1, 7, 8], "Excellent student working hard"),
    ([3, 95, 0, 5, 2], "High achiever slacking off"),
]

print("\nTest predictions:")
for case, description in test_cases:
    pred = model.predict([case])[0]
    print(f"{description}")
    print(f"  Input: study={case[0]}h, prev={case[1]}, extra={case[2]}, sleep={case[3]}h, papers={case[4]}")
    print(f"  Prediction: {pred:.2f} (change: {pred - case[1]:+.2f})")
    print()