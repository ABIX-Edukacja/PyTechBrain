# coding=utf-8

import serial.tools.list_ports

class comport:    
    
    def main(self):
        try:
            plik = open('plik.txt', 'a')
            print (u"Lista portów szeregowych")
            print ("="*80)
            lists = list(serial.tools.list_ports.comports())
            lists = sorted(lists)
            for x in lists:
                print (x[0], "\t", x[1], "\t",x[2])
                plik.write(str(x[0])+'\n')
                plik.write(str(x[1])+'\n')
                plik.write(str(x[2])+'\n')
                plik.write('\n')
            print ("="*80)
            plik.close()
            print (u'Naciśnij CTRL + C')
            while True:
                pass

        except (KeyboardInterrupt, SystemExit):
             print (u"OK")

if __name__ == '__main__':
    comport = comport()
    comport.main()
