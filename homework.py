import pandas as pd
import numpy as np

num_students = 10

data = {
    'Student': [f'Student_{i+1}' for i in range(num_students)],
    'Math': np.random.randint(1, 6, size=num_students),
    'Science': np.random.randint(1, 6, size=num_students),
    'English': np.random.randint(1, 6, size=num_students),
    'History': np.random.randint(1, 6, size=num_students),
    'Art': np.random.randint(1, 6, size=num_students)
}

df = pd.DataFrame(data)
print(df.head())

average_grades = df.mean(numeric_only=True)
median_grades = df.median(numeric_only=True)

print("Средние и медианные оценки по каждому предмету:")

for subject in average_grades.index:
    print(f"{subject}:")
    print(f"  Средняя: {average_grades[subject]:.1f}")
    print(f"  Медианная: {median_grades[subject]:.1f}")

Q1_math = df['Math'].quantile(0.25)
Q3_math = df['Math'].quantile(0.75)
IQR_math = Q3_math - Q1_math

print(f"Q1 (25-й перцентиль) для оценок по математике: {Q1_math:.1f}")
print(f"Q3 (75-й перцентиль) для оценок по математике: {Q3_math:.1f}")
print(f"IQR (межквартильный размах) для оценок по математике: {IQR_math:.1f}")

std_deviation = df.std(numeric_only=True)
print("Стандартное отклонение по каждому предмету:")
for subject, std in std_deviation.items():
    print(f"{subject}: {std:.2f}")





