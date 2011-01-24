# This sends an sms using gammu either locally or by executing
# gammu on a remote host using ssh - ssh is expected to be setup
# for passwordless login from the sending host

class SendSMS:
    def sendSMS(self, number, message, sshHost=None):
        if sshHost == None:
            print("SendSMS local mode")
        else:
            print("SendSMS ssh mode, host is %s" % (sshHost))

if __name__ == '__main__':
    se = SendSMS()
    se.sendSMS("123456789", "This is a ' test of send sms")
    se.sendSMS("123456789", "This is a ' test of send sms", "tobias-debian32.local")
