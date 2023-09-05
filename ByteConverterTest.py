from ByteConverter import GigaBytes, MemoryUnit

if __name__ == "__main__":
    gigaBytes = GigaBytes(0.125)
    bytes = gigaBytes.convert(to=MemoryUnit.BYTES).bytes
    kiloBytes = gigaBytes.convert(to=MemoryUnit.KILOBYTES).kilobytes
    megaBytes = gigaBytes.convert(to=MemoryUnit.MEGABYTES).megabytes

    print(f"GigaBytes to Bytes: {bytes}")
    print(f"GigaBytes to KiloBytes: {kiloBytes}")
    print(f"GigaBytes to MegaBytes: {megaBytes}")
    print(f"GigaBytes: {gigaBytes.gigabytes}")