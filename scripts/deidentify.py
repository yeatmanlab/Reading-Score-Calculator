import pandas as pd
import numpy as np
import os
import glob

# set home directory so can be used on all OS
home = os.path.expanduser('~')

# find the most recent data file exported from the screening database and set it as the file
file = max(glob.iglob(home+'/Downloads/RDRPScreeningDatabas-TransferData_DATA_*.csv'), key=os.path.getctime)

# load data using the record_id as the index
scr = pd.read_csv(file, index_col='record_id', dtype=object)

# insert the redcap_event_name and set the value to subject_intake_arm_1 for easy import
scr['redcap_event_name'] = 'subject_intake_arm_1'

# set the sid from the subject_id
scr['sid']=scr.subject_id

# remove spaces from sid
scr['sid']=scr['sid'].str.replace(" ", "")

#for sub in scr.index:
#    scr.loc[scr.index==[sub],'sid']==str(scr.sid[sub]).replace(" ", "")

# create dummy email address for repository for ID
scr['sid_email']=scr.sid+'@red.cap'

# create new DataFrame for registry by selecting necessary values
reg = pd.DataFrame(scr, columns=['child' , 'adult' ,
'teen' , 'who_complete' , 'xx' , 'are_you' , 'are_you_cap' , 'do_you' ,
'do_you_cap' , 'have_you' , 'have_you_cap' , 'i_cap' ,
'i_have' , 'i_have_cap' , 'my_data' , 'their' , 'their_cap' , 'v_s' ,
'were_you' , 'were_you_cap' , 'you' , 'you_all_cap' , 'you_cap' ,
'you_and_your_child' , 'you_and_your_child_cap' , 'you_and_your' ,
'you_and_your_cap' , 'you_are' , 'you_are_cap' , 'you_have' ,
'you_have_cap' , 'you_or_your' , 'you_or_your_cap' , 'your' ,
'your_cap' , 'scr_waiver_initials' , 'pronouns_complete', 'first_name' ,
'last_name', 'dob' , 'scr_date' , 'age' , 'age_months' , 'gender' , 'teen_email'
, 'teen_phone' , 'parent_first_name' , 'parent_last_name' , 'email' ,
'phone' , 'city' , 'state' , 'zip' , 'parent2' , 'parent2_first_name'
, 'parent2_last_name' , 'parent2_email' , 'parent2_phone' , 'parent3'
, 'parent3_first_name' , 'parent3_last_name' , 'parent3_email' ,
'parent3_phone' , 'screening_complete' , 'scr_verified' , 'consent_staff',
'verify_scr_complete' , 'cg_adult_or_child' , 'cg_adult_name' , 'cg_child_name' ,
'cg_recording' , 'cg_recording_video', 'cg_adult_sig' ,
'cg_adult_date' , 'cg_adult_print' , 'cg_lar_sig' , 'cg_lar_date' ,
'cg_lar_print' , 'cg_lar_act' , 'cg_adult_sig_2' , 'cg_adult_date_2' ,
'cg_adult_print_2' , 'cg_lar_sig_3' , 'cg_lar_date_3' , 'cg_lar_print_3' ,
'cg_lar_act_3' , 'cg_lar_sig_4' , 'cg_lar_date_4' , 'cg_lar_print_4' ,
'cg_lar_act_4' , 'cg_staff_sig' , 'cg_staff_name' , 'cc_statement' , 'cc_name' ,
'cc_date' , 'subject_id' , 'uw_database', 'study_type', 'general_consent_complete' , 'co_open' ,
'co_datetime' , 'co_who' , 'co_notes' , 'contact_complete' , 'email_name',
'redcap_event_name', 'sid', 'district_pool', 'dashboard_id'])

