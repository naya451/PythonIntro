import zlib
import struct
import sys
def read_git_object():
    data = sys.stdin.buffer.read()
    if data[0:4] == b'PACK':
        version = struct.unpack('>I', data[4:8])[0]
        num_objects = struct.unpack('>I', data[8:12])[0]
        print('pack:', version, num_objects)
        return
    signature, version = struct.unpack('>4sI', data[:8])
    if signature == b'\xFF\x74\x4F\x63' and version == 2:
        print("index:", struct.unpack('>' + ('I'*256), data[8:8+256*4])[255])
        return
    # If the file is not a pack file, try expecting it as a blob, tree, tag or commit object
    try:
        data_decompressed = zlib.decompress(data)
        type_and_size, content = data_decompressed.split(b'\x00', 1)
        type_, size = type_and_size.split(b' ', 1)

        if type_ == b'blob':
            print('blob:', len(content)) # size?
        elif type_ == b'tree':
            print("tree:")
            i = len(data_decompressed)
            while i > 20:
                num = content.split(b' ', 1)[0].decode()
                fd = content.split(b' ', 1)[1].split(b'\x00')[0].decode()
                k = content.split(b' ', 1)[1].split(b'\x00')[1]
                comm = content.split(b' ')[1].split(b'\x00')[1][:20].hex()
                content = content[len(num) + len(fd) + 22:]
                i -= len(num) + len(fd) + 22
                print('  ', comm, num, fd)
        elif type_ == b'tag':
            print('tag:', content.decode().split('\n')[2].split(' ')[1])
        elif type_ == b'commit':
            print('commit:', content.decode().split(' ')[1].split('\n')[0])
        else:
            print(type_, len(content))
    except:
        # If the file is not a git object
        print('unknown:')

read_git_object()