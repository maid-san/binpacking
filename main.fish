set bin_size 10
set n_max 1000
set dis 3

for n in (seq -w 10 10 $n_max)
    python main.py -n $n -b $bin_size -d $dis | tee /dev/stderr | tail -n 1 >> output3_1.txt
end
