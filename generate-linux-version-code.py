#!/usr/bin/python3
from pathlib import Path

import os

ROOT_PATH = Path(__file__).root
OUT_PATH = ROOT_PATH / "os_dep/linux/custom_linux_version.h"

def get_linux_version_code():
    kernel_version = os.uname().release
    version_parts = kernel_version.split('.')

    major = int(version_parts[0])
    minor = int(version_parts[1])
    patch = int(version_parts[2].split('-')[0]) if len(version_parts) > 2 else 0

    return (major << 16) + (minor << 8) + patch

if __name__ == '__main__':
    linux_version_code = get_linux_version_code()
    constant = f"#define LINUX_VERSION_CODE {linux_version_code}"

    with open(OUT_PATH, 'w') as file:
        file.write(constant)