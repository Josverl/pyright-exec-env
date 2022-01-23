"""access hw om platform esp32 """

import machine  # should import from esp32  - OK 
import esp32 # should import from esp32     - OK
import esp  # should import from esp32      - OK 
import pyb # Should Fail to import          - INCORRECT  - imports from 3rd exec environment



