# https://stackoverflow.com/questions/16989988/disable-signals-at-lldb-initialization

import lldb
import threading
import time


class UnixSignalConfig(threading.Thread):
    def __init__(self, debugger, sig_act_cfg):
        super(UnixSignalConfig, self).__init__()
        self._listener = debugger.GetListener()
        self._debugger = debugger
        self._interpreter = debugger.GetCommandInterpreter()
        self._handled = set()
        self._sig_act_cfg = sig_act_cfg

    def _suppress_signals(self, process):
        signals = process.GetUnixSignals()
        for (sig, act, cfg) in self._sig_act_cfg:
            if act == 'pass':
                signals.SetShouldPass(sig, cfg)
            elif act == 'stop':
                signals.SetShouldStop(sig, cfg)
            elif act == 'notify':
                signals.SetShouldNotify(sig, cfg)

    def run(self):
        while True:
            event = lldb.SBEvent()
            if not self._listener.PeekAtNextEvent(event):
                continue
            process = self._interpreter.GetProcess()
            if process and not process.GetUniqueID() in self._handled:
                self._suppress_signals(process)
                self._handled.add(process.GetUniqueID())
            time.sleep(0.03)

"""
import lldb
import sys
sys.path.append(os.path.expanduser(os.path.join('~', '.config/rcn_debug')))
from rcn.lldb.unix_signal_config import UnixSignalConfig
from rcn.amd64.unix_signal import *

def __lldb_init_module(debugger, *rest):
    sig_act_cfg = [
        (SIGIO, 'stop', False),
        (SIGTERM, 'stop', False)
        ]
    listener_thread = UnixSignalConfig(debugger, sig_act_cfg)
    listener_thread.start()
"""
