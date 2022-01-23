"""sanity check """

# This script is located in a folder with NO additional Search Paths
# None of the below imports should resolve 

import machine # should fail to import      - INCORRECT 
import esp32 # should fail to import        - INCORRECT 
import esp  # should fail to import         - INCORRECT 
import pyb # Should Fail to import          - INCORRECT 


