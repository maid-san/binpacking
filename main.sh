exec_python () {
    bin_size=$1
    n_min=$2
    n_max=$3
    dis=$4

    for n in `seq -w $n_min 100 $n_max`; do
        python main.py -n $n -b $bin_size -d $dis >> output$dis.txt
    done
}

exec_python 10 700 5000 1 &
exec_python 10 1300 5000 2 &
exec_python 10 1300 5000 4 &
exec_python 10 1600 5000 5 &
exec_python 10 1000 5000 6 &
exec_python 10 1000 5000 7 &
exec_python 10 500 5000 8 &
exec_python 10 300 5000 9 &
wait
exec_python 10 1300 5000 10 &
exec_python 10 1000 5000 11 &
exec_python 10 500 5000 12 &
exec_python 10 300 5000 13 &
