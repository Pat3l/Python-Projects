from speedtest import Speedtest
import speedtest
wifi = speedtest.Speedtest()

print(wifi.download())
print(wifi.upload())