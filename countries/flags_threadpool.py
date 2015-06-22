"""Download flags of top 20 countries by population

ThreadPoolExecutor version

Sample run::

    $ python3 flags_threadpool.py
    BD retrieved.
    EG retrieved.
    CN retrieved.
    ...
    PH retrieved.
    US retrieved.
    IR retrieved.
    20 flags downloaded in 0.93s

"""
# BEGIN FLAGS_THREADPOOL
from concurrent import futures

from flags import save_flag, get_flag, show, main  # Ⓐ

MAX_WORKERS = 20  # Ⓑ


def download_one(cc):  # Ⓒ
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


def download_many(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))  # Ⓓ
    with futures.ThreadPoolExecutor(workers) as executor:  # Ⓔ
        res = executor.map(download_one, sorted(cc_list))  # Ⓕ

    return len(list(res))  # Ⓖ


if __name__ == '__main__':
    main(download_many)  # Ⓗ
# END FLAGS_THREADPOOL
