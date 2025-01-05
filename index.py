import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Excel file
file_path = "Cyber Sample Data Set with Summary 2022.xlsx"  # Update with your file path
data = pd.ExcelFile(file_path)

# Load the "Sample Data" sheet
sample_data = data.parse("Sample Data")

# Selecting relevant columns for clustering
relevant_columns = [
    "Age Group",
    "Gender",
    "Studying or Working",
    "Have you attended any webinar on Cyber Crime Awareness?",
    "Are you aware about Cyber Crime and Safety Precautions tips?",
    "Does this small training programme help you to enhance your knowledge on Cyber Crime Awareness and Safety Precautions?",
    "Would you like to participate in the Webinar on Cyber Crime Awareness?",
    "Would you like to participate in the Cyber Champion Ambassador Programme of College/City/State/National Level to create awareness on Cyber Crime and Safety Precautions?"
]

clustering_data = sample_data[relevant_columns]

# Preprocessing: Handle missing values
imputer = SimpleImputer(strategy='most_frequent')
clustering_data = pd.DataFrame(imputer.fit_transform(clustering_data), columns=relevant_columns)

# Encoding categorical variables
label_encoders = {}
for column in clustering_data.columns:
    le = LabelEncoder()
    clustering_data[column] = le.fit_transform(clustering_data[column])
    label_encoders[column] = le

# Determine the optimal number of clusters using the Elbow Method
inertia = []
k_range = range(1, 11)

for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init='auto')
    kmeans.fit(clustering_data)
    inertia.append(kmeans.inertia_)

# Plot the Elbow Curve
plt.figure(figsize=(8, 5))
plt.plot(k_range, inertia, marker='o')
plt.title("Elbow Method to Determine Optimal Number of Clusters")
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Inertia")
plt.xticks(k_range)
plt.grid()
plt.show()

# Perform clustering with the chosen number of clusters (e.g., 3)
optimal_clusters = 3  # Update this based on the Elbow Curve
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42, n_init='auto')
clustering_data['Cluster'] = kmeans.fit_predict(clustering_data)

# Visualize each feature against the cluster labels
for feature in relevant_columns:
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=clustering_data, x="Cluster", y=feature, palette="Set2")
    plt.title(f"Distribution of {feature} Across Clusters")
    plt.xlabel("Cluster")
    plt.ylabel(feature)
    plt.grid(axis="y")
    plt.show()

# Save clustered data to a new Excel file
output_file = "Clustered_Participant_Profiles.xlsx"
clustering_data.to_excel(output_file, index=False)
print(f"Clustered data saved to {output_file}")
