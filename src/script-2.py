"""sanity check """

# this script is located in a folder with NO additional Search Paths

import machine  # should to import          - INCORRECT - imports from esp32 ( 1st exec env)
import esp32 # should fail to import        - INCORRECT - imports from esp32 ( 1st exec env)
import esp  # should import from 8266       - INCORRECT - imports from esp32 ( 1st exec env)
import pyb # Should Fail to import          - INCORRECT  - imports from 3rd exec environment


