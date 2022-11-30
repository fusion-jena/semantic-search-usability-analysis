#! python

"""
This scripts "flattens" the dataset as described in the readme and combines
all survey results into one big file. It then adds the tasks metadata.
"""

import os
import re
import numpy as np 
import pandas as pd

metadata_path = "data/raw_data/task_data.csv"
survey_results_path = "data/raw_data/survey_data"
output_path = "data/complete_dataset.csv"

n_users = 20
n_tasks = 8

full_data = pd.DataFrame()


if __name__ == '__main__':

    metadata = pd.read_csv(metadata_path, sep=",")
    metadata.drop("index", axis=1, inplace=True)

    for i in range(n_users):
        user_id = i+1
        print(f"Current User: {user_id}")
        
       
        user_data = metadata[metadata.user == user_id]
        user_result_path = os.path.join(
                survey_results_path, f"User{user_id}",f"results_user{user_id}.csv")
        try:
            user_survey = pd.read_csv(user_result_path, sep=",") 
            
            user_survey.fillna('null',inplace = True)
 
            #print(user_survey)
        except FileNotFoundError:
            print(
                    f"No survey results for user {user_id} found, checked path {user_result_path}...")
            continue

       
        
        # determine how many rows we have and select the row were most questions were answered
        #user_survey = user_survey.sort_values(
         #       "lastpage. Last page", ascending=False).head(1)
        pattern = "(feedbackB\d\[SQ0\d\d\])\.[A-Za-z0-9:,;\.\s]+ (\[.+.\])"
        feedback_cols = [c for c in user_survey if re.search(pattern,c)]
        user_system_feedback = user_survey[feedback_cols]
        
       
        
        #undergrad_cols = [c for c in user_survey.columns if re.search("(Undergraduate|Bachelor) student", c) ]
        #user_is_undergrad =  any(user_survey[undergrad_cols] != "No")
    
        # searchExperience[SQ001]. Please consider the entire search experience that you just had when you respond to the following questions [1. To what extent did you understand the nature of the searching task?]
        #pattern_exit_understandTask="searchExperience\[SQ00\d\]\. Please consider the entire search experience that you just had when you respond to the following questions \[1\. To what extent did you understand the nature of the searching task\?\]"
        #exit_understandTask="exit_understandTask"
        
        # searchExperience[SQ002]. Please consider the entire search experience that you just had when you respond to the following questions [2. To what extent did you find this task similar to other searching tasks that you typically perform?]
        #pattern_exit_similarToDailyWork="searchExperience\[SQ00\d\]\. Please consider the entire search experience that you just had when you respond to the following questions \[2\. To what extent did you find this task similar to other searching tasks that you typically perform\?\]"
        #exit_similarToDailyWork="exit_similarToDailyWork"
              
        # searchExperience[SQ003]. Please consider the entire search experience that you just had when you respond to the following questions [3. How different did you find the systems from one another?]
        pattern_exit_searchExperience="searchExperience\[SQ00\d\]\. Please consider the entire search experience that you just had when you respond to the following questions \[\d\. ([A-Za-z\s]+)\?\]"
        
        # easyToUse. Which of the two systems did you find easier to use?
        pattern_exit_easyToUse="(easyToUse)(\[SQ0\d\d\])?\. Which of the two systems did you find easier to use\?(\s\[BIODIV \d\])?"
        exit_easyToUse="exit_easyToUse"
        
        # easyToLearn. Which of the two systems did you find easier to learn to use?
        pattern_exit_easyToLearn="(easyToLearn)(\[SQ0\d\d\])?\. Which of the two systems did you find easier to learn to use\?(\s\[BIODIV \d\])?"
        exit_easyToLearn="exit_easyToLearn"

        # bestOverall. Which of the two systems did you like the best overall?/ bestOverall[SQ001]. Which of the two systems did you like the best overall? [BIODIV 1]
        pattern_exit_bestOverall="bestOverall(\[SQ0\d\d\])?\. Which of the two systems did you like the best overall\?(\s\[BIODIV \d\])?"
        exit_bestOverall="bestOverall"
        
        # like. What did you like about each of the systems?
        #pattern_exit_like="like\. What did you like about each of the systems\?"
        
        # dislike. What did you dislike about each of the systems?
        pattern_exit_like_dislike="(like|dislike)\. What did you (like|dislike) about each of the systems\?"
               
        ### statistics #####
        # education[SQ001]. Please provide your educational background? [((Undergraduate|Bachelor|Master) student)|Post-Doc|Professor|Researcher|Data Curator]
        pattern_student_cols = "education\[SQ0\d\d\]\. Please provide your educational background\? \[((Undergraduate|Bachelor|Master|PhD) student)|Post-Doc|Professor|Researcher|Data Curator\]"
        
        #research background
        pattern_research_background = "researchBackground\[SQ0\d\d\]\. What is your main research background\? \[(Botany|Zoology|Ecology|Biodiversity|Geography)\]"
        
        #searchUsage. How often do you need to search for datasets?
        pattern_searchUsage = "searchUsage\. How often do you need to search for datasets\?"
        # researchBackground[SQ001]. What is your main research background? [Botany|Zoology|Ecology|Biodiversity|Geography]
        # fieldOfResearch. Please provide your field(s) of research:
        


        #exit_cols_understandTask = [c for c in user_survey.columns if re.search(pattern_exit_understandTask, c) ]
        #exit_cols_similarToDailyWork = [c for c in user_survey.columns if re.search(pattern_exit_similarToDailyWork, c) ]
        exit_cols_searchExperience = [c for c in user_survey.columns if re.search(pattern_exit_searchExperience, c) ]
        exit_cols_easyToLearn = [c for c in user_survey.columns if re.search(pattern_exit_easyToLearn, c) ]
        exit_cols_easyToUse = [c for c in user_survey.columns if re.search(pattern_exit_easyToUse, c) ]
        exit_cols_bestOverall = [c for c in user_survey.columns if re.search(pattern_exit_bestOverall, c) ]
        exit_cols_like_dislike = [c for c in user_survey.columns if re.search(pattern_exit_like_dislike, c) ]
        
        student_cols = [c for c in user_survey.columns if re.search(pattern_student_cols, c) ]
        research_background_cols = [c for c in user_survey.columns if re.search(pattern_research_background, c) ]
        searchUsage_cols = [c for c in user_survey.columns if re.search(pattern_searchUsage, c) ]
        
        #user_is_student =  any(user_survey[student_cols] == "Yes")
        
        #exit_cols = exit_cols_understandTask + exit_cols_similarToDailyWork+ exit_cols_easyToLearn+ exit_cols_easyToUse+exit_cols_bestOverall
        exit_cols = exit_cols_searchExperience+ exit_cols_easyToLearn+ exit_cols_easyToUse+exit_cols_bestOverall+exit_cols_like_dislike+student_cols+research_background_cols+searchUsage_cols
        exit_stats = user_survey[exit_cols]
               
        exit_stats[exit_easyToLearn] = exit_stats[exit_cols_easyToLearn].sum(1)
        exit_stats = exit_stats.drop(exit_cols_easyToLearn, 1)
               
        exit_stats[exit_easyToUse] = exit_stats[exit_cols_easyToUse].sum(1)
        exit_stats = exit_stats.drop(exit_cols_easyToUse, 1)
        
        exit_stats[exit_bestOverall] = exit_stats[exit_cols_bestOverall].sum(1)
        exit_stats = exit_stats.drop(exit_cols_bestOverall, 1)
        
        exit_stats.replace('NoNoYes', 'no difference', regex=True, inplace=True)
        exit_stats.replace('YesNoNo', 'Biodiv 1', regex=True, inplace=True)
        exit_stats.replace('NoYesNo', 'Biodiv 2', regex=True, inplace=True)
        
        #exit_stats.info()
        #print('easyToLearn'+str(exit_cols_easyToLearn))
        
        #exit_stats["student"] = user_is_student
        
        for j in range(n_tasks):
            task_id = j+1
            
            task_system = int(
                    user_data.loc[user_data.task == task_id, "system"])
            task_row = user_data.loc[user_data.task == task_id]
            print('UserID: '+str(user_id)+', taskID: '+str(task_id))
            #print(
                 #   f"User {user_id} Task {task_id} was done in System {task_system}")

            task_metadata = metadata[(metadata.user == user_id) & (
                metadata.task == task_id)]
         
            
            # pattern to search for questions answered after each search task
            #Are you familiar with this topic?
            afterSearchTask_familiarWithTopic = "topicB\dT\d\[SQ00\d\]\. Biodiv\d - (Task"+str(task_id)+") - .+(Are you familiar with this topic\?)\]"
            familiarWithTopic = "familiarWithTopic"
            
            afterSearchTask_easyToGetStarted = "topicB\dT\d\[SQ00\d\]\. Biodiv\d - (Task"+str(task_id)+") - .+(Was it easy to get started on this search\?)\]"
            easyToGetStarted = "easyToGetStarted"

            afterSearchTask_easyToDoTheTask = "topicB\dT\d\[SQ00\d\]\. Biodiv\d - (Task"+str(task_id)+") - .+(Was it easy to do the search on this topic?\?)\]"
            easyToDoTheTask = "easyToDoTheTask"

            afterSearchTask_satisfaction = "topicB\dT\d\[SQ00\d\]\. Biodiv\d - (Task"+str(task_id)+") - .+(Are you satisfied with your search results\?)\]"
            satisfaction = "satisfactionPerTask"

            afterSearchTask_enoughTime = "topicB\dT\d\[SQ00\d\]\. Biodiv\d - (Task"+str(task_id)+") - .+(Did you have enough time to do an effective search\?)"
            enoughTime = "timePerTask"
            
            afterSearchTask_whyRelevant = "relevancyResultsB\dT\d\. Biodiv\d - (Task"+str(task_id)+") - .+(Why are these datasets relevant\? \/ Why are no datasets relevant\?)"
            whyRelevant = "whyRelevant"
           
            afterSearchTask_issues = "issuesB\d(T"+str(task_id)+")\. Please use the space below if you encounter any issues in this search task \(What is confusing or surprising\? What is positive or negativ\? Why\?\)"
            issues = "issues"
            
            #full_data[user_data.task == task_id, "test"] = user_survey[column]
            task_columns = [c for c in user_survey.columns if  re.search(afterSearchTask_easyToGetStarted, c)]
            c_todo = [c for c in user_survey.columns if  re.search(afterSearchTask_easyToDoTheTask, c)]
            c_satisfaction = [c for c in user_survey.columns if  re.search(afterSearchTask_satisfaction, c)]
            c_enoughTime = [c for c in user_survey.columns if  re.search(afterSearchTask_enoughTime, c)]
            c_familiarWithTopic = [c for c in user_survey.columns if  re.search(afterSearchTask_familiarWithTopic, c)]
            c_whyRelevant = [c for c in user_survey.columns if  re.search(afterSearchTask_whyRelevant, c)]
            c_issues = [c for c in user_survey.columns if  re.search(afterSearchTask_issues, c)]
            #print (c_issues)
            task_columns = task_columns + c_todo + c_satisfaction + c_enoughTime + c_familiarWithTopic + c_whyRelevant + c_issues
            # filter out fillers
            #task_columns = [c for c in task_columns if "placeholder" not in c and "task" not in c]

          
            #print(user_survey[task_columns])
            # select columns that are about given task
            task_data = user_survey[task_columns]
            
            
            # remove full questions (usually after >>.<<) 
            #task_columns_clean = [re.sub(varname_shorthand, "", col).split(".")[0] for col in task_columns]
            #task_columns_clean = [re.sub(afterSearchTask_easyToGetStarted, easyToGetStarted_easyName,col) for col in task_columns]


            #task_data.columns = ['Task{task_id} - Was it easy to get started on this search?']
            #task_data = task_data[task_columns_clean]

            #task_data.reset_index(drop=True, inplace=True)
            task_data.reset_index(drop=True, inplace=True)
            task_metadata.reset_index(drop=True, inplace=True)
            user_system_feedback.reset_index(drop=True, inplace=True)
            exit_stats.reset_index(drop=True, inplace=True)
         
            
            cols = task_metadata.columns.tolist()+[easyToGetStarted,easyToDoTheTask,satisfaction,enoughTime,familiarWithTopic,whyRelevant,issues] + user_system_feedback.columns.tolist()+exit_stats.columns.tolist()      
            #cols = task_metadata.columns.tolist()+[easyToGetStarted,easyToDoTheTask,satisfaction,enoughTime,familiarWithTopic] + user_system_feedback.columns.tolist()+[exit_understandTask,exit_similarToDailyWork,exit_easyToLearn,exit_easyToUse]
