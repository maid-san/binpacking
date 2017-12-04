set bin_size 10
set n_max 1000
set dis 2

for n in (seq -w 880 10 $n_max)
    set command python main.py -n $n -b $bin_size -d $dis
    echo $command  
    eval $command | tee /dev/stderr | tail -n 1 >> output2.txt
end
