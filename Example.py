from vmx_editor.editor import Editvmx
vm = Editvmx()

vm.add_or_modify_setting(vm.find_vmx(), vm.Settings.Hardware.VIRTUAL_MEMORY, 4000)
vm.add_or_modify_setting(vm.find_vmx(), vm.Settings.Connection.FIRST_ETHERNET_CONNECTION_TYPE, vm.Values.Connection.BRIDGED)
print(vm.read_setting(vm.find_vmx(), vm.Settings.Hardware.VIRTUAL_MEMORY))
vm.add_or_modify_setting(vm.find_vmx(), vm.Settings.Hardware.HARDWARE_VERSION, 11)