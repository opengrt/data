
# Assumes that the html files are already uncompressed

rm -f data.csv

find -name *.html -exec ./parser.py {} \; > data.csv

