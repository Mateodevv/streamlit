import finanzInformatikConnector as fI
import pandas as pd

# Every connector adds its Data to the List to concat the Data to one DataFrame.
clustered_jobtitles = [fI.get_clustered_job_title()]
jobamount_over_time = [fI.get_jobamount_over_time()]
jobtitles_over_time = [fI.get_jobtitles_over_time()]


def get_concated_clustered_jobtitles():
    return pd.concat(clustered_jobtitles, ignore_index=True)


def get_concated_jobamount_over_time():
    return pd.concat(jobamount_over_time, ignore_index=True)


def get_concated_jobtitles_over_time():
    return pd.concat(jobtitles_over_time, ignore_index=True)
