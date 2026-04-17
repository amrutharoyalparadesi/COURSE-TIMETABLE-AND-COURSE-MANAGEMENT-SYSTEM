import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def faculty_workload(faculty_list):
    workloads = [len(f.assigned_courses) for f in faculty_list]
    names = [f.name for f in faculty_list]

    avg = np.mean(workloads)
    print("Average workload:", avg)

    df = pd.DataFrame({
        'Faculty': names,
        'Workload': workloads
    })

    print(df)

    plt.bar(names, workloads)
    plt.title("Faculty Workload Distribution")
    plt.xlabel("Faculty")
    plt.ylabel("Courses Assigned")
    plt.show()
