"""access hw om platform ESP8266 """

import machine  # should import from esp8266- INCORRECT - imports from esp32 ( 1st exec env)
import esp32 # should fail to import        - INCORRECT - imports from esp32 ( 1st exec env)
import esp  # should import from 8266       - INCORRECT - imports from esp32 ( 1st exec env)
import pyb # Should Fail to import          - INCORRECT  - imports from 3rd exec environment


