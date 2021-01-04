class Variables:

    class Settings:

        class Tools:
            SYNC_TIME_WITH_HOST = "tools.syncTime"

        class Connection:
            FIRST_ETHERNET_CONNECTION_TYPE = "ethernet0.connectionType"
            SECOND_ETHERNET_CONNECTION_TYPE = "ethernet1.connectionType"

        class Hardware:
            VIRTUAL_MEMORY = "memsize"
            HARDWARE_VERSION = "virtualHW.version"
            NUMBER_OF_CORES = "numvcpus"
            CORES_PER_SOCKET = "cpuid.coresPerSocket"

        DISPLAY_NAME = "displayName"
        GUEST_OS = "guestOS"

    class Values:

        TRUE = "TRUE"
        FALSE = "FALSE"

        class Connection:
            BRIDGED = "bridged"
            NAT = "nat"

        class OS:
            WINDOWS_VISTA = "winVista"
            WINDOWS_VISTA_64 = "winVista-64"
            WINDOWS_7 = "windows7"
            WINDOWS_7_64 = "windows7-64"
            WINDOWS_8 = "windows8"
            WINDOWS_8_64 = "windows8-64"
            WINDOWS_10 = "windows9"
            WINDOWS_10_64 = "windows9-64"
            UBUNTU = "ubuntu"
            UBUNTU_64 = "ubuntu-64"
            CENTOS_7_64 = "centos7-64"
