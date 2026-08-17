# Level 1 - Task 2: Exploratory Data Analysis (EDA)

## Objective
Perform exploratory data analysis on a student academic performance dataset to identify patterns, trends, distributions, and relationships between numerical features.

## Dataset
- Number of rows: 275
- Number of columns: 16
- Dataset type: Student Academic Performance

## Tools Used
- Python
- Pandas
- Matplotlib
- Seaborn

## EDA Steps Performed

### 1. Data Loading
The dataset was loaded using Pandas `read_csv()`.

### 2. Dataset Inspection
- `df.head()` was used to view the first five rows.
- `df.shape` was used to check the number of rows and columns.
- `df.info()` was used to inspect data types and non-null values.

### 3. Summary Statistics
Mean, median, mode, and standard deviation were calculated for numerical columns.

### 4. Data Visualization
- Histogram of Overall Performance
- Boxplot of Overall Performance
- Scatter plot of Study Hours Per Day vs Overall Performance
- Correlation heatmap

### 5. Correlation Analysis
Important correlations with Overall Performance observed in the analysis:
- Final Exam Score: 0.81
- Midterm Score: 0.69
- Assignment Score: 0.61
- Lab Score: 0.57
- Study Hours Per Day: 0.53
- Attendance Percentage: 0.52

## Key Findings
1. Final Exam Score has the strongest positive correlation with Overall Performance among the listed features.
2. Midterm Score shows a fairly strong positive relationship with Overall Performance.
3. Assignment Score and Lab Score show moderate positive relationships with Overall Performance.
4. Study Hours Per Day and Attendance Percentage show moderate positive relationships with Overall Performance.
5. The correlation heatmap provides a visual overview of relationships among numerical variables.

## Conclusion
The exploratory data analysis helped identify important patterns and relationships in the student academic performance dataset. Overall Performance is most strongly associated with Final Exam Score among the observed relationships.

## Files
- `Student_EDA.csv` - Dataset
- `task2.py` - Python EDA code
- `README.md` - Project documentation
