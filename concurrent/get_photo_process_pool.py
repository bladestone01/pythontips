from concurrent import futures
from get_photos import out_wrapper, download_one, user_conf

@out_wrapper
def download_many():
    zzr = user_conf()
    with futures.ProcessPoolExecutor(len(zzr)) as executor:
        res = executor.map(download_one, zzr)
    return len(list(res))

if __name__ == '__main__':
    download_many()