#            + user_system_feedback.columns.tolist() + exit_stats.columns.tolist()
            
            #cols = task_metadata.columns.tolist()
            #task_data = pd.concat(
            #        [task_metadata,task_data,user_system_feedback,exit_stats], axis=1, ignore_index=True)
            
            task_data = pd.concat([task_metadata,task_data,user_system_feedback,exit_stats], axis=1, ignore_index=True)
            task_data.columns = cols
           
            
            # remove characters from scale variables (e.g. "5 - strongly agree" to 5)´
            stronglyDisagree = r"1 - strongly<br\s?\/>\s?disagree"
            notAtAll = r"0 - not at all"
            notAtAll1 = r"1 - not at all"
            somewhat = r"2 - somewhat"
            somewhat3 = r"3 - somewhat"
            neutral = r"3 - neutral"
            extremely = r"4 - extremely"
            extremely5 = r"5 - extremely"
            completely = r"5 - completely"
            stronglyAgree = r"5 - strongly<br\s?\/>\s?agree"
            task_data.replace([notAtAll,notAtAll1,stronglyDisagree,somewhat,somewhat3,neutral,extremely,extremely5, completely,stronglyAgree], [0,1,1,2,3,3,4,5,5,5],regex=True,inplace=True)
         
            # rating scale for user 14 and 15 were set to 0 - 4 instead of 1 - 5 --> correction needed
            if user_id == 14 or user_id == 15 or user_id == 20:
               #print ("user_id 14,15, or 20")
               task_data[easyToGetStarted] = int(task_data[easyToGetStarted]) + 1
               task_data[easyToDoTheTask] = int(task_data[easyToDoTheTask]) +1
               task_data[satisfaction] = int(task_data[satisfaction]) +1
               task_data[enoughTime] = int(task_data[enoughTime]) +1
               task_data[familiarWithTopic] = int(task_data[familiarWithTopic]) +1

            # add user stats
            #task_data["student"] = user_is_student
            #task_data["undergrad"] = user_is_undergrad
            
            full_data = pd.concat([full_data, task_data],
                    axis=0, )
            full_data.reset_index(inplace=True, drop=True)        
            #full_data['test']=user_survey[column]
            

     # entries consisting only of whitespace will be converted to empty entries
    full_data.replace("^\s+$","", regex=True, inplace=True)
    
    # create index task_satisfaction
    #index_vars = ["topic[SQ002]", "topic[SQ003]", "topic[SQ004]", "topic[SQ005]"]
    #index_data = full_data[index_vars].apply(pd.to_numeric).sum(axis=1) * 1/4
    #full_data["task_satisfaction"] = index_data

    # create index total_issues
    index_vars = ["issues_functional", "issues_content", "issues_comprehensibity", "issues_presentation"]
    index_data = full_data[index_vars].apply(pd.to_numeric).sum(axis=1)
    full_data["total_issues"] = index_data

    # remove questions text in varnames (they are separated from varname by a full stop)
    full_data.columns = [ re.sub("\..+$", "", c) for c in full_data.columns ]
  
    full_data.searchUsage.replace(['Never','1 - 2 times a year', '1 - 2 times in a month','1 - 2 times in week','Daily'], [1, 2,3,4,5], inplace=True)
 
    
    positive_vars = [1,3,6,8,9]
    #create sus score
    #even vars are negative, odd positive
    for system in (1,2):
       sus_varname = f"SUS_Biodiv{system}"
       full_data[sus_varname] = 0.0
       for item in range(1,11):
           varname = f"feedbackB{system}[SQ0{item:02d}]"
           x = full_data[varname]
           
           var = pd.to_numeric(full_data[varname]).fillna(0)
           s = var - 1 if item in positive_vars else 5 - var
           full_data[sus_varname] += s
       full_data[sus_varname] *= 2.5

    # calucate how many seconds were spent working on this task
    full_data["task_full_time"] = full_data.task_minutes * 60 + full_data.task_seconds
    
    #data correction for user 14 and 15 (rating scale 0 - 4 instead of 1 - 5)
    

    full_data.to_csv(output_path, sep=";")
