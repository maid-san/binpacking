set b 10
set n 100

for n in (seq -w 10 10 $n)
    python main.py -n $n -b $b | grep time > output.txt
end