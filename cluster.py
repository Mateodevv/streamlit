import re
import pandas as pd


# Wrapper method. Builds a DataFrame with data provided from label_titles().
def get_clustered_job_titles(df):
    admin, consultant, datajobs, entwicklung, fachlich, leitung, security, sonstige = label_titles(df)

    source = pd.DataFrame({
        'Jobbezeichnung': ['entwicklung', 'datajobs', 'systemadmin', 'security', 'consultant', 'leitung', 'fachlich',
                           'sonstige'],
        'offene Stellen': [entwicklung, datajobs, admin, security, consultant, leitung, fachlich, sonstige]
    })
    return source


def get_jobamount_over_time(df):
    uniquedates = df.date.unique()
    date = []
    amount = []

    # Sums amount of job listings for a date
    for udate in uniquedates:
        tmp = df.loc[df['date'] == udate]
        amount.append(len(tmp.index))
        date.append(udate)

    return pd.DataFrame({'Anzahl Ausschreibungen': amount, 'Datum': date})


def get_jobtitles_over_time(df):
    columns = ["job_title", "date", "amount"]
    data = pd.DataFrame(columns=columns)
    # selects all the unique dates from the DataFrame. Used for easy iterating.
    uniquedates = df.date.unique()
    for udate in uniquedates:
        tmpdf = df.loc[df['date'] == udate]
        admin, consultant, datajobs, entwicklung, fachlich, leitung, security, sonstige = label_titles(tmpdf)
        rows = [
            {"job_title": "Systemadmin", "date": udate, "amount": admin},
            {"job_title": "Berater/Consultant", "date": udate, "amount": consultant},
            {"job_title": "Datajobs", "date": udate, "amount": datajobs},
            {"job_title": "Entwicklung", "date": udate, "amount": entwicklung},
            {"job_title": "Facharbeiter", "date": udate, "amount": fachlich},
            {"job_title": "Führungskraft", "date": udate, "amount": leitung},
            {"job_title": "Security", "date": udate, "amount": security},
            {"job_title": "Sonstige", "date": udate, "amount": sonstige}
        ]
        for row in rows:
            data = data.append(row, ignore_index=True)

    return data


def label_titles(df):
    entwicklung = 0
    datajobs = 0
    admin = 0
    security = 0
    consultant = 0
    leitung = 0
    fachlich = 0
    sonstige = 0
    # Checks for specific keywords in the listing title to label it and counts the sum.
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
    return admin, consultant, datajobs, entwicklung, fachlich, leitung, security, sonstige
