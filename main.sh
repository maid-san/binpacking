exec_python () {
    bin_size=$1
    n_min=$2
    n_max=$3
    dis=$4

    for n in `seq -w $n_min 100 $n_max`; do
        python main.py -n $n -b $bin_size -d $dis >> output$dis.txt
    done
}

exec_python 10 100 2500 2 &
exec_python 10 100 2500 4 &
exec_python 10 100 2500 5 &
exec_python 10 100 2500 8 &
exec_python 10 100 2500 10 &
exec_python 10 100 2500 12 &
exec_python 10 100 2500 3 &
wait
exec_python 10 100 2500 1 &
exec_python 10 100 2500 6 &
exec_python 10 100 2500 7 &
exec_python 10 100 2500 9 &
exec_python 10 100 2500 11 &
exec_python 10 100 2500 13 &
