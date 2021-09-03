import micropython
micropython.mem_info()

import esp
print("flash size: " + str(esp.flash_size()))
