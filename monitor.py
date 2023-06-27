"""cron: 00 00 * * * /usr/bin/python3 /home/zer0py2C/monitor.py"""
import os
import time
import sys
import datetime
import subprocess

today = datetime.datetime.now().strftime("%Y%m%d")


def exec_cmd(args):
    try:
        proc = subprocess.Popen(
            args, stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        out, err = proc.communicate()
        if proc.returncode != 0:
            raise OSError(err)
    except OSError:
        sys.exit(1)

    return str(out, "utf-8")


def ensure_monitor_uniq(ps_name):
    ps_out = exec_cmd(["ps", "kstart_time", "-ef", "|",
                       "grep", ps_name, "|",
                       "awk", "'{print $2}'"])
    for pid in ps_out.split("\n")[:-1]:
        pid.isdigit() and exec_cmd(["kill", "-15", pid])


def aggs_csv(csv_path):
    pass


def main():
    username = "zer0py2C"
    home_path = "/home/%s/" % username
    watch_file = home_path + "%s.csv" % today
    ensure_monitor_uniq(home_path + "[m]onitor.py")
    while 1:
        time.sleep(3)
        if os.path.isfile(watch_file) and \
            os.path.getsize(watch_file) > 0:
            aggs_csv(watch_file)
            break


if __name__ == "__main__":
    main()
