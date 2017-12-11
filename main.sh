bin_size=10
n_max=20
dis=1

for n in `seq -w 10 1 $n_max`; do
    python ./main.py -n $n -b $bin_size -d $dis | tee /dev/stderr | tail -n 1 >> output.txt
done
