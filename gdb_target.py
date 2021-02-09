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

class Target:
    def __init__(self):
        pass

    def flash(self, hex , jflash_cfg):
        self.jflash_exe     = 'JFlash.exe'
        try:
            cmd = '{} -openprj{} -open{} -auto -exit'.format(self.jflash_exe, jflash_cfg, hex)
            subprocess.check_call(cmd)
        except OSError:
            print('{} not found'.format(self.jflash_exe))
            sys.exit(1)
        except subprocess.CalledProcessError:
            print("Something went wrong while flashing the target")
            sys.exit(1)

    def __del__(self):
        pass


    class GDB:
        def __init__(self):
            self.jlinkGDBServer = 'JLinkGDBServerCL.exe'
            self.gdb_exe        = 'arm-none-eabi-gdb-py.exe'

        def run_server(self):
            try:
                cmd = '{} -select USB -device Cortex-M4 -endian little -if SWD -speed 4000 -noir -LocalhostOnly'.format(self.jlinkGDBServer)
                subprocess.Popen(cmd, shell=True)
            except OSError:
                print('{} not found'.format(self.jlinkGDBServer))
                sys.exit(1)
            except subprocess.CalledProcessError as error:
                print(error.out)
                sys.exit(1)

        def terminate_server(self):
            """workaround. Otherwise additional modules are needed"""
            os.system('TASKKILL /F /IM {}'.format(self.jlinkGDBServer))
            pass

        def run_client_test(self, elf, test_script):
            """workaround. Not found the way how to pass arg to execute script through GDB"""
            try:
                f = open("st_temp.txt","w")
                f.write(elf)
                f.close()
            except:
                print("Something went wrong while writting settings of gdb client")
                sys.exit(1)
            try:
                cmd = '{} -x {}'.format(self.gdb_exe,test_script)
                subprocess.call(cmd)
            except OSError:
                print('{} not found'.format(self.gdb_exe))
                sys.exit(1)
            except subprocess.CalledProcessError:
                print("Something went wrong while running gdb client")
                sys.exit(1)

        def __del__(self):
            pass
