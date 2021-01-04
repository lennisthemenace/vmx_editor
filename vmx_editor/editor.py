import glob
from vmx_editor.variables import Variables
import re


class Editvmx(Variables):

	def find_vmx(self):
		for file in glob.glob("*.vmx"):
			return file

	def read_file(self, filename: str) -> list:
		with open(filename, 'r') as vmxfile:
			vmxfiledata = vmxfile.readlines()
		return vmxfiledata

	def dump_to_file(self, filename: str, content: list) -> None:
		with open(filename, 'w') as vmxfile:
			for line in content:
				vmxfile.write(line)

	def remove_setting(self, filename: str, settingname: str) -> int or None:
		vmxfiledata = self.read_file(filename)
		for line in vmxfiledata:
			if line.startswith(settingname) or line is settingname:
				place = vmxfiledata.index(line)
				vmxfiledata.remove(line)
				self.dump_to_file(filename, vmxfiledata)
				return place
		self.dump_to_file(filename, vmxfiledata)
		return None

	def read_setting(self, filename: str, settingname: str) -> str or None:
		vmxfiledata = self.read_file(filename)
		for line in vmxfiledata:
			if line.startswith(settingname) or line is settingname:
				value = re.search(r'\"(.+?)\"', line)
				return value.group().strip('"')
		return None

	def add_or_modify_setting(self, filename: str, settingname: str, value: str or int) -> None:
		settingline = "{} = \"{}\"\n".format(settingname, value)
		entry = self.remove_setting(filename, settingname)
		vmxfiledata = self.read_file(filename)
		if entry is None:
			vmxfiledata.append(settingline)
		else:
			vmxfiledata.insert(entry, settingline)
		self.dump_to_file(filename, vmxfiledata)


