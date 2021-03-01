import re
import pandas as pd


def cluster_job_titles_timeseries(df):
    entwicklung = 0
    datajobs = 0
    admin = 0
    security = 0
    consultant = 0
    leitung = 0
    fachlich = 0
    sonstige = 0

    columns = ['entwicklung', 'datajobs', 'admin', 'security', 'consultant', 'leitung', 'fachlich', 'sonstige', 'date']
    clustered_df = pd.DataFrame(columns=columns)

    uniquedates = df.date.unique()
    for date in uniquedates:
        tmp = df.loc[df['date'] == date]
        for index, row in tmp.iterrows():
            job_title = str(row["job_title"]).lower()
            if re.search("leiter", job_title):
                leitung += 1
            elif re.search("data", job_title):
                datajobs += 1
            elif re.search("software", job_title) or re.search("entwickl", job_title):
                entwicklung += 1
            elif re.search("system", job_title) or re.search("admin", job_title) or re.search("architect",
                                                                                              job_title) or re.search(
                "netzwerk", job_title):
                admin += 1
            elif re.search("security", job_title) or re.search("sicherheit", job_title):
                security += 1
            elif re.search("consultant", job_title) or re.search("berater", job_title):
                consultant += 1
            elif re.search("produktverant", job_title) or re.search("manager", job_title) or re.search("fachlich",
                                                                                                       job_title):
                fachlich += 1

            else:
                sonstige += 1

        new_row = {'entwicklung': entwicklung, 'datajobs': datajobs, 'admin': admin, 'security': security,
                   'consultant': consultant, 'leitung': leitung, 'fachlich': fachlich, 'sonstige': sonstige,
                   'date': date}
        clustered_df = clustered_df.append(new_row, ignore_index=True)

    return clustered_df


def cluster_job_titles(df):
    entwicklung = 0
    datajobs = 0
    admin = 0
    security = 0
    consultant = 0
    leitung = 0
    fachlich = 0
    sonstige = 0


    for index, row in df.iterrows():
        job_title = str(row["job_title"]).lower()
        if re.search("leiter", job_title):
            leitung += 1
        elif re.search("data", job_title):
            datajobs += 1
        elif re.search("software", job_title) or re.search("entwickl", job_title):
            entwicklung += 1
        elif re.search("system", job_title) or re.search("admin", job_title) or re.search("architect",
                                                                                          job_title) or re.search(
            "netzwerk", job_title):
            admin += 1
        elif re.search("security", job_title) or re.search("sicherheit", job_title):
            security += 1
        elif re.search("consultant", job_title) or re.search("berater", job_title):
            consultant += 1
        elif re.search("produktverant", job_title) or re.search("manager", job_title) or re.search("fachlich",
                                                                                                   job_title):
            fachlich += 1

        else:
            sonstige += 1

    source = pd.DataFrame({
        'Jobbezeichnung': ['entwicklung', 'datajobs', 'admin', 'security', 'consultant', 'leitung', 'fachlich', 'sonstige'],
        'offene Stellen': [entwicklung, datajobs, admin, security, consultant, leitung, fachlich, sonstige]
    })
    return source
