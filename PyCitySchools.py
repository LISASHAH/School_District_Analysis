# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Add the Pandas dependency.
import pandas as pd
#import formula as df

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

#%%
# Calculate the total budget.
total_budget = school_data_df["budget"].sum()
total_budget
#%%
# Calculate the average reading score.
average_reading_score = school_data_complete_df["reading_score"].mean()
average_reading_score
#%%
# Calculate the average math score.
average_math_score = school_data_complete_df["math_score"].mean()
average_math_score
#%%
passing_math = school_data_complete_df["math_score"] >= 70
passing_reading = school_data_complete_df["reading_score"] >= 70
#%%
# Get all the students who are passing math in a new DataFrame.
passing_math = school_data_complete_df[school_data_complete_df["math_score"] >= 70]
passing_math.head()
#%%
# Get all the students who are passing english in a new DataFrame.
passing_reading = school_data_complete_df[school_data_complete_df["reading_score"] >= 70]
passing_reading.head()
#%%
# Calculate the number of students passing math.
passing_math_count = passing_math["student_name"].count()
passing_math_count
# Calculate the percent that passed math.
passing_math_percentage = passing_math_count / float(student_count["student_name"]) * 100
passing_math_percentage
#%%
# Calculate the number of students passing reading.
passing_reading_count = passing_reading["student_name"].count()
# Calculate the percent that passed reading.
passing_reading_percentage = passing_reading_count / float(student_count["student_name"]) * 100
#%%
# Calculate the overall passing percentage.
overall_passing_percentage = (passing_math_percentage + passing_reading_percentage ) / 2

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


#%%
# Format the columns.
district_summary_df["Average Math Score"] = district_summary_df["Average Math Score"].map("{:.1f}".format)

district_summary_df["Average Reading Score"] = district_summary_df["Average Reading Score"].map("{:.1f}".format)

district_summary_df["% Passing Math"] = district_summary_df["% Passing Math"].map("{:.0f}".format)

district_summary_df["% Passing Reading"] = district_summary_df["% Passing Reading"].map("{:.0f}".format)

district_summary_df["% Overall Passing"] = district_summary_df["% Overall Passing"].map("{:.0f}".format)

district_summary_df

# Reorder the columns in the order you want them to appear.
new_column_order = ["Total Students","Total Schools", "Total Budget","Average Math Score", "Average Reading Score", "% Passing Math", "% Passing Reading", "% Overall Passing"]
# Assign district summary df the new column order.
district_summary_df = district_summary_df[new_column_order]
district_summary_df


# %%
# Define a function that calculates the percentage of students that passed both # math and reading and prints the passing percentage to the output when the
# function is called.
def passing_math_percent1(pass_math_count, student_count):
    return pass_math_count / float(student_count) * 100
#%%
# Call the function.
#passing_math_percent = passing_math_percent1(passing_math_count, total_student_count)

# %%
district_summary_df