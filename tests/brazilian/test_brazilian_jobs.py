from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    brazilian_jobs = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    assert 'title' in brazilian_jobs[0]
    assert 'salary' in brazilian_jobs[0]
    assert 'type' in brazilian_jobs[0]
