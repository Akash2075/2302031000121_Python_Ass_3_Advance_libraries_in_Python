import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
df = pd.read_csv('students.csv')

# Print the full DataFrame
print("Student Marks Data:\n", df)

# Calculate average marks for each student
df['Average'] = df[['Maths', 'Science', 'English']].mean(axis=1)
print("\nAverage Marks:\n", df[['Name', 'Average']])

# Find top scorer
topper = df[df['Average'] == df['Average'].max()]
print("\nTop Scorer:\n", topper[['Name', 'Average']])

# Visualize data
df.plot(x='Name', y=['Maths', 'Science', 'English'], kind='bar')
plt.title("Subject-wise Marks of Students")
plt.ylabel("Marks")
plt.grid(True)
plt.tight_layout()
plt.show()