test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

run print_fires_help python ../../src/print_fires.py -h
assert_exit_code 0
assert_in_stdout "usage: print_fires"

run print_fires_default_res python ../../src/print_fires.py \
    --file-name "../data/test.csv" \
    --country-column 0 \
    --country "Argentina"
assert_exit_code 0
assert_stdout

run print_fires_choose_res python ../../src/print_fires.py \
    --file-name "../data/test.csv" \
    --country-column 0 \
    --country "United States of America" \
    --fires-column 10
assert_exit_code 0
assert_stdout

run print_fires_bad_file python ../../src/print_fires.py \
    --file-name "../data/no_test_file.csv" \
    --country-column 0 \
    --country "Argentina"
assert_exit_code 1

run print_fires_res_non_numeric python ../../src/print_fires.py \
    --file-name "../data/test.csv" \
    --country-column 0 \
    --country "United States of America" \
    --fires-column 0
assert_exit_code 1
assert_stdout "Could not convert result to float, so can't convert to int."

run print_fires_query_col_neg python ../../src/print_fires.py \
    --file-name "../data/test.csv" \
    --country-column -1 \
    --country "United States of America"
assert_exit_code 1
assert_stdout "Query column must be positive."

run print_fires_with_mean python ../../src/print_fires.py \
    --file-name "../data/test.csv" \
    --country-column 0 \
    --country "Zimbabwe" \
    --summary_function "mean"
assert_exit_code 0
assert_in_stdout 1991

run print_fires_with_median python ../../src/print_fires.py \
    --file-name "../data/test.csv" \
    --country-column 0 \
    --country "Belize" \
    --summary_function "median"
assert_exit_code 0
assert_in_stdout 1991

run print_fires_with_bad_summary python ../../src/print_fires.py \
    --file-name "../data/test.csv" \
    --country-column 0 \
    --country "Zimbabwe" \
    --summary_function "mode"
assert_exit_code 1
assert_stdout "Summary function must be "mean", "median", or "std_dev"."

run print_fires_res_non_numeric_with_mean python ../../src/print_fires.py \
    --file-name "../data/test.csv" \
    --country-column 0 \
    --country "United States of America" \
    --fires-column 0 \
    --summary_function "mean"
assert_exit_code 1
assert_stdout "Could not convert result to float, so can't convert to int."