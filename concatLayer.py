import finanzInformatikConnector as fICon
import fiduciaGADConnector as fiduCon
import pandas as pd
from utils import trendwordlist
import re

# Every connector adds its Data to the List to concat the Data to one DataFrame.
clustered_jobtitles = [fICon.get_clustered_job_title()]
jobamount_over_time = [fICon.get_jobamount_over_time()]
jobtitles_over_time = [fICon.get_jobtitles_over_time()]

clustered_jobtitles_fidu = fiduCon.get_clustered_job_title()
jobamount_over_time_fidu = fiduCon.get_jobamount_over_time()
jobtitles_over_time_fidu = fiduCon.get_jobtitles_over_time()

text_fidu = fiduCon.get_text()

trendlist = trendwordlist.get_trend_wordlist()
mentions = []
for x in range(len(trendlist)):
    trendlist[x] = trendlist[x].lower()
    mentions.append(0)


def get_concated_clustered_jobtitles():
    return pd.concat(clustered_jobtitles, ignore_index=True)


def get_concated_jobamount_over_time():
    return pd.concat(jobamount_over_time, ignore_index=True)


def get_concated_jobtitles_over_time():
    return pd.concat(jobtitles_over_time, ignore_index=True)


def get_fidu_clustered_jobtitles():
    return clustered_jobtitles_fidu


def get_fidu_jobamount_over_time():
    return jobamount_over_time_fidu


def get_fidu_jobtitles_over_time():
    return jobtitles_over_time_fidu


def get_trendmentions():
    for text in text_fidu:
        for trend in range(len(trendlist)):
            for word in text.split():
                if re.search(rf'\b{trendlist[trend]}\b', word.lower()):
                    mentions[trend] += 1
    df = pd.DataFrame(list(zip(trendlist, mentions)),
                      columns=['trend', 'mentioned'])
    print(df)
    return df.sort_values(['mentioned'], ascending=[False]).head(10)


def get_fidu_clustered_jobtitles():
    return clustered_jobtitles_fidu


def get_fidu_jobamount_over_time():
    return jobamount_over_time_fidu


def get_fidu_jobtitles_over_time():
    return jobtitles_over_time_fidu


def get_trendmentions():
    for text in text_fidu:
        for trend in range(len(trendlist)):
            for word in text.split():
                if re.search(rf'\b{trendlist[trend]}\b', word.lower()):
                    mentions[trend] += 1
    df = pd.DataFrame(list(zip(trendlist, mentions)),
                      columns=['trend', 'mentioned'])
    print(df)
    return df.sort_values(['mentioned'], ascending=[False]).head(10)
