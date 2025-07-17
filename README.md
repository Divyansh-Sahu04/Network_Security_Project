### Network Security Project for Phishing Data

* Processed a large dataset of over 11,000 records and more than 30 features capturing URL and website characteristics, where the model outputs -1 for malicious websites and 1 for safe ones.
* Extracted and cleaned a Kaggle dataset, transformed it from CSV to JSON format, and loaded it into MongoDB Atlas using an ETL pipeline.
* Built an end-to-end machine learning training pipeline including modules for data ingestion, validation, transformation, and model training, ensuring scalable and efficient model development.
* Exported raw data as a DataFrame during the data ingestion phase, stored it in a feature store, and performed a train-test split to generate train.csv and test.csv for model training.
* Initiated the data validation process by reading the dataset, verifying the number of columns, ensuring the presence of numerical features, detecting data drift, and generating a comprehensive data drift report.
* Initiated the data transformation process by splitting the dataset into input and output features, and implemented the KNN Imputer technique to handle missing values effectively.
* Initiated the model training process using classification algorithms such as Random Forest, Decision Tree, Gradient Boosting, Logistic Regression, and AdaBoost.
* Performed hyperparameter tuning for each model and tracked performance metrics (F1 score, precision, recall) using MLflow for efficient model comparison and evaluation.
* Deployed the solution as a FastAPI application with a custom HTML interface, integrated logging for traceability, and containerized the project using Docker, publishing the image to Docker Hub for seamless cross-platform execution.
* Achieved an F1-score of 0.979, precision of 0.977, and recall of 0.980 using the Gradient Boosting algorithm for phishing website classification.



