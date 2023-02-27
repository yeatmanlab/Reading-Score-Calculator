import pandas as pd
import os
import glob

#  get path to most recent lookup table
ltpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'tables/')


#  load lookup tables into pandas dataframes
percentile_lt = pd.read_csv(os.path.join(ltpath, 'Standard Score to Percentile.csv'), index_col='standard.Score')


def towre_lookup(input_df, output_merged):
    """
    Look up TOWRE scores from lookup tables
    """
    towre_swe_lt = pd.read_csv(ltpath + 'TOWRE Sight Word Efficiency.csv', index_col='TOWRE.swe.raw')
    towre_pde_lt = pd.read_csv(ltpath + 'TOWRE Phonemic Decoding Efficiency.csv', index_col='TOWRE.pde.raw')
    towre_ranks_lt = pd.read_csv(ltpath + 'TOWRE Percentile Ranks.csv', index_col='TOWRE.index')
    towre_index_lt = pd.read_csv(ltpath + 'TOWRE Index.csv', index_col='TOWRE.sum')

    # look up towre swe ss & towre pde ss from raw (requires age)
    for x in range(len(output_merged)):
        # setting age values for iteration
        ageY = input_df.age_years[x]
        ageM = input_df.age_months[x]

        if ((ageY == 6) and (ageM >= 0) and (ageM <= 4)):
            towreSWElookup = "TOWRE.swe.6"
            towrePDElookup = "TOWRE.pde.6"
        elif ((ageY == 6) and (ageM >= 5) and (ageM <= 8)):
            towreSWElookup = "TOWRE.swe.6.5"
            towrePDElookup = "TOWRE.pde.6.5"
        elif ((ageY == 6) and (ageM >= 9) and (ageM <= 11)):
            towreSWElookup = "TOWRE.swe.6.9"
            towrePDElookup = "TOWRE.pde.6.9"
        elif ((ageY == 7) and (ageM >= 0) and (ageM <= 4)):
            towreSWElookup = "TOWRE.swe.7"
            towrePDElookup = "TOWRE.pde.7"
        elif ((ageY == 7) and (ageM >= 5) and (ageM <= 8)):
            towreSWElookup = "TOWRE.swe.7.5"
            towrePDElookup = "TOWRE.pde.7.5"
        elif ((ageY == 7) and (ageM >= 9) and (ageM <= 11)):
            towreSWElookup = "TOWRE.swe.7.9"
            towrePDElookup = "TOWRE.pde.7.9"
        elif ((ageY == 8) and (ageM >= 0) and (ageM <= 6)):
            towreSWElookup = "TOWRE.swe.8"
            towrePDElookup = "TOWRE.pde.8"
        elif ((ageY == 8) and (ageM >= 7) and (ageM <= 11)):
            towreSWElookup = "TOWRE.swe.8.7"
            towrePDElookup = "TOWRE.pde.8.7"
        elif ((ageY == 9) and (ageM >= 0) and (ageM <= 11)):
            towreSWElookup = "TOWRE.swe.9"
            towrePDElookup = "TOWRE.pde.9"
        elif ((ageY == 10) and (ageM >= 0) and (ageM <= 11)):
            towreSWElookup = "TOWRE.swe.10"
            towrePDElookup = "TOWRE.pde.10"
        elif ((ageY == 11) and (ageM >= 0) and (ageM <= 11)):
            towreSWElookup = "TOWRE.swe.11"
            towrePDElookup = "TOWRE.pde.11"
        elif ((ageY == 12) and (ageM >= 0) and (ageM <= 11)):
            towreSWElookup = "TOWRE.swe.12"
            towrePDElookup = "TOWRE.pde.12"
        elif ((ageY == 13) and (ageM >= 0) and (ageM <= 11)):
            towreSWElookup = "TOWRE.swe.13"
            towrePDElookup = "TOWRE.pde.13"
        elif ((ageY == 14) and (ageM >= 0) and (ageM <= 11)):
            towreSWElookup = "TOWRE.swe.14"
            towrePDElookup = "TOWRE.pde.14"
        elif ((ageY == 15) and (ageM >= 0) and (ageM <= 11)):
            towreSWElookup = "TOWRE.swe.15"
            towrePDElookup = "TOWRE.pde.15"
        elif ((ageY == 16) and (ageM >= 0) and (ageM <= 11)):
            towreSWElookup = "TOWRE.swe.16"
            towrePDElookup = "TOWRE.pde.16"
        elif ((ageY >= 17) and (ageM >= 0) and (ageM <= 11)):
            towreSWElookup = "TOWRE.swe.17"
            towrePDElookup = "TOWRE.pde.17"

        output_merged.twre_swe_ss[x] = towre_swe_lt.loc[input_df.twre_swe_raw[x]][towreSWElookup]
        output_merged.twre_pde_ss[x] = towre_pde_lt.loc[input_df.twre_pde_raw[x]][towrePDElookup]

    # look up towre sum, index & percentile rank
        if (output_merged.twre_swe_ss[x] != "X") & (output_merged.twre_pde_ss[x] != "X"):
            output_merged.twre_swe_perc[x] = percentile_lt.loc[int(output_merged.twre_swe_ss[x])]["percentile.Rank"]
            output_merged.twre_pde_perc[x] = percentile_lt.loc[output_merged.twre_pde_ss[x]]["percentile.Rank"]

            towreSum = int(output_merged.twre_pde_ss[x]) + int(output_merged.twre_swe_ss[x])
            output_merged.twre_index[x] = towre_index_lt.loc[towreSum]["TOWRE.index"]
            output_merged.twre_index_perc[x] = towre_ranks_lt.loc[output_merged.twre_index[x]]["TOWRE.percentile"]

        else:

            if (input_df.twre_swe_raw[x] == "N/A"):
                output_merged.twre_swe_raw[x] = "X"
                output_merged.twre_swe_perc[x] = "X"

            else:
                (input_df.twre_pde_ss[x] == "N/A")
                output_merged.twre_pde_raw[x] = "X"
                output_merged.twre_pde_perc[x] = "X"

            output_merged.twre_index[x] = "X"
            output_merged.twre_index_perc[x] = "X"

