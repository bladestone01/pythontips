from concurrent import futures
from get_photos import out_wrapper, download_one, user_conf

@out_wrapper
def download_many():
    zzr = user_conf()
    with futures.ThreadPoolExecutor(len(zzr)) as executor:
        to_do = [executor.submit(download_one, item) for item in zzr]
        ret = [future.result() for future in futures.as_completed(to_do)]
    return ret

if __name__ == '__main__':
    download_many()
