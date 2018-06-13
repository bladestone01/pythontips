from gevent import monkey
monkey.patch_all()

import gevent

from get_photos import out_wrapper, download_one, user_conf

@out_wrapper
def download_many():
    zzr = user_conf()
    jobs = [gevent.spawn(download_one, item) for item in zzr]
    gevent.joinall(jobs)


if __name__ == '__main__':
    download_many()
