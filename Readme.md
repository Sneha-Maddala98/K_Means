# K-Means Clustering Algorithm

This Python script implements the K-Means clustering algorithm for data clustering. K-Means is an unsupervised machine learning technique used to partition a dataset into groups or clusters based on the similarity of data points. This script provides a basic implementation of K-Means and allows you to perform clustering on a given dataset.

## Prerequisites

Before running the script, make sure you have the following libraries installed:

- [NumPy] For numerical operations.
- [Pandas]: For data manipulation.
- [argparse] For command-line arguments.

## Usage

- `data_file.csv`: The path to the CSV file containing your dataset. The CSV file should have columns for data points, and each point should have an 'x' and 'y' value. The 'label' column is used to represent the cluster label.

## Algorithm

The script implements the K-Means algorithm with the following steps:

1. Read the dataset from the specified CSV file.
2. Initialize the centroids for each cluster ('A', 'B', 'C').
3. Perform the K-Means clustering algorithm to assign each data point to the nearest centroid.
4. Update the centroids based on the mean of data points assigned to each cluster.
5. Repeat the process until there is no change in cluster assignments.
6. Print the centroids for each cluster.


This will load the dataset from `Example.csv` and perform K-Means clustering to partition the data into clusters.

The script will print the centroids of clusters 'A', 'B', and 'C' for each iteration and stop when there is no further change in cluster assignments.

You can customize the 'k' value (number of clusters) and modify the script to suit your specific clustering needs.