def ctopp_lookup(input_df, output_merged):
    """
    Look up CTOPP scores in lookup tables
    """
    ctopp_mfd_lt = pd.read_csv(ltpath + 'CTOPP Memory for Digits.csv', index_col='CTOPP.mfd.raw')
    ctopp_rdn_lt = pd.read_csv(ltpath + 'CTOPP Rapid Digit Naming.csv', index_col='CTOPP.rdn.raw')
    ctopp_rln_lt = pd.read_csv(ltpath + 'CTOPP Rapid Letter Naming.csv', index_col='CTOPP.rln.raw')
    ctopp_composite_lt = pd.read_csv(ltpath + 'CTOPP Standard to Composite Scores.csv', index_col='CTOPP.sum.2')
    for x in range(len(output_merged)):
        # setting age values for iteration
        ageY = input_df.age_years[x]
        ageM = input_df.age_months[x]

        if ((ageY == 4) and (ageM >= 0) and (ageM <= 3)):
            ctoppMFDsslookup = "CTOPP.mfd.ss.4"
            ctoppMFDplookup = "CTOPP.mfd.p.4"
            ctoppRDNsslookup = "CTOPP.rdn.ss.4"
            ctoppRDNplookup = "CTOPP.rdn.p.4"
            ctoppRLNsslookup = "CTOPP.rln.ss.4"
            ctoppRLNplookup = "CTOPP.rln.p.4"
        elif ((ageY == 4) and (ageM >= 4) and (ageM <= 7)):
            ctoppMFDsslookup = "CTOPP.mfd.ss.4.4"
            ctoppMFDplookup = "CTOPP.mfd.p.4.4"
            ctoppRDNsslookup = "CTOPP.rdn.ss.4.4"
            ctoppRDNplookup = "CTOPP.rdn.p.4.4"
            ctoppRLNsslookup = "CTOPP.rln.ss.4.4"
            ctoppRLNplookup = "CTOPP.rln.p.4.4"
        elif ((ageY == 4) and (ageM >= 8) and (ageM <= 11)):
            ctoppMFDsslookup = "CTOPP.mfd.ss.4.8"
            ctoppMFDplookup = "CTOPP.mfd.p.4.8"
            ctoppRDNsslookup = "CTOPP.rdn.ss.4.8"
            ctoppRDNplookup = "CTOPP.rdn.p.4.8"
            ctoppRLNsslookup = "CTOPP.rln.ss.4.8"
            ctoppRLNplookup = "CTOPP.rln.p.4.8"
        elif ((ageY == 5) and (ageM >= 0) and (ageM <= 5)):
            ctoppMFDsslookup = "CTOPP.mfd.ss.5"
            ctoppMFDplookup = "CTOPP.mfd.p.5"
            ctoppRDNsslookup = "CTOPP.rdn.ss.5"
            ctoppRDNplookup = "CTOPP.rdn.p.5"
            ctoppRLNsslookup = "CTOPP.rln.ss.5"
            ctoppRLNplookup = "CTOPP.rln.p.5"
        elif ((ageY == 5) and (ageM >= 6) and (ageM <= 11)):
            ctoppMFDsslookup = "CTOPP.mfd.ss.5.6"
            ctoppMFDplookup = "CTOPP.mfd.p.5.6"
            ctoppRDNsslookup = "CTOPP.rdn.ss.5.6"
            ctoppRDNplookup = "CTOPP.rdn.p.5.6"
            ctoppRLNsslookup = "CTOPP.rln.ss.5.6"
            ctoppRLNplookup = "CTOPP.rln.p.5.6"
        elif ((ageY == 6) and (ageM >= 0) and (ageM <= 5)):
            ctoppMFDsslookup = "CTOPP.mfd.ss.6"
            ctoppMFDplookup = "CTOPP.mfd.p.6"
            ctoppRDNsslookup = "CTOPP.rdn.ss.6"
            ctoppRDNplookup = "CTOPP.rdn.p.6"
            ctoppRLNsslookup = "CTOPP.rln.ss.6"
            ctoppRLNplookup = "CTOPP.rln.p.6"
        elif ((ageY == 6) and (ageM >= 6) and (ageM <= 11)):
            ctoppMFDsslookup = "CTOPP.mfd.ss.6.6"
            ctoppMFDplookup = "CTOPP.mfd.p.6.6"
            ctoppRDNsslookup = "CTOPP.rdn.ss.6.6"
            ctoppRDNplookup = "CTOPP.rdn.p.6.6"
            ctoppRLNsslookup = "CTOPP.rln.ss.6.6"
            ctoppRLNplookup = "CTOPP.rln.p.6.6"
        elif ((ageY == 7) and (ageM >= 0) and (ageM <= 5)):
            ctoppMFDsslookup = "CTOPP.mfd.ss.7"
            ctoppMFDplookup = "CTOPP.mfd.p.7"
            ctoppRDNsslookup = "CTOPP.rdn.ss.7"
            ctoppRDNplookup = "CTOPP.rdn.p.7"
            ctoppRLNsslookup = "CTOPP.rln.ss.7"
            ctoppRLNplookup = "CTOPP.rln.p.7"
        elif ((ageY == 7) and (ageM >= 6) and (ageM <= 11)):
            ctoppMFDsslookup = "CTOPP.mfd.ss.7.6"
            ctoppMFDplookup = "CTOPP.mfd.p.7.6"
            ctoppRDNsslookup = "CTOPP.rdn.ss.7.6"
            ctoppRDNplookup = "CTOPP.rdn.p.7.6"
            ctoppRLNsslookup = "CTOPP.rln.ss.7.6"
            ctoppRLNplookup = "CTOPP.rln.p.7.6"
        elif ((ageY == 8) and (ageM >= 0) and (ageM <= 11)):
            ctoppMFDsslookup = "CTOPP.mfd.ss.8"
            ctoppMFDplookup = "CTOPP.mfd.p.8"
            ctoppRDNsslookup = "CTOPP.rdn.ss.8"
            ctoppRDNplookup = "CTOPP.rdn.p.8"
            ctoppRLNsslookup = "CTOPP.rln.ss.8"
            ctoppRLNplookup = "CTOPP.rln.p.8"
        elif ((ageY == 9) and (ageM >= 0) and (ageM <= 11)):
            ctoppMFDsslookup = "CTOPP.mfd.ss.9"
            ctoppMFDplookup = "CTOPP.mfd.p.9"
            ctoppRDNsslookup = "CTOPP.rdn.ss.9"
            ctoppRDNplookup = "CTOPP.rdn.p.9"
            ctoppRLNsslookup = "CTOPP.rln.ss.9"
            ctoppRLNplookup = "CTOPP.rln.p.9"
        elif ((ageY == 10) and (ageM >= 0) and (ageM <= 11)):
            ctoppMFDsslookup = "CTOPP.mfd.ss.10"
            ctoppMFDplookup = "CTOPP.mfd.p.10"
            ctoppRDNsslookup = "CTOPP.rdn.ss.10"
            ctoppRDNplookup = "CTOPP.rdn.p.10"
            ctoppRLNsslookup = "CTOPP.rln.ss.10"
            ctoppRLNplookup = "CTOPP.rln.p.10"
        elif ((ageY == 11) and (ageM >= 0) and (ageM <= 11)):
            ctoppMFDsslookup = "CTOPP.mfd.ss.11"
            ctoppMFDplookup = "CTOPP.mfd.p.11"
            ctoppRDNsslookup = "CTOPP.rdn.ss.11"
            ctoppRDNplookup = "CTOPP.rdn.p.11"
            ctoppRLNsslookup = "CTOPP.rln.ss.11"
            ctoppRLNplookup = "CTOPP.rln.p.11"
        elif ((ageY == 12) and (ageM >= 0) and (ageM <= 11)):
            ctoppMFDsslookup = "CTOPP.mfd.ss.12"
            ctoppMFDplookup = "CTOPP.mfd.p.12"
            ctoppRDNsslookup = "CTOPP.rdn.ss.12"
            ctoppRDNplookup = "CTOPP.rdn.p.12"
            ctoppRLNsslookup = "CTOPP.rln.ss.12"
            ctoppRLNplookup = "CTOPP.rln.p.12"
        elif ((ageY == 13) and (ageM >= 0) and (ageM <= 11)):
            ctoppMFDsslookup = "CTOPP.mfd.ss.13"
            ctoppMFDplookup = "CTOPP.mfd.p.13"
            ctoppRDNsslookup = "CTOPP.rdn.ss.13"
            ctoppRDNplookup = "CTOPP.rdn.p.13"
            ctoppRLNsslookup = "CTOPP.rln.ss.13"
            ctoppRLNplookup = "CTOPP.rln.p.13"
        elif ((ageY == 14) and (ageM >= 0) and (ageM <= 11)):
            ctoppMFDsslookup = "CTOPP.mfd.ss.14"
            ctoppMFDplookup = "CTOPP.mfd.p.14"
            ctoppRDNsslookup = "CTOPP.rdn.ss.14"
            ctoppRDNplookup = "CTOPP.rdn.p.14"
            ctoppRLNsslookup = "CTOPP.rln.ss.14"
            ctoppRLNplookup = "CTOPP.rln.p.14"
        elif ((ageY >= 15) and (ageM >= 0) and (ageM <= 11)):
            ctoppMFDsslookup = "CTOPP.mfd.ss.15"
            ctoppMFDplookup = "CTOPP.mfd.p.15"
            ctoppRDNsslookup = "CTOPP.rdn.ss.15"
            ctoppRDNplookup = "CTOPP.rdn.p.15"
            ctoppRLNsslookup = "CTOPP.rln.ss.15"
            ctoppRLNplookup = "CTOPP.rln.p.15"

        output_merged.ctopp_md_ss[x] = ctopp_mfd_lt.loc[input_df.ctopp_md_raw[x]][ctoppMFDsslookup]
        output_merged.ctopp_md_perc[x] = ctopp_mfd_lt.loc[input_df.ctopp_md_raw[x]][ctoppMFDplookup]
        output_merged.ctopp_rd_ss[x] = ctopp_rdn_lt.loc[input_df.ctopp_rd_raw[x]][ctoppRDNsslookup]
        output_merged.ctopp_rd_perc[x] = ctopp_rdn_lt.loc[input_df.ctopp_rd_raw[x]][ctoppRDNplookup]
        output_merged.ctopp_rl_ss[x] = ctopp_rln_lt.loc[input_df.ctopp_rl_raw[x]][ctoppRLNsslookup]
        output_merged.ctopp_rl_perc[x] = ctopp_rln_lt.loc[input_df.ctopp_rl_raw[x]][ctoppRLNplookup]

    # look up ctopp rsn composite score & percentile
        if (output_merged.ctopp_rd_ss[x] != "X") & (output_merged.ctopp_rl_ss[x] != "X"):
            ctoppSum = int(output_merged.ctopp_rd_ss[x]) + int(output_merged.ctopp_rl_ss[x])
            output_merged.ctopp_rapid[x] = ctopp_composite_lt.loc[ctoppSum]["CTOPP.cs"]
            output_merged.ctopp_rapid_perc[x] = ctopp_composite_lt.loc[ctoppSum]["CTOPP.cs.p"]

        else:
            output_merged.ctopp_rapid[x] = "X"
            output_merged.ctopp_rapid_perc[x] = "X"

        if (output_merged.ctopp_rd_ss[x] == "X"):
            output_merged.ctopp_rd_raw[x] = "X"

        if (output_merged.ctopp_rl_ss[x] == "X"):
            output_merged.ctopp_rl_raw[x] = "X"

        if (output_merged.ctopp_md_ss[x] == "X"):
            output_merged.ctopp_md_raw[x] = "X"
            output_merged.ctopp_md_ss[x] = "X"
            output_merged.ctopp_md_perc[x] = "X"

def wj_lookup(input_df, output_merged):
    """
    Look up percentile from ss for wj assessments
    """
    # look up percentile from ss for wj assessments
    for x in range(len(output_merged)):
        output_merged.wj_lwid_perc[x] = percentile_lt.loc[input_df.wj_lwid_ss[x]]["percentile.Rank"]
        output_merged.wj_wa_perc[x] = percentile_lt.loc[input_df.wj_wa_ss[x]]["percentile.Rank"]
        output_merged.wj_or_perc[x] = percentile_lt.loc[input_df.wj_or_ss[x]]["percentile.Rank"]
        output_merged.wj_srf_perc[x] = percentile_lt.loc[input_df.wj_srf_ss[x]]["percentile.Rank"]
