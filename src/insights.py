from src.jobs import read


def get_unique_job_types(path):

    jobs_list = read(path)
    unique_jobs = [jobs['job_type'] for jobs in jobs_list]
    return set(unique_jobs)


def filter_by_job_type(jobs, job_type):

    filtered_jobs = [job for job in jobs if job_type == job['job_type']]
    return filtered_jobs


def get_unique_industries(path):

    jobs_list = read(path)
    unique_industries = [job['industry']
                         for job in jobs_list
                         if job['industry']]
    return set(unique_industries)


def filter_by_industry(jobs, industry):
    filtered_industries = [job for job in jobs if job['industry'] == industry]
    return filtered_industries


def get_max_salary(path):
    jobs_list = read(path)
    all_salaries = [int(job['max_salary'])
                    for job in jobs_list
                    if job['max_salary'].isnumeric()]
    max_salary = max(all_salaries)
    return max_salary


def get_min_salary(path):
    jobs_list = read(path)
    all_salaries = [int(job['min_salary'])
                    for job in jobs_list
                    if job["min_salary"].isnumeric()]
    min_salary = min(all_salaries)
    return min_salary


def matches_salary_range(job, salary):
    if (
        'min_salary' not in job or
        'max_salary' not in job or
        type(job['max_salary']) != int or
        type(job['min_salary']) != int or
        job['max_salary'] < job['min_salary'] or
        type(salary) != int
    ):
        raise ValueError

    if job['min_salary'] <= salary <= job['max_salary']:
        return True
    return False


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
