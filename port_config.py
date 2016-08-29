#!/usr/bin/env python
#coding=utf-8

import os
import logging
import re

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S')
def config_stats():
    """
    config the all port of config.py in the marathon-lb
    :None
    """
    if not os.path.isfile('config.py'):
        logging.debug("The file: config.py doesn't exist...")
        return
    try:
        with open('config.py','r+') as fd:
            flag_stats=False
            for line in fd.readlines():
                with open('config_tmp.py','a+') as ftmp:

                    stats_r=re.match("listen stats\n",line)
                    if stats_r or flag_stats:
                        logging.debug("Find the line:{}".format(line))
                        if stats_r:
                            flag_stats=True
                            ftmp.write(line)
                            continue
                        elif flag_stats:
                            stat_bind=re.match("  bind ",line)
                            if stat_bind:
                                logging.debug("Find the line:{}".format(line))
                                stat_port=os.getenv("STATS")
                                logging.debug("Get the envvariable:{}".format(stat_port))
                                sub_r="  bind 0.0.0.0:{}".format(stat_port)
                                line=re.sub(r"  bind 0.0.0.0:10002",sub_r,line)
                                logging.debug("The dealed line :{}".format(sub_r))
                                ftmp.write(line)
                                flag_stats=False
                            else:
                                ftmp.wrie(line)
                    else:
                        ftmp.write(line)
    except Exception:
        logging.debug("Open or Read the config.py Failed!...")
    os.system("rm -rf config.py")
    os.system("cp config_tmp.py config.py")
    os.system("rm -rf config_tmp.py")
def config_marathon_http_in():
    """
    config the all port of config.py in the marathon-lb
    :None
    """
    if not os.path.isfile('config.py'):
        logging.debug("The file: config.py doesn't exist...")
        return
    try:
        with open('config.py','r+') as fd:
            flag_marathon_http_in=False
            for line in fd.readlines():
                with open('config_tmp.py','a+') as ftmp:

                    marathon_http_in_r=re.match("frontend marathon_http_in\n",line)
                    if marathon_http_in_r or flag_marathon_http_in:
                        logging.debug("Find the line:{}".format(line))
                        if marathon_http_in_r:
                            flag_marathon_http_in=True
                            ftmp.write(line)
                            continue
                        elif flag_marathon_http_in:
                            stat_bind_marathon_http_in=re.match("  bind ",line)
                            if stat_bind_marathon_http_in:
                                logging.debug("Find the line:{}".format(line))
                                marathon_http_in_port=os.getenv("MARATHON_HTTP_IN")
                                logging.debug("Get the envvariable:{}".format(marathon_http_in_port))
                                marathon_http_in_sub_r="  bind *:{}".format(marathon_http_in_port)
                                marathon_http_in_line=re.sub(r"  bind \*:8080",marathon_http_in_sub_r,line)
                                logging.debug("The dealed line :{}".format(marathon_http_in_line))
                                ftmp.write(marathon_http_in_line)
                                flag_marathon_http_in=False
                            else:
                                ftmp.wrie(line)
                    else:
                        ftmp.write(line)
    except Exception:
        logging.debug("Open or Read the config.py Failed!...")
    os.system("rm -rf config.py")
    os.system("cp config_tmp.py config.py")
    os.system("rm -rf config_tmp.py")
def config_marathon_http_appid_in():
    """
    config the marathon_http_appid_in's port of config.py in the marathon-lb
    :None
    """
    if not os.path.isfile('config.py'):
        logging.debug("The file: config.py doesn't exist...")
        return
    try:
        with open('config.py','r+') as fd:
            flag_marathon_http_appid_in=False
            for line in fd.readlines():
                with open('config_tmp.py','a+') as ftmp:

                    marathon_http_appid_in_r=re.match("frontend marathon_http_appid_in\n",line)
                    if marathon_http_appid_in_r or flag_marathon_http_appid_in:
                        logging.debug("Find the line:{}".format(line))
                        if marathon_http_appid_in_r:
                            flag_marathon_http_appid_in=True
                            ftmp.write(line)
                            continue
                        elif flag_marathon_http_appid_in:
                            stat_bind_marathon_http_appid_in=re.match("  bind ",line)
                            if stat_bind_marathon_http_appid_in:
                                logging.debug("Find the line:{}".format(line))
                                marathon_http_appid_in_port=os.getenv("MARATHON_HTTP_APPID_IN")
                                logging.debug("Get the envvariable:{}".format(marathon_http_appid_in_port))
                                marathon_http_appid_in_sub_r="  bind *:{}".format(marathon_http_appid_in_port)
                                marathon_http_appid_in_line=re.sub(r"  bind \*:9091",marathon_http_appid_in_sub_r,line)
                                logging.debug("The dealed line :{}".format(marathon_http_appid_in_line))
                                ftmp.write(marathon_http_appid_in_line)
                                flag_marathon_http_appid_in=False
                            else:
                                ftmp.wrie(line)
                    else:
                        ftmp.write(line)
    except Exception:
        logging.debug("Open or Read the config.py Failed!...")
    os.system("rm -rf config.py")
    os.system("cp config_tmp.py config.py")
    os.system("rm -rf config_tmp.py")
def config_marathon_https_in():
    """
    config the all port of config.py in the marathon-lb
    :None
    """
    if not os.path.isfile('config.py'):
        logging.debug("The file: config.py doesn't exist...")
        return
    try:
        with open('config.py','r+') as fd:
            flag_marathon_https_in=False
            for line in fd.readlines():
                with open('config_tmp.py','a+') as ftmp:

                    marathon_https_in_r=re.match("frontend marathon_https_in\n",line)
                    if marathon_https_in_r or flag_marathon_https_in:
                        logging.debug("Find the line:{}".format(line))
                        if marathon_https_in_r:
                            flag_marathon_https_in=True
                            ftmp.write(line)
                            continue
                        elif flag_marathon_https_in:
                            stat_bind_marathon_https_in=re.match("  bind ",line)
                            if stat_bind_marathon_https_in:
                                logging.debug("Find the line:{}".format(line))
                                marathon_https_in_port=os.getenv("MARATHON_HTTPS_IN")
                                logging.debug("Get the envvariable:{}".format(marathon_https_in_port))
                                marathon_https_in_sub_r="  bind *:{} ssl ".format(marathon_https_in_port)+"{"+"sslCert"+"}"
                                logging.debug("The marathon_https_in_sub_r : {}".format(marathon_https_in_sub_r))
                                marathon_https_in_line=re.sub(r"  bind \*:443 ssl \{sslCerts\}",marathon_https_in_sub_r,line)
                                logging.debug("The dealed line :{}".format(marathon_https_in_line))
                                ftmp.write(marathon_https_in_line)
                                flag_marathon_https_in=False
                            else:
                                ftmp.wrie(line)
                    else:
                        ftmp.write(line)
    except Exception:
        logging.debug("Open or Read the config.py Failed!...")
    os.system("rm -rf config.py")
    os.system("cp config_tmp.py config.py")
    os.system("rm -rf config_tmp.py")



if __name__=='__main__':
    config_stats()
    config_marathon_http_in()
    config_marathon_http_appid_in()
    #config_marathon_https_in()

