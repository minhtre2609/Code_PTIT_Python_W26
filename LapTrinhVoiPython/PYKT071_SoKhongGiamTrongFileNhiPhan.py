import pickle
import struct

def load_ints(filename):
    with open(filename, "rb") as f:
        data = f.read()
    if data[:4] != b"\xac\xed\x00\x05":
        return pickle.loads(data)
    pos = 4
    n = len(data)
    handles = []
    unpack_from = struct.unpack_from

    def read_utf():
        nonlocal pos
        ln = unpack_from(">H", data, pos)[0]
        pos += 2
        s = data[pos : pos + ln].decode("utf-8", "replace")
        pos += ln
        return s

    def skip_block_or_obj():
        nonlocal pos
        while pos < n:
            t = data[pos]
            if t == 0x78:
                pos += 1
                return
            if t == 0x77:
                pos += 2 + data[pos + 1]
            elif t == 0x7A:
                pos += 5 + unpack_from(">I", data, pos + 1)[0]
            else:
                read_obj()

    def read_classdesc():
        nonlocal pos
        b = data[pos]
        pos += 1
        if b == 0x70:
            return None
        if b == 0x71:
            h = unpack_from(">I", data, pos)[0]
            pos += 4
            return handles[h - 0x7E0000]
        if b == 0x72:
            name = read_utf()
            pos += 9
            fc = unpack_from(">H", data, pos)[0]
            pos += 2
            desc = [name, []]
            handles.append(desc)
            for _ in range(fc):
                tc = chr(data[pos])
                pos += 1
                fname = read_utf()
                if tc == "L" or tc == "[":
                    read_obj()
                desc[1].append((tc, fname))
            skip_block_or_obj()
            sup = read_classdesc()
            desc.append(sup)
            return desc
        raise ValueError(b)

    def read_obj():
        nonlocal pos
        while pos < n and data[pos] == 0x79:
            pos += 1
            handles.clear()
        b = data[pos]
        pos += 1
        if b == 0x70:
            return None
        if b == 0x71:
            h = unpack_from(">I", data, pos)[0]
            pos += 4
            return handles[h - 0x7E0000]
        if b == 0x74:
            s = read_utf()
            handles.append(s)
            return s
        if b == 0x7C:
            ln = unpack_from(">Q", data, pos)[0]
            pos += 8
            s = data[pos : pos + ln].decode("utf-8", "replace")
            pos += ln
            handles.append(s)
            return s
        if b == 0x73:
            desc = read_classdesc()
            name = desc[0]
            if name == "java.lang.Integer":
                val = unpack_from(">i", data, pos)[0]
                pos += 4
                handles.append(val)
                return val
            if name == "java.util.ArrayList":
                idx = len(handles)
                handles.append(None)
                size = unpack_from(">i", data, pos)[0]
                pos += 4
                if pos < n and data[pos] == 0x77:
                    pos += 2 + data[pos + 1]
                elif pos < n and data[pos] == 0x7A:
                    pos += 5 + unpack_from(">I", data, pos + 1)[0]
                arr = [0] * size
                for i in range(size):
                    arr[i] = read_obj()
                if pos < n and data[pos] == 0x78:
                    pos += 1
                handles[idx] = arr
                return arr
            val = unpack_from(">i", data, pos)[0]
            pos += 4
            handles.append(val)
            return val
        raise ValueError(b)

    return read_obj()

ok = [False] * 10000
for x in range(10, 10000):
    s = str(x)
    if all(s[i] <= s[i + 1] for i in range(len(s) - 1)):
        ok[x] = True

c1 = [0] * 10000
for x in load_ints("DATA1.in"):
    if 10 <= x < 10000 and ok[x]:
        c1[x] += 1

c2 = [0] * 10000
for x in load_ints("DATA2.in"):
    if 10 <= x < 10000 and ok[x]:
        c2[x] += 1

out = []
for x in range(10, 10000):
    if c1[x] and c2[x]:
        out.append(f"{x} {c1[x]} {c2[x]}")
print("\n".join(out))