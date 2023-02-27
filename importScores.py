#!/usr/bin/env python
from scripts.lookuptables import *
from scripts.timepoints import prep_timepoints

def importScores(input_df):

    # TODO: streamline this process (creating output df)
    # create an output data frame
    output = pd.DataFrame(
        columns=['record_id', 'redcap_event_name', 'wj_lwid_raw', 'wj_lwid_ss', 'wj_lwid_perc', 'wj_wa_raw', 'wj_wa_ss',
                 'wj_wa_perc', 'wj_or_ss',
                 'wj_or_perc', 'wj_srf_correct_raw', 'wj_srf_incorrect_raw', 'wj_srf_ss', 'wj_srf_perc', 'wj_mff_raw',
                 'wj_mff_ss',
                 'wj_mff_perc', "wj_brs", "wj_brs_perc", "wj_brs_level", "wj_rf", "wj_rf_perc", "wj_rf_level",
                 'twre_swe_raw', 'twre_swe_ss', 'twre_swe_perc', 'twre_pde_raw', 'twre_pde_ss', 'twre_pde_perc',
                 'twre_index_sum', 'twre_index',
                 'twre_index_perc', 'ctopp_md_raw', 'ctopp_md_ss', 'ctopp_md_perc', 'ctopp_rd_raw', 'ctopp_rd_ss',
                 'ctopp_rd_perc', 'ctopp_rl_raw',
                 'ctopp_rl_ss', 'ctopp_rl_perc', 'ctopp_rapid_sum', 'ctopp_rapid', 'ctopp_rapid_perc', 'study_name',
                 'lmb_cohort', 'intervention', 'study_format', 'mock_mri_run', 'mri_run', 'wj_run', 'towre_run',
                 'wasi_run', 'ctopp_run',
                 'ames_run', 'wj_form_num', 'wj_form', 'wj_lwid_run', 'wj_wa_run', 'wj_or_run', 'wj_srf_run',
                 'wj_mff_run', 'towre_form_num', 'towre_form', 'towre_swe_run', 'towre_pde_run', 'wasi_vocab_run',
                 'wasi_mr_run', 'ctopp_md_run', 'ctopp_rd_run', 'ctopp_rl_run', 'ames_type___1', 'ames_type___2',
                 'ames_type___3', 'ames_type___4', 'ames_type___5'])

    # merge input values to output
    output_merged = pd.merge(input_df, output, how="outer",
                             on=["record_id", "redcap_event_name", "wj_lwid_raw", "wj_lwid_ss", "wj_wa_raw", "wj_wa_ss",
                                 "wj_or_ss",
                                 "wj_srf_correct_raw", "wj_srf_incorrect_raw", "wj_srf_ss", "wj_mff_raw", "wj_mff_ss",
                                 "wj_mff_perc", "wj_brs", "wj_brs_perc", "wj_brs_level", "wj_rf", "wj_rf_perc",
                                 "wj_rf_level",
                                 "twre_swe_raw", "twre_pde_raw", "ctopp_md_raw", "ctopp_rd_raw", "ctopp_rl_raw"])

    ##########################

    # run sheet prep for each timepoint
    prep_timepoints(input_df, output_merged)

    # perform look ups for each test
    towre_lookup(input_df, output_merged)
    ctopp_lookup(input_df, output_merged)
    wj_lookup(input_df, output_merged)

    x = len(output_merged) - 1
    # remove values that aren't in redcap + automatically calculated sum values from final .csv
    if (input_df.timepoint[x] == "CHIN") | (input_df.timepoint[x] == "B2") | (input_df.timepoint[x] == "F3") | (
            input_df.timepoint[x] == "S4"):
        output_merged.drop(
            columns=['timepoint', 'age_years', 'age_months', 'twre_index_sum', 'ctopp_md_raw', 'ctopp_md_ss',
                     'ctopp_md_perc', 'ctopp_rd_raw', 'ctopp_rd_ss', 'ctopp_rd_perc', 'ctopp_rl_raw',
                     'ctopp_rl_ss', 'ctopp_rl_perc', 'ctopp_rapid_sum', 'ctopp_rapid', 'ctopp_rapid_perc'],
            inplace=True)
    else:
        output_merged.drop(columns=['timepoint', 'age_years', 'age_months', 'ctopp_rapid_sum', 'twre_index_sum'],
                           inplace=True)

    return output_merged
    # # write output to .csv
    # output_merged.to_csv(home + '/Downloads/score_output.csv', index=False)
    #
    # print("score_output.csv generated successfully!")



#DEBUGGING/TESTING
if __name__ == '__main__':
    import os
    import glob
    home = os.path.expanduser('~')
    path = max(glob.iglob(home+'/Documents/redcap/scoreinput.csv'), key=os.path.getctime)
    df = pd.read_csv(path)
    output = importScores(df)
    output.to_csv(home + '/Downloads/score_output.csv', index=False)

    print("score_output.csv generated successfully!")
