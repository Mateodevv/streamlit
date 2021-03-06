import finanzInformatikDataPipe as fI
import cluster

initDF = fI.find_job_offers()


def get_clustered_job_title():
    return cluster.get_clustered_job_titles(initDF)


def get_jobamount_over_time():
    return cluster.get_jobamount_over_time(initDF)


def get_jobtitles_over_time():
    return cluster.get_jobtitles_over_time(initDF)
