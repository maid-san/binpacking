set bin_size 10
set n_max 1000
set dis 1

for n in (seq -w 500 10 $n_max)
    set command python main.py -n $n -b $bin_size -d $dis | tee /dev/stderr | tail -n 1 >> output.txt
    echo $command  
    eval $command
end
