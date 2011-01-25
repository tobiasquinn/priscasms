# This sends an sms using gammu either locally or by executing
# gammu on a remote host using ssh - ssh is expected to be setup
# for passwordless login from the sending host
import re
from paramiko import SSHClient

class SendSMS:
    def _gammuCommand(self, number, message):
        return "echo gammu sendsms TEXT %s -text '%s'" % (number, re.escape(message))

    def sendSMS(self, number, message, sshHost=None):
        cmd = self._gammuCommand(number, message)
        print(cmd)
        if sshHost == None:
            print("SendSMS local mode")
            print("Would run: %s" % cmd)
        else:
            print("SendSMS ssh mode, host is %s" % (sshHost))
            print("Command is: %s" % cmd)
            client = SSHClient()
            client.load_system_host_keys()
            client.connect(sshHost)
            chan = client.get_transport().open_session()
            chan.exec_command(cmd)
            if chan.recv_exit_status() != 0:
                print("Command error")
                while chan.recv_stderr_ready():
                    print(chan.recv_stderr(1024))
            client.close()
            print("Closed")

if __name__ == '__main__':
    se = SendSMS()
    se.sendSMS("123456789", "This is a ' test of send sms")
    se.sendSMS("123456789", "This is a ' test of send sms", "tobias-debian32.local")
