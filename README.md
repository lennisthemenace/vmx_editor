# vmx_editor

Python module for safely reading and editing .vmx files for vmware virtual machines. 
This is especially helpful if the user only has
vmware Player

Example:
```Python
from vmx_editor.editor import Editvmx
vm = Editvmx()

vm.add_or_modify_setting(vm.find_vmx(), vm.Settings.Hardware.VIRTUAL_MEMORY, 4000)
vm.add_or_modify_setting(vm.find_vmx(), vm.Settings.Connection.FIRST_ETHERNET_CONNECTION_TYPE, vm.Values.Connection.BRIDGED)
print(vm.read_setting(vm.find_vmx(), vm.Settings.Hardware.VIRTUAL_MEMORY))
vm.add_or_modify_setting(vm.find_vmx(), vm.Settings.Hardware.HARDWARE_VERSION, 11)
```
Install:
```shell script
pip install vmx-editor
```