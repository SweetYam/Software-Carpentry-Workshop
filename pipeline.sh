echo Cleaning Up the Folder
rm *.txt
rm *.tmp
rm *.csv

echo Download data
curl https://github.com/zonca/swcarpentry-workshop-pandas/blob/master/rawdata/rawdata.zip?raw=true -o rawdata.zip -L

echo Unpack data and Remove zip File
unzip rawdata.zip
rm rawdata.zip

echo Remove empty files such as .tmp
rm *tmp

echo Rename txt files to csv files
for f in *.txt
do
	mv $f ${f/txt/csv}
done

echo Available csv files. File listing
ls *.csv

for f in *data.csv
do
~/anaconda/Scripts/ipython.exe analyze_mosquito_data_script.py $f
done

mv *png figures/
mv *parameters.csv parameters/


