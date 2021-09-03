import network

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
print("\n".join([x[0].decode() for x in sta_if.scan()]))
