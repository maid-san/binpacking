set b 10
set n 50

for n in (seq -w 10 10 $n)
    python main.py -n $n -b $b | tee /dev/stderr | tail -n 1 >> output.txt
end