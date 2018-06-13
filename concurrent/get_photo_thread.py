import threading
from get_photos import out_wrapper, download_one, user_conf

@out_wrapper
def download_many():
    zzr = user_conf()
    task_list = []

    for item in zzr:
        t = threading.Thread(target=download_one, args=(item,))
        t.start()
        task_list.append(t)
    [t.join() for t in task_list]

if __name__ == '__main__':
    download_many()
