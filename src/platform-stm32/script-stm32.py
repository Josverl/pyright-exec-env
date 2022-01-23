"""access hw om platform stm32 - pyboard """

import machine  # should import from stm32  - INCORRECT - imports from esp32 ( 1st exec env)
import esp32 # should fail to import        - INCORRECT - imports from esp32 ( 1st exec env)
import esp  # should fail to import         - INCORRECT - imports from esp32 ( 1st exec env)
import pyb # Should Fail to import          - OK  


