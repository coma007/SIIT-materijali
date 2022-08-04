import sys

current_key = ""
key = ""
last_value = 0
diff_down = 0
diff_up = 0

for line in sys.stdin:
    line = line.strip()
    key, val = line.split("\t")
    try:
        val = int(val.strip())
    except Exception:
        pass
    if last_value == 0:
        last_value = val
        continue
    key, date = key.split("-")
    if current_key == key:
        diff = last_value - val
        if diff < 0 and diff < diff_down:
            diff_down = diff
        if diff > 0 and diff > diff_up:
            diff_up = diff
    else:
        if current_key:
            print("%s\t%s\t%s" % (current_key, diff_down, diff_up))
        current_key = key
        last_value = val
        diff_up = 0
        diff_down = 0


if current_key == key:
    print("%s\t%s\t%s" % (key, diff_down, diff_up))
