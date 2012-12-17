#!/usr/bin/python
#-*-coding:utf-8-*-

"""
    Video-wall controller (pc's) with web-interface (flask)
"""

from flask import Flask, render_template, jsonify, request
from subprocess import Popen
import yaml
from os import path, environ, system
from geometry import vports_recall

#import socket
#import fcntl
#import struct

#def get_ip_address(ifname):
#    s = socket.socket(socket.SOCK_DGRAM)
#    return socket.inet_ntoa(fcntl.ioctl(
#        s.fileno(),
#        0x8915,  # SIOCGIFADDR
#        struct.pack('256s', ifname[:15])
#    )[20:24])

app = Flask(__name__)

#my_ip = get_ip_address('eth1')
my_ip = '192.168.28.116'

my_passwd = 'user'

#vp_matrix = vports_recall(640, 480)
vp_matrix = vports_recall(1920, 1080)
#vp_matrix = vports_recall(1280, 960)

daemonizer = path.join(path.dirname(__file__), 'dmnexec.py')
cfg_file = path.join(path.dirname(__file__), 'config.yml')


class config(object):
    """ Config driver """
    def __init__(self, cfgfile):
        self.fl = cfgfile

    def r(self):
        return yaml.load(open(self.fl))

    def w(self, data):
        return yaml.safe_dump(data, open(self.fl, 'w'))
cfg = config(cfg_file)


def run(command, params=None):
    conf = cfg.r()

    print(str(conf['vsources']['panta']['addr']).split('://')[1])

    #print command, params
    cmd = ''
    if command == 'run_vp':
        scrid = params['screen']
        vpid = params['vp']
        environ['DISPLAY'] = ':0'
        pos_x, pos_y, res_w, res_h = vp_matrix[vpid]

        ply_params = dict(
            #            ply_drv         = '-vo vdpau -vc ffh264vdpau' if res_w >= 640 else '',
            ply_drv='-vo vdpau -vc ffh264vdpau',
            ply_sz='-x {} -y {}'.format(res_w, res_h),
            ply_pos='-geometry {}:{}'.format(pos_x, pos_y),
            ply_name='-name "{}.{}"'.format(scrid, vpid)
        )

        cmd = 'xdotool search --classname "{}.{}" windowkill %@'.format(scrid, vpid)
        system(cmd)

        if not vpid in conf['screens'][scrid]['vports']:
            return
        vsrcalias = conf['screens'][scrid]['vports'][vpid]
        vsrc = conf['vsources'][vsrcalias]
        if vsrc['addr'][0:4] == 'rtsp':
            cam_params = dict(
                cam_ip=vsrc['addr'][7:],  # rtsp://[ip.ip.ip.ip]
                cam_res='resolution={}x{}'.format(640, 360) if res_w <= 640 else '',
                cam_audio='&audio=0',
                #   cam_label='',
                #   cam_label='&text=1&textstring=&textcolor=white&textbackgroundcolor=transparent&clock=1&date=1'
                #   cam_label='&text=1&textstring={}:{}'
                #       '&textcolor=white'
                #       '&textbackgroundcolor=semitransparent'
                #       '&clock=1'
                #       '&date=1'
                #           .format(scrid, vsrcalias),
            )

            # cmd = 'mplayer rtsp://%(cam_ip)s/axis-media/media.amp?%(cam_res)s%(cam_audio)s%(cam_label)s ' \
            # '%(ply_drv)s %(ply_sz)s %(ply_pos)s -noborder %(ply_name)s' % dict(ply_params.items()
            # + cam_params.items())

            cmd = 'mplayer rtsp://%(cam_ip)s/axis-media/media.amp?%(cam_res)s%(cam_audio)s '\
                  '%(ply_drv)s %(ply_sz)s %(ply_pos)s -noborder %(ply_name)s' % \
                  dict(ply_params.items() + cam_params.items())

        elif vsrc['addr'][0:4] == 'file':
            file_params = dict(
                path=vsrc['addr'][7:]
            )
            cmd = 'mplayer %(path)s %(ply_drv)s %(ply_sz)s %(ply_pos)s -noborder %(ply_name)s -loop 0'\
                  % dict(file_params.items() + ply_params.items())

    elif command == 'resetvps':
        cmd = 'pkill mplayer'

    elif command == 'init':
        print my_ip
        for scr in conf['screens']:
            if conf['screens'][scr]['ip'] == my_ip:
                for vp in conf['screens'][scr]['vports']:
                    run('run_vp', {'screen': scr, 'vp': vp})

    elif command == 'shutdown':
        system('echo {}|sudo -S shutdown -h now'.format(my_passwd))

    elif command == 'restart':
        system('echo {}|sudo -S shutdown -h now'.format(my_passwd))

    print cmd
    Popen([daemonizer] + cmd.split())
    return
