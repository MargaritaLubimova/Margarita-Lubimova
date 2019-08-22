run_api() {
    cd api-playground && npm start
}

run_tests() {
   sleep 5 && echo "" && python3.6 tests_api.py
}

run_tests & run_api &
wait
