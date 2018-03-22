bin/1bpkg_to_filter.py 
cat static_list.txt >> tw_float_list.txt
../YousList/bin/add_checksum.py tw_float_list.txt > a.txt && mv a.txt tw_float_list.txt
../YousList/bin/validate_checksum.py tw_float_list.txt 

