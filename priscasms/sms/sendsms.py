# This sends an sms using gammu either locally or by executing
# gammu on a remote host using ssh - ssh is expected to be setup
# for passwordless login from the sending host
import re, select
from paramiko import SSHClient

class SendSMS:
    def _gammuCommand(self, number, message):
        #return "echo gammu sendsms TEXT %s -text '%s'" % (number, re.escape(message))
        return "gammu savesms TEXT"

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
            chan.get_pty()
            chan.exec_command(cmd)
            (r, w, e) = select.select([chan], [chan], [chan])
            if r:
                print("READ")
                rstr = ''
                while chan.recv_ready():
                    rstr += chan.recv(1024)
                    print rstr
                # if we find the wanted string we can send the message
                # otherwise the output should be handled as error condition
                if rstr == "Enter message text and press ^D:\r\n":
                    print("Got WANTED string")
                else:
                    print("Got UNWANTED string - error condition")
            if w:
                print("WRITE")
            if e:
                print("ERROR")
            if chan.recv_exit_status() != 0:
                print("EXIT STATUS ERROR")
                while chan.recv_stderr_ready():
                    print(chan.recv_stderr(1024))
            client.close()
            print("Closed")

if __name__ == '__main__':
    HOST = "tobias-debian32.local"
    se = SendSMS()
    se.sendSMS("123456789", "This is a ' test of send sms", HOST)