# create new DataFrame for repo
repo = pd.DataFrame(scr, columns=['child' , 'adult' ,
'teen' , 'who_complete' , 'xx' , 'are_you' , 'are_you_cap' , 'do_you' ,
'do_you_cap' , 'have_you' , 'have_you_cap' , 'i_cap' ,
'i_have' , 'i_have_cap' , 'my_data' , 'their' , 'their_cap' , 'v_s' ,
'were_you' , 'were_you_cap' , 'you' , 'you_all_cap' , 'you_cap' ,
'you_and_your_child' , 'you_and_your_child_cap' , 'you_and_your' ,
'you_and_your_cap' , 'you_are' , 'you_are_cap' , 'you_have' ,
'you_have_cap' , 'you_or_your' , 'you_or_your_cap' , 'your' , 'your_cap' ,
'pronouns_complete', 'dob' , 'scr_date' , 'recruit', 'bilingual' , 'languages___1' ,
'languages___2' , 'languages___3' , 'languages___4' , 'languages___5' ,
'languages___6' , 'languages___7' , 'languages___8' , 'languages___9' ,
'languages___10' , 'languages___11' , 'languages___12' , 'languages___13' ,
'languages___14' , 'languages___15' , 'languages___16' ,
'languages___17' , 'languages___18' , 'languages___19' ,
'languages___20' , 'languages___21' , 'languages___98' ,
'languages_other' , 'primary_lang' , 'eng_age' , 'eng_daily' ,
'speech_dis' , 'speech_dis_dx___1' , 'speech_dis_dx___2' ,
'speech_dis_dx___3' , 'speech_dis_dx___4' , 'speech_dis_dx___5' ,
'speech_dis_dx___6' , 'speech_dis_dx___98' , 'speech_dis_other' ,
'speech_dis_treat' , 'aud_dis' , 'aud_dis_dx___1' , 'aud_dis_dx___2' ,
'aud_dis_dx___3' , 'aud_dis_dx___4' , 'aud_dis_dx___5' ,
'aud_dis_dx___98' , 'aud_dis_other' , 'aud_dis_treat' , 'dys_dx' ,
'dys_treat' , 'reading_rate' , 'adhd_dx' , 'ld_dx' , 'ld_treat' ,
'vision_dis' , 'brain_injury' , 'brain_injury_des' , 'brain_injury_cons',
'scr_hand', 'scr_comments', 'scr_metal', 'scr_metal_removal', 'scr_metal_removal_date',
'scr_braces', 'scr_braces_date', 'adhd_treat', 'adhd_medi', 'ld_dx_type___1', 'ld_dx_type___2',
'ld_dx_type___3', 'ld_dx_type___4', 'ld_dx_type___5', 'ld_dx_type___6', 'ld_dx_type___98',
'ld_dx_other', 'meds', 'meds_no_adhd', 'psych_dx', 'psych_dx_no_aut', 'autism_dx',
'vision_dis_corrected', 'vision_dis_treat', 'vision_dis_type___1', 'vision_dis_type___2',
'vision_dis_type___3', 'vision_dis_type___98', 'vision_dis_other', 'lang_num', 'eng_first',
'eng_fluency', 'lang_name_1', 'lang_name_2', 'lang_name_3', 'lang_name_4', 'lang_name_5',
'lang_age_1', 'lang_age_2', 'lang_age_3', 'lang_age_4', 'lang_age_5', 'lang_daily_1', 'lang_daily_2',
'lang_daily_3', 'lang_daily_4', 'lang_daily_5', 'lang_fluency_1', 'lang_fluency_2', 'lang_fluency_3',
'lang_fluency_4', 'lang_fluency_5', 'lang_daily_t_v', 'neuro_dx', 'neuro_dx_note', 'expedite',
'screening_complete' , 'scr_verified' , 'consent_staff', 'subject_id', 'redcap_event_name',
'sid', 'sid_email', 'scr_mri', 'other_lang_1', 'other_lang_2', 'other_lang_3', 'other_lang_4',
'other_lang_5', 'vision_dis_desc', 'study_type'])

# set all transfer fields to complete
scr.reg_xfer=1
scr.repo_xfer=1
scr.scr_delete=1

# create new DataFrame to mark subs as transfered
xfer =pd.DataFrame(scr, columns=['reg_xfer', 'repo_xfer', 'scr_delete'])

# write out csv files
reg.to_csv(home+'/Downloads/reg.csv')
repo.to_csv(home+'/Downloads/repo.csv')
xfer.to_csv(home+'/Downloads/xfer.csv')

# delete the file from which we're working for security!
os.remove(file)