run('init')


@app.route('/')
def index():
    return render_template('index.html', SELF=my_ip)


@app.route('/shutdown/', methods=['POST'])
def shutdown():
    run('shutdown')
    return render_template('empty.html')


@app.route('/restart/', methods=['POST'])
def shutdown():
    run('restart')
    return render_template('empty.html')


@app.route('/conf/')
def retconf():
    return jsonify(screens=cfg.r()['screens'])


@app.route('/layout/<scrname>', methods=['GET', 'POST'])
def layout(scrname):
    conf = cfg.r()
    srv = request.values.get('srv')

    if request.method == 'POST':
        vt_type = request.values.get('vt_type')
        if vt_type[0:2] == 'vt':
            conf['screens'][scrname]['vt_type'] = vt_type
            conf['screens'][scrname]['vports'] = {}
            cfg.w(conf)
        if conf['screens'][scrname]['ip'] == my_ip:
            run('resetvps')

    if scrname in conf['screens']:
        tmpl_name = conf['screens'][scrname]['vt_type']
        if srv == my_ip:
            st = {}
            lbl = {}
            lnk = {}
            for vport, vsource in dict(conf['screens'][scrname]['vports']).iteritems():
                st[vport] = 'play'
                lbl[vport] = conf['vsources'][vsource]['title']
                addr = str(conf['vsources'][vsource]['addr']).split('://')[1]
                if addr.find('@') > -1:
                    addr = addr.split('@')[1]
                lnk[vport] = '{}://{}'.format('http', addr)
                print(lnk[vport])
            return render_template('.'.join((tmpl_name, 'html')), st=st, lbl=lbl, lnk=lnk)
        else:
            return render_template('empty.html')
    else:
        return render_template('empty.html')


@app.route('/setvpsrc/<scrname>', methods=['GET', 'POST'])
def setvpsrc(scrname):
    if request.method == 'POST':
        vpid = request.values.get('vpid')
        srcalias = request.values.get('srcalias')
        screxe = request.values.get('screxe')
        print srcalias, vpid
        conf = cfg.r()
        if srcalias != '---':
            conf['screens'][scrname]['vports'][vpid] = srcalias
        else:
            if vpid in conf['screens'][scrname]['vports']:
                del conf['screens'][scrname]['vports'][vpid]
        cfg.w(conf)

        if my_ip == conf['screens'][screxe]['ip']:
        #   print 'Ok!'
        #   return redirect(url_for(run(conf['screens'][scrname]['ip'], 'run_vp', {'screen':scrname, 'vp':vpid})))
            run('run_vp', {'screen': scrname, 'vp': vpid})
        return render_template('empty.html')

    elif request.method == 'GET':
        vs = []
        for itm in cfg.r()['vsources'].items():
            addr = str(itm[1]['addr']).split('://')[1]
            if addr.find('@') > -1:
                addr = addr.split('@')[1]
            ptzlink = '{}://{}/'.format('http', addr)
            name = itm[1]['title']
            title = itm[0]
            vs.append(dict(ptzlink=ptzlink, title=title, name=name))
        return render_template('videosrcs.html', vs=vs)


@app.route('/vsources/')
def vsources():
    return render_template('vsources_dlg.html', vsconfig=cfg.r()['vsources'])


@app.route('/vsources/<vsrcid>/del', methods=['POST'])
def vsrcdel(vsrcid):
    conf = cfg.r()
    del conf['vsources'][vsrcid]
    cfg.w(conf)
    return render_template('empty.html')


@app.route('/vsources/<vsrcid>/add', methods=['GET', 'POST'])
def vsrcadd(vsrcid):
    vs_title = request.values.get('vstitle')
    vs_addr = request.values.get('vsaddr')
    conf = cfg.r()
    conf['vsources'][vsrcid] = dict(title=vs_title, addr='rtsp://' + str(vs_addr))
    cfg.w(conf)
    return render_template('empty.html')


if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0', port=8008)
