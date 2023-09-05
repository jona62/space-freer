from enum import Enum

class MemoryUnit(Enum):
    BYTES = 1
    KILOBYTES = 1024
    MEGABYTES = 1024 ** 2
    GIGABYTES = 1024 ** 3

class Bytes:
    def __init__(self, bytes: float):
        self.bytes = bytes
    
    def convert(self, to: MemoryUnit) -> 'Bytes':
        if to is MemoryUnit.BYTES:
            return self
        elif to is MemoryUnit.KILOBYTES:
            return KiloBytes(self.bytes / MemoryUnit.KILOBYTES.value)
        elif to is MemoryUnit.MEGABYTES:
            return MegaBytes(self.bytes / MemoryUnit.MEGABYTES.value)
        else:
            return GigaBytes(self.bytes / MemoryUnit.GIGABYTES.value)

class KiloBytes(Bytes):
    def __init__(self, kilobytes: float):
        super().__init__(bytes=kilobytes * MemoryUnit.KILOBYTES.value)
        self.kilobytes = kilobytes
    
    def convert(self, to: MemoryUnit) -> 'KiloBytes':
        if to is MemoryUnit.BYTES:
            return Bytes(self.bytes)
        elif to is MemoryUnit.KILOBYTES:
            return self
        elif to is MemoryUnit.MEGABYTES:
            return MegaBytes(self.bytes / MemoryUnit.MEGABYTES.value)
        else:
            return GigaBytes(self.bytes / MemoryUnit.GIGABYTES.value)
        
class MegaBytes(KiloBytes):
    def __init__(self, megabytes: float):
        super().__init__(kilobytes=megabytes * MemoryUnit.KILOBYTES.value)
        self.megabytes = megabytes
    
    def convert(self, to: MemoryUnit) -> 'MegaBytes':
        if to is MemoryUnit.BYTES:
            return Bytes(self.bytes)
        elif to is MemoryUnit.KILOBYTES:
            return KiloBytes(self.kilobytes)
        elif to is MemoryUnit.MEGABYTES:
            return self
        else:
            return GigaBytes(self.bytes / MemoryUnit.GIGABYTES.value)

class GigaBytes(MegaBytes):
    def __init__(self, gigabytes: float):
        super().__init__(megabytes=gigabytes * MemoryUnit.KILOBYTES.value)
        self.gigabytes = gigabytes
    
    def convert(self, to: MemoryUnit) -> 'GigaBytes':
        if to is MemoryUnit.BYTES:
            return Bytes(self.bytes)
        elif to is MemoryUnit.KILOBYTES:
            return KiloBytes(self.kilobytes)
        elif to is MemoryUnit.MEGABYTES:
            return MegaBytes(self.megabytes)
        else:
            return self

def human_readable_size(size_bytes: Bytes) -> str:
    if size_bytes.bytes >= MemoryUnit.GIGABYTES.value:
        return "{:.2f} GB".format(size_bytes.convert(to=MemoryUnit.GIGABYTES).gigabytes)
    elif size_bytes.bytes >= MemoryUnit.MEGABYTES.value:
        return "{:.2f} MB".format(size_bytes.convert(to=MemoryUnit.MEGABYTES).megabytes)
    elif size_bytes.bytes >= MemoryUnit.KILOBYTES.value:
        return "{:.2f} KB".format(size_bytes.convert(to=MemoryUnit.KILOBYTES).kilobytes)
    else:
        return "{} bytes".format(size_bytes.convert(to=MemoryUnit.BYTES).bytes)
