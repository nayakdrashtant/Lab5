import sys
class IPAddress():
    def __init__(self,ip_address,mask,cdir=24):
        if '/' in ip_address:
            self._address_val, self._cidr = ip.address.split('/') 
            self._address = map(int, self._address_val.split('.'))
        else:
            self._address = map(int, ip_address.split('.'))
            self._cidr = cdir
        self.ip_address = ip_address
        self.mask = mask

    def dec_to_binary(self):
        return map(lambda x: bin(x)[2:].zfill(8), self._address)
 
    def __str__(self):
        for i in self.dec_to_binary():
            print(i)
        return str(self.dec_to_binary())  + " " + str(self.mask)

i = input("Enter IP Address to get network information:")
m = input("Enter mask to get network information:")
myobj = IPAddress(i,m)
print(myobj)
