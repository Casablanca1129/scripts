find . -type d | while read directory; do 
    touch ${directory}/0xdf 2>/dev/null && echo "${directory} - write file" && rm ${directory}/0xdf; 
    mkdir ${directory}/0xdf 2>/dev/null && echo "${directory} - write dir" && rmdir ${directory}/0xdf; 
done
