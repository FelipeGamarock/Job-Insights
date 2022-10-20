from src.counter import count_ocurrences


def test_counter():
    assert count_ocurrences('src/jobs.csv', 'Brazil') == 3
    assert count_ocurrences('src/jobs.csv', 'BRAZIL') == 3
    assert count_ocurrences('src/jobs.csv', 'brazil') == 3
