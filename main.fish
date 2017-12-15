set bin_size 10
set n_max 5000
set dis 4

for n in (seq -w 100 100 $n_max)
    python main.py -n $n -b $bin_size -d $dis | tee /dev/stderr | tail -n 1 >> output4.txt &
end