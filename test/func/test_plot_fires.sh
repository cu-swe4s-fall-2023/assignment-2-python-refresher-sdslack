test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run plot_fires_help python ../../src/plot_fires.py -h
assert_exit_code 0
assert_in_stdout "usage: plot_fires"

run plot_fires python ../../src/plot_fires.py \
    --file-name "../data/test_col.txt" \
    --output-path ./ \
    --title "Test Plot" \
    --x-label "X" \
    --y-label "Y"
assert_exit_code 0
assert_equal "test_col_hist.png" $(ls "test_col_hist.png")

run plot_fires_file_not_found python ../../src/plot_fires.py \
    --file-name "../data/no_file.txt" \
    --output-path ./ \
    --title "Test Plot" \
    --x-label "X" \
    --y-label "Y"
assert_exit_code 1
assert_in_stdout "File not found:"

run plot_fires_missing_arg python ../../src/plot_fires.py \
    --file-name "../data/no_file.txt" \
    --output-path ./ \
    --x-label "X" \
    --y-label "Y"
assert_exit_code 2
assert_in_stderr "usage: plot_fires"