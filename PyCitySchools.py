# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Add the Pandas dependency.
import pandas as pd


# %%
# Files to load
school_data_to_load = "Resources/schools_complete.csv"
student_data_to_load = "Resources/students_complete.csv"


# %%
# Read the school data file and store it in a Pandas DataFrame.
school_data_df = pd.read_csv(school_data_to_load)
# Read the student data file and store it in a Pandas DataFrame.
student_data_df = pd.read_csv(student_data_to_load)


# %%
student_data_df.count()
school_data_df.isnull().sum()


# %%
# Add each prefix and suffix to remove to a list.
prefixes_suffixes = ["Dr. ", "Mr. ","Ms. ", "Mrs. ", "Miss ", " MD", " DDS", " DVM", " PhD"]
# Put the cleaned students' names in another list.
student_names = student_data_df["student_name"].tolist()


# %%
# Iterate through the words in the "prefixes_suffixes" list and replace them with an empty space, "".
for word in prefixes_suffixes:
    student_data_df["student_name"] = student_data_df["student_name"].str.replace(word,"")


# %%
# Combine the data into a single dataset.
school_data_complete_df = pd.merge(student_data_df, school_data_df, on=["school_name", "school_name"])
school_data_complete_df.head()


# %%
# Get the total number of students.
student_count = school_data_complete_df.count()
student_count


# %%
school_data_complete_df["Student ID"].count()


# %%
school_count = school_data_df["school_name"].count()
school_count


# %%
school_count2 =len(school_data_complete_df["school_name"].unique())
school_count2


# %%
school_budget = 0
school_budget = school_data_df["budget"].sum()
school_budget


# %%
average_reading_score = school_data_complete_df["reading_score"].mean()
average_reading_score


# %%
average_math_score = school_data_complete_df["math_score"].mean()
average_math_score


# %%
passing_math = school_data_complete_df["math_score"] >= 70
#passing_reading = school_data_complete_df["reading_score"] >= 70
passing_math.head()


# %%
# Adding a list of values with keys to create a new DataFrame.
district_summary_df = pd.DataFrame(
          [{"Total Schools": school_count,
          "Total Students": student_count,
          "Total Budget": total_budget,
          "Average Math Score": average_math_score,
          "Average Reading Score": average_reading_score,
          "% Passing Math": passing_math_percentage,
         "% Passing Reading": passing_reading_percentage,
        "% Overall Passing": overall_passing_percentage}])
district_summary_df



