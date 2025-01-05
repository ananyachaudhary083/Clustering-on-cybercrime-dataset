# Clustering Participants Profile to Tailor Cybercrime Awareness Programs

## Overview
This project uses **clustering techniques** to group participants based on their **demographic and behavioral data**. The goal is to design **customized awareness programs** for each cluster, enhancing the effectiveness of cybercrime awareness initiatives.

By understanding the unique needs of each group, we aim to create targeted interventions to improve cyber literacy and engagement.

---

## Features
- **Data Preprocessing**:
  - Handling missing values and encoding categorical data.
- **K-Means Clustering**:
  - Dividing participants into distinct clusters based on similarity.
- **Cluster Analysis**:
  - Visualizing and interpreting the clusters to derive actionable insights.
- **Customized Program Design**:
  - Suggestions for awareness programs tailored to each cluster's characteristics.

---

## Repository Structure
```plaintext
├── data/
│   ├── Cyber Sample Data Set with Summary 2022.xlsx  # Input dataset
│   └── Clustered_Participant_Profiles.xlsx           # Output with assigned clusters
├── notebooks/
│   ├── clustering_analysis.ipynb                    # Jupyter notebook for exploratory analysis
├── scripts/
│   ├── clustering_pipeline.py                       # Script for clustering workflow
├── README.md                                        # Project documentation
```

---

## Requirements
Install the required Python libraries using the following command:
```bash
pip install -r requirements.txt
```

**Key Libraries**:
- `pandas`: Data manipulation.
- `scikit-learn`: Clustering with K-Means.
- `matplotlib` & `seaborn`: Data visualization.

---

## How to Run the Project
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. **Prepare the Data**:
   - Place the input dataset (`Cyber Sample Data Set with Summary 2022.xlsx`) in the `data/` folder.

3. **Run the Clustering Pipeline**:
   Execute the script to preprocess data, perform clustering, and generate the output file:
   ```bash
   python scripts/clustering_pipeline.py
   ```

4. **Analyze the Results**:
   - Open `Clustered_Participant_Profiles.xlsx` to view the clusters.
   - Use the visualizations or statistics generated in the notebook/script to interpret clusters.

---

## Key Insights
- **Cluster 0**: Participants with low awareness; ideal for beginner-level programs.
- **Cluster 1**: Moderately aware participants; suited for intermediate-level training.
- **Cluster 2**: Highly aware participants; potential ambassadors for cyber awareness.

---

## Future Work
- Explore advanced clustering algorithms (e.g., DBSCAN, Hierarchical Clustering).
- Integrate additional features for more robust clustering.
- Automate the customization of awareness program content.

---

## Contributing
We welcome contributions to improve this project. To contribute:
1. Fork the repository.
2. Create a new branch for your feature.
3. Submit a pull request.

---

## License
This project is licensed under the [MIT License](LICENSE).
