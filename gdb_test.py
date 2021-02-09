###########################################################
#
# @author Gabriel Dobato dobatog@gmail.com
# @date   
# @version 0.0.1
#
###########################################################

import os
import signal
import subprocess
import sys
from   target import Target



STM32F4_target = Target( )
STM32F4.flash( 'App_Example.hex',
                'STM32F429.jflash')
STM32F4.GDB().run_server()
STM32F4.GDB().run_client_test('App_Example.elf',
                               'gdb_target_script.py')
STM32F4.GDB().terminate_server()

