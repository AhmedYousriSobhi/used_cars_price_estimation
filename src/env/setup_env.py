"""
    Author: Ahmed Sobhi.
    Department: Data Science.
    Created_at: 2023-06-14
    Objective: Create workspace directories for project.
"""
# Importing Required Libararies
import os

# Code flow
if __name__=='__main__':
    
    # Create required directories for data
    if not os.path.exists('data/'):
        os.makedirs('data/raw')
        os.makedirs('data/intermid')
        os.makedirs('data/output')

    # Create required directories for nb_workspace
    if not os.path.exists('nb_workspace'):
        os.makedirs('nb_workspace')
    
    # Create required directories for report
    if not os.path.exists('report/'):
        os.makedirs('report/plots')
        os.makedirs('report/reports')

    # Create required directories for Documentation
    if not os.path.exists('docs/'):
        os.makedirs('docs/')