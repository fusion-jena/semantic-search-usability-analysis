# Data preprocessing

For easier analysis we have to merge the survey-results of all participants.
However, variable naming across all surveys is not uniform (if task 5 was 
completed in system 1, the resulting variable name is something like B1T5). 
We should transform the dataset, so that all variables concerning a certain
task are named the same. For this to work we need additional variables storing
information on what task was solved using what system for a particular user.

After that we should change the dataset structure from a user-based scheme (as in:
every row represents one user) two a task-based scheme (so that every row contains
data on one task). This is because most of the quantitative analysis we do is done
on a per-task-base.

# Enrichment of data

The final dataset does not consist of only the survey results. We also have to
add the following variables:

- Task success:

  *for each user and task there is an additional variable that stores if the use
  had success working on that task. `0` signifies no success, `1` partial success 
  and `2` full success. This variable can be generated programatically by
  counting the files in the given taskresult.*
- Issues raised:
  
  *For each user session the is a .doc-File that describes what issues were 
  raised during the given task. For each user / task we should have a variable
  that counts how many issues of a certain category where encountered.*

# Used scripts

The scrupt `get_task_success.py` automatically looks up how many files are in 
the .zip-archive for each user/task and adds this information to `data/raw_data/task_data.csv`.
