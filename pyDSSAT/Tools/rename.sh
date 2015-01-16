for file in *.FOR; do
  mv "$file" "`basename $file .FOR`.f90"
done

for file in *.for; do
  mv "$file" "`basename $file .for`.f90"
done
