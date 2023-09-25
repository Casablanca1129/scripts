for file in *.zip; do
    base_name=$(basename "$file" .zip)
    unzip "$file" -d "$base_name"
    rm $file
done

